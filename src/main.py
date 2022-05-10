import datetime
import enum
import re
import textwrap
from collections import (
    defaultdict,
    deque,
)
from typing import (
    Dict,
    Optional,
    Tuple,
    Type,
    Union,
)

import click as click

from test_cases import (
    Action,
    ACTIONS,
    SkipException,
)

CONTAINERS = (dict, list, set, tuple, deque)
INDENT = '  '

CollectionType = Union[
    Type[deque],
    Type[dict],
    Type[list],
    Type[set],
    Type[tuple],
]
Results = Dict[CollectionType, Dict[str, Tuple[str, float]]]


def _echo(
        message: str,
        *args,
        cr: bool = False,
        dedent: bool = True,
        indent: Optional[int] = None,
        prepend_empty_line: bool = False,
        strip: bool = True,
        **kwargs
) -> None:
    # dedent should stay before strip as it allows you to write multiline strings
    # with empty starting line to make the dedent actually work
    if dedent:
        message = textwrap.dedent(message)
    if strip:
        message = message.strip()
    if indent:
        message = textwrap.indent(message, INDENT * indent)
    if prepend_empty_line:
        message = f'\n{message}'
    if cr:
        message = f'{message}\r'
    click.echo(message, *args, **kwargs)


def _results_by_case(results: Results) -> None:
    actions = sorted(Action, key=lambda x: x.value)
    printed_cases = set()
    for action in actions:
        for results_container, container_results in results.items():
            for case in container_results.keys():
                if case in printed_cases or not re.match(fr'^{action} \(\d+\)$', case):
                    continue
                printed_cases.add(case)
                _echo(case, indent=1)
                for container in CONTAINERS:
                    try:
                        code, time = results[container][case]
                    except KeyError:
                        continue
                    _echo(f'{container.__name__.ljust(5)} {time}', indent=2)


def _results_by_container(results: Results) -> None:
    for container_type, container_results in results.items():
        _echo(str(container_type), indent=1)
        for case in sorted(container_results):
            time = container_results[case][1]
            _echo(f'{case.ljust(15)} {time}', indent=2)


def _results_in_markdown(results: Results) -> None:
    _echo(f'|   | {" | ".join(x.__name__ for x in results)} |')
    _echo(f'|--{"--|--" * len(results)}--|')
    # TODO: reduce duplication with _results_by_case
    actions = sorted(Action, key=lambda x: x.value)
    printed_cases = set()
    for action in actions:
        for results_container, container_results in results.items():
            for case in container_results.keys():
                if case in printed_cases or not re.match(fr'^{action} \(\d+\)$', case):
                    continue
                _echo(f'| {case} |', nl=False)
                printed_cases.add(case)
                for container in results:
                    try:
                        _, time = results[container][case]
                    except KeyError:
                        time = '-'
                    _echo(
                        f' {time} |',
                        dedent=False,
                        nl=False,
                        strip=False,
                    )
                _echo('')  # new line


@enum.unique
class ResultBy(enum.Enum):
    CASE = 'by-case'
    CONTAINER = 'by-container'
    MARKDOWN = 'markdown-table'

    # TODO: write to a file

    def print(self, results: Results) -> None:
        _echo(f'The results {self.value}', prepend_empty_line=True)
        _RESULTS_BY[self](results)


_RESULTS_BY = {
    ResultBy.CASE: _results_by_case,
    ResultBy.CONTAINER: _results_by_container,
    ResultBy.MARKDOWN: _results_in_markdown,
}


class EnumChoice(click.Choice):

    # Copied from click.Choice just to modify self.choices -> str on the first line
    def get_metavar(self, param: click.Option) -> str:
        choices_str = "|".join((x.value for x in self.choices))

        # Use curly braces to indicate a required argument.
        if param.required and param.param_type_name == "argument":
            return f"{{{choices_str}}}"

        # Use square braces to indicate an option or optional argument.
        return f"[{choices_str}]"

    def convert(self, value: str, *_) -> ResultBy:
        return ResultBy(value)


def _execute_cases(*, repeat: int, test_cases: Tuple[int, ...]) -> Results:
    results = defaultdict(dict)
    prev_line_len = 0
    # TODO: control which containers to test with an option
    for container in CONTAINERS:
        for action, logic in ACTIONS[container].items():
            if logic._container is not container:
                # TODO: refactor so this could not be possible
                raise Exception(f'{container} contained logic for {logic._container}')
            for item_count in test_cases:
                case = f'{action} ({item_count})'
                now = datetime.datetime.now(tz=datetime.timezone.utc)
                exec_text = f'Executing case `{case}`. Started at {now}'
                # TODO: see if possible to get \r working with click.echo
                print(exec_text.ljust(prev_line_len, ' '), end='\r')
                prev_line_len = len(exec_text)
                try:
                    code, time = logic.timeit(
                        item_count=item_count,
                        repeat=repeat,
                    )
                except SkipException:
                    continue
                results[container][case] = (code, time)
    return results


def _print_code(results: Results) -> None:
    _echo('Code by container by case', prepend_empty_line=True)
    for results_container, container_results in results.items():
        for case, case_values in container_results.items():
            code, _, = case_values
            # The wrapping text must be dedented before the code is
            # included or dedent will not work .
            code_wrap = textwrap.dedent('''
                    ```python
                    {code}
                    ```
                    ''').strip()
            _echo(
                f'{results_container.__name__} - {case}',
                prepend_empty_line=True,
            )
            _echo(code_wrap.format(code=code))


@click.command()
@click.option(
    '--item-count',
    'test_cases',
    required=True,
    type=int,
    multiple=True,
    help='''
        The number of items in the container. Depending on the test case this 
        may be the number of items in the container before the tested action 
        (e.g. adding to or removing from the conatiner) 
        or how many items the container will contain after the tested action 
        (e.g. initialisation cases).
        
        May be given multiple times to run the test cases with multiple 
        different item counts at once.
    ''',
)
@click.option(
    '--repeat',
    type=int,
    default=1_000,
    help='The amount of times each test case is executed.',
)
@click.option(
    '--print-code',
    type=bool,
    is_flag=True,
    default=False,
    help='Print the code used in each of the executed test cases.'
)
@click.option(
    '--print-results',
    type=EnumChoice(ResultBy),
    multiple=True,
    help='''
    How to print the results.
    
    e.g. python3 main.py --item-count 10 --print-results by-container
    ```
    ...
    The results by-container
      <class 'dict'>
        add right (10)  <RESULT>
        consume FIFO (10) <RESULT>
        ...
      <class 'list'>
        add right (10)  <RESULT>
        consume FIFO (10) <RESULT>
        ...
    ```
    ''',
)
def cmd(
        *,
        repeat: int,
        test_cases: Tuple[int, ...],
        print_results: Tuple[ResultBy, ...],
        print_code: bool,
):
    """
    Executes test cases on python containers to benchmark the performance
    of different actions in various situations.
    """
    _echo(f'''
        Test case confs
            Item counts: {', '.join((str(x) for x in test_cases))}
            Test case repeats: {repeat}
    ''')
    results = _execute_cases(repeat=repeat, test_cases=test_cases)
    if print_code:
        _print_code(results)
    for result_by in print_results:
        result_by.print(results)


if __name__ == '__main__':
    cmd()
