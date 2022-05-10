import enum
import textwrap
import timeit
from collections import deque
from typing import (
    Tuple,
)

READ_RAND_LOGIC = 'c_filled[i_rand]'
READ_CENTER_LOGIC = 'c_filled[i_center]'

COPY_LOGIC = 'copy.copy(c_filled)'
DEEPCOPY_LOGIC = 'copy.deepcopy(c_nested_filled)'
IN_LOGIC = 'v_rand in c_filled'
INIT_EMPTY_LOGIC = '{container}()'
INIT_LOGIC = '{container}(items)'
INIT_AND_FILL_LOGIC = f'''
    c = {INIT_EMPTY_LOGIC}
    for i in items:
        %s
'''
ITER_LOGIC = '''
    for _ in c_filled:
        pass
'''
LEN_LOGIC = 'len(c_filled)'
RANDOM_INDEX_LOGIC = 'random.choice({items_range})'
READ_FIRST_LOGIC = 'c_filled[0]'
READ_LAST_LOGIC = 'c_filled[i_last]'


@enum.unique
class Action(str, enum.Enum):
    INIT = 'init'
    ITERATE = 'iterate'
    ITERATE_ITEMS = 'iterate dict items'
    INIT_AND_FILL = 'init empty and fill'
    APPEND = 'add right'
    PREPEND = 'add left'
    ADD = 'add unordered'
    READ_FIRST = 'read first'
    READ_LAST = 'read last'
    READ_RANDOM = 'read random'
    READ_CENTER = 'read center'
    DELETE = 'delete'  # TODO: implement
    FIFO = 'consume FIFO'
    LIFO = 'consume LIFO'
    CONSUME = 'consume random order'
    LEN = 'len'
    IN = 'in'
    IN_DICT_VALUES = 'in dict values'
    COPY = 'copy'
    DEEPCOPY = 'deepcopy'


@enum.unique
class Prep(str, enum.Enum):
    INIT_EMPTY = 'c_empty = {container}()'
    INIT_FILLED = f'c_filled = {INIT_LOGIC}'
    DICT_VALUES = 'd_values = c_filled.values()'
    DICT_ITEMS = 'd_items = c_filled.items()'
    RANDOM_INDEX = f'i_rand = {RANDOM_INDEX_LOGIC} if {{items_range}} else "foo"'
    CENTER_INDEX = 'i_center = int(len({items_range}) / 2)'
    LAST_INDEX = 'i_last = len({items_range}) - 1 if {container} is dict else -1'
    RANDOM_VALUE = f'v_rand = {RANDOM_INDEX_LOGIC} if {{items_range}} else "foo"'
    INIT_NESTED_FILLED = f'''
        if {{container}} is dict:
            c_nested_filled = {{container}}((i, {INIT_LOGIC}) for i in range(100))
        else:
            c_nested_filled = {{container}}({INIT_LOGIC} for _ in range(100))
    '''


class SkipException(Exception):
    pass


class Logic:
    _SETUP = textwrap.dedent('''
        import copy
        import random
        from collections import deque
    ''').strip()

    def __init__(
            self,
            *,
            container,
            code: str,
            preparations: Tuple[Prep, ...] = None,
            reset_every_time: bool = True,
            skip_empty: bool = False,
    ):
        self._container = container
        self._code = textwrap.dedent(code).strip()
        self._preparations = preparations or tuple()
        self._reset_every_time = reset_every_time
        self._skip_empty = skip_empty

    def timeit(
            self,
            *,
            item_count: int,
            repeat: int,
    ) -> Tuple[str, float]:
        if self._skip_empty and not item_count:
            raise SkipException('Skipping due to no items')
        items_range = f'range({item_count})' if item_count else 'range(0)'
        if self._container is dict:
            items_code = f'items = [(x, x) for x in {items_range}]'
        else:
            items_code = f'items = list({items_range})'

        code_fills = {
            'container': self._container.__name__,
            'items_range': items_range,
        }

        code = self._code.format(**code_fills)

        setup = self._SETUP
        setup += f'\n{items_code}'
        for prep in self._preparations:
            setup += f'\n{textwrap.dedent(prep.value)}'
        setup = setup.format(**code_fills)

        time = sum(timeit.repeat(code, setup=setup, number=1, repeat=repeat))
        executed_code = f'# setup code\n{setup}\n\n# timed code\n{code}'
        return executed_code, time


ACTIONS = {
    dict: {
        Action.INIT: Logic(
            container=dict,
            code=INIT_LOGIC,
        ),
        Action.INIT_AND_FILL: Logic(
            container=dict,
            code=f'''
                c = {INIT_EMPTY_LOGIC}
                for k, v in items:
                    c[k] = v
            ''',
            skip_empty=True,
        ),
        Action.ITERATE: Logic(
            container=dict,
            code=ITER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.ITERATE_ITEMS: Logic(
            container=dict,
            preparations=(
                Prep.INIT_FILLED,
                Prep.DICT_ITEMS,
            ),
            code=f'''
                for _, _ in d_items:
                    pass
            ''',
            skip_empty=True,
        ),
        Action.APPEND: Logic(
            container=dict,
            code='c_filled["foo"] = "foo"',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.READ_FIRST: Logic(
            container=dict,
            code=READ_FIRST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.READ_LAST: Logic(
            container=dict,
            code=READ_LAST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.LAST_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_RANDOM: Logic(
            container=dict,
            code=READ_RAND_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_CENTER: Logic(
            container=dict,
            code=READ_CENTER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.CENTER_INDEX,
            ),
            skip_empty=True,
        ),
        Action.IN: Logic(
            container=dict,
            code='i_rand in c_filled',
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_INDEX,
            ),
        ),
        Action.IN_DICT_VALUES: Logic(
            container=dict,
            code='v_rand in d_values',
            preparations=(
                Prep.INIT_FILLED,
                Prep.DICT_VALUES,
                Prep.RANDOM_VALUE,
            ),
        ),
        Action.LEN: Logic(
            container=dict,
            code=LEN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.FIFO: Logic(
            container=dict,
            code=f'''
                while c_filled:
                    _ = c_filled.pop(next(iter(c_filled)))
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.LIFO: Logic(
            container=dict,
            code=f'''
                while c_filled:
                    _ = c_filled.popitem()
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.COPY: Logic(
            container=dict,
            code=COPY_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.DEEPCOPY: Logic(
            container=dict,
            code=DEEPCOPY_LOGIC,
            preparations=(
                Prep.INIT_NESTED_FILLED,
            ),
        ),
    },
    list: {
        Action.INIT: Logic(
            container=list,
            code=INIT_LOGIC,
        ),
        Action.INIT_AND_FILL: Logic(
            container=list,
            code=INIT_AND_FILL_LOGIC % 'c.append(i)',
            preparations=tuple(),
            skip_empty=True,
        ),
        Action.ITERATE: Logic(
            container=list,
            code=ITER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.APPEND: Logic(
            container=list,
            code='c_filled.append("foo")',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.PREPEND: Logic(
            container=list,
            code='c_filled.insert(0, "foo")',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.READ_FIRST: Logic(
            container=list,
            code=READ_FIRST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.READ_LAST: Logic(
            container=list,
            code=READ_LAST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.LAST_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_RANDOM: Logic(
            container=list,
            code=READ_RAND_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_CENTER: Logic(
            container=list,
            code=READ_CENTER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.CENTER_INDEX,
            ),
            skip_empty=True,
        ),
        Action.IN: Logic(
            container=list,
            code=IN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_VALUE,
            ),
        ),
        Action.LEN: Logic(
            container=list,
            code=LEN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.FIFO: Logic(
            container=list,
            code=f'''
                while c_filled:
                    _ = c_filled.pop(0)
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.LIFO: Logic(
            container=list,
            code=f'''
                while c_filled:
                    _ = c_filled.pop()
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.COPY: Logic(
            container=list,
            code=COPY_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.DEEPCOPY: Logic(
            container=list,
            code=DEEPCOPY_LOGIC,
            preparations=(
                Prep.INIT_NESTED_FILLED,
            ),
        ),
    },
    set: {
        Action.INIT: Logic(
            container=set,
            code=INIT_LOGIC,
        ),
        Action.INIT_AND_FILL: Logic(
            container=set,
            code=INIT_AND_FILL_LOGIC % 'c.add(i)',
            preparations=tuple(),
            skip_empty=True,
        ),
        Action.ITERATE: Logic(
            container=set,
            code=ITER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.ADD: Logic(
            container=set,
            code='c_filled.add("foo")',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.IN: Logic(
            container=set,
            code=IN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_VALUE,
            ),
        ),
        Action.LEN: Logic(
            container=set,
            code=LEN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.CONSUME: Logic(
            container=set,
            code=f'''
                while c_filled:
                    c_filled.pop()
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.COPY: Logic(
            container=set,
            code=COPY_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
    },
    tuple: {
        Action.INIT: Logic(
            container=tuple,
            code=INIT_LOGIC,
        ),
        Action.INIT_AND_FILL: Logic(
            container=tuple,
            code=INIT_AND_FILL_LOGIC % 'c = c + (i,)',
            preparations=tuple(),
            skip_empty=True,
        ),
        Action.ITERATE: Logic(
            container=tuple,
            code=ITER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.IN: Logic(
            container=tuple,
            code=IN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_VALUE,
            ),
        ),
        Action.LEN: Logic(
            container=tuple,
            code=LEN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.FIFO: Logic(
            container=tuple,
            code=f'''
                while c_filled:
                    _ = c_filled[0]
                    c_filled = c_filled[1:]
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.LIFO: Logic(
            container=tuple,
            code=f'''
                while c_filled:
                    _ = c_filled[-1]
                    c_filled = c_filled[:-1]
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.READ_FIRST: Logic(
            container=tuple,
            code=READ_FIRST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.READ_LAST: Logic(
            container=tuple,
            code=READ_LAST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.LAST_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_RANDOM: Logic(
            container=tuple,
            code=READ_RAND_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_CENTER: Logic(
            container=tuple,
            code=READ_CENTER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.CENTER_INDEX,
            ),
            skip_empty=True,
        ),
        Action.COPY: Logic(
            container=tuple,
            code=COPY_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.DEEPCOPY: Logic(
            container=tuple,
            code=DEEPCOPY_LOGIC,
            preparations=(
                Prep.INIT_NESTED_FILLED,
            ),
        ),
    },
    deque: {
        Action.INIT: Logic(
            container=deque,
            code=INIT_LOGIC,
        ),
        Action.INIT_AND_FILL: Logic(
            container=deque,
            code=INIT_AND_FILL_LOGIC % 'c.append(i)',
            preparations=tuple(),
            skip_empty=True,
        ),
        Action.ITERATE: Logic(
            container=deque,
            code=ITER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.APPEND: Logic(
            container=deque,
            code='c_filled.append("foo")',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.PREPEND: Logic(
            container=deque,
            code='c_filled.appendleft("foo")',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.IN: Logic(
            container=deque,
            code=IN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_VALUE,
            ),
        ),
        Action.LEN: Logic(
            container=deque,
            code=LEN_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.FIFO: Logic(
            container=deque,
            code=f'''
                while c_filled:
                    _ = c_filled.popleft()
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.LIFO: Logic(
            container=deque,
            code=f'''
                while c_filled:
                    _ = c_filled.pop()
            ''',
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.READ_FIRST: Logic(
            container=deque,
            code=READ_FIRST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
            skip_empty=True,
        ),
        Action.READ_LAST: Logic(
            container=deque,
            code=READ_LAST_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.LAST_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_RANDOM: Logic(
            container=deque,
            code=READ_RAND_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.RANDOM_INDEX,
            ),
            skip_empty=True,
        ),
        Action.READ_CENTER: Logic(
            container=deque,
            code=READ_CENTER_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
                Prep.CENTER_INDEX,
            ),
            skip_empty=True,
        ),
        Action.COPY: Logic(
            container=deque,
            code=COPY_LOGIC,
            preparations=(
                Prep.INIT_FILLED,
            ),
        ),
        Action.DEEPCOPY: Logic(
            container=deque,
            code=DEEPCOPY_LOGIC,
            preparations=(
                Prep.INIT_NESTED_FILLED,
            ),
        ),
    },
}
