dict - init (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]

# timed code
dict(items)
```

dict - init (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]

# timed code
dict(items)
```

dict - init (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]

# timed code
dict(items)
```

dict - init empty and fill (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]

# timed code
c = dict()
for k, v in items:
    c[k] = v
```

dict - init empty and fill (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]

# timed code
c = dict()
for k, v in items:
    c[k] = v
```

dict - iterate (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
for _ in c_filled:
    pass
```

dict - iterate (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
for _ in c_filled:
    pass
```

dict - iterate dict items (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
d_items = c_filled.items()

# timed code
for _, _ in d_items:
    pass
```

dict - iterate dict items (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
d_items = c_filled.items()

# timed code
for _, _ in d_items:
    pass
```

dict - add right (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)

# timed code
c_filled["foo"] = "foo"
```

dict - add right (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
c_filled["foo"] = "foo"
```

dict - add right (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
c_filled["foo"] = "foo"
```

dict - read first (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
c_filled[0]
```

dict - read first (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
c_filled[0]
```

dict - read last (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
i_last = len(range(1000)) - 1 if dict is dict else -1

# timed code
c_filled[i_last]
```

dict - read last (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
i_last = len(range(100000)) - 1 if dict is dict else -1

# timed code
c_filled[i_last]
```

dict - read random (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
i_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
c_filled[i_rand]
```

dict - read random (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
i_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
c_filled[i_rand]
```

dict - read center (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
i_center = int(len(range(1000)) / 2)

# timed code
c_filled[i_center]
```

dict - read center (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
i_center = int(len(range(100000)) / 2)

# timed code
c_filled[i_center]
```

dict - in (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)
i_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
i_rand in c_filled
```

dict - in (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
i_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
i_rand in c_filled
```

dict - in (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
i_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
i_rand in c_filled
```

dict - in dict values (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)
d_values = c_filled.values()
v_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
v_rand in d_values
```

dict - in dict values (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)
d_values = c_filled.values()
v_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
v_rand in d_values
```

dict - in dict values (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)
d_values = c_filled.values()
v_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
v_rand in d_values
```

dict - len (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)

# timed code
len(c_filled)
```

dict - len (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
len(c_filled)
```

dict - len (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
len(c_filled)
```

dict - consume FIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.pop(next(iter(c_filled)))
```

dict - consume FIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.pop(next(iter(c_filled)))
```

dict - consume FIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.pop(next(iter(c_filled)))
```

dict - consume LIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.popitem()
```

dict - consume LIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.popitem()
```

dict - consume LIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
while c_filled:
    _ = c_filled.popitem()
```

dict - copy (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]
c_filled = dict(items)

# timed code
copy.copy(c_filled)
```

dict - copy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]
c_filled = dict(items)

# timed code
copy.copy(c_filled)
```

dict - copy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]
c_filled = dict(items)

# timed code
copy.copy(c_filled)
```

dict - deepcopy (0)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(0)]

if dict is dict:
    c_nested_filled = dict((i, dict(items)) for i in range(100))
else:
    c_nested_filled = dict(dict(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

dict - deepcopy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(1000)]

if dict is dict:
    c_nested_filled = dict((i, dict(items)) for i in range(100))
else:
    c_nested_filled = dict(dict(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

dict - deepcopy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = [(x, x) for x in range(100000)]

if dict is dict:
    c_nested_filled = dict((i, dict(items)) for i in range(100))
else:
    c_nested_filled = dict(dict(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

list - init (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

# timed code
list(items)
```

list - init (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
list(items)
```

list - init (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
list(items)
```

list - init empty and fill (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
c = list()
for i in items:
    c.append(i)
```

list - init empty and fill (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
c = list()
for i in items:
    c.append(i)
```

list - iterate (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
for _ in c_filled:
    pass
```

list - iterate (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
for _ in c_filled:
    pass
```

list - add right (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
c_filled.append("foo")
```

list - add right (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
c_filled.append("foo")
```

list - add right (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
c_filled.append("foo")
```

list - add left (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
c_filled.insert(0, "foo")
```

list - add left (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
c_filled.insert(0, "foo")
```

list - add left (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
c_filled.insert(0, "foo")
```

list - read first (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
c_filled[0]
```

list - read first (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
c_filled[0]
```

list - read last (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)
i_last = len(range(1000)) - 1 if list is dict else -1

# timed code
c_filled[i_last]
```

list - read last (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)
i_last = len(range(100000)) - 1 if list is dict else -1

# timed code
c_filled[i_last]
```

list - read random (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)
i_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
c_filled[i_rand]
```

list - read random (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)
i_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
c_filled[i_rand]
```

list - read center (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)
i_center = int(len(range(1000)) / 2)

# timed code
c_filled[i_center]
```

list - read center (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)
i_center = int(len(range(100000)) / 2)

# timed code
c_filled[i_center]
```

list - in (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)
v_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
v_rand in c_filled
```

list - in (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)
v_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
v_rand in c_filled
```

list - in (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)
v_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
v_rand in c_filled
```

list - len (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
len(c_filled)
```

list - len (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
len(c_filled)
```

list - len (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
len(c_filled)
```

list - consume FIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop(0)
```

list - consume FIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop(0)
```

list - consume FIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop(0)
```

list - consume LIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

list - consume LIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

list - consume LIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

list - copy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = list(items)

# timed code
copy.copy(c_filled)
```

list - copy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = list(items)

# timed code
copy.copy(c_filled)
```

list - copy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = list(items)

# timed code
copy.copy(c_filled)
```

list - deepcopy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

if list is dict:
    c_nested_filled = list((i, list(items)) for i in range(100))
else:
    c_nested_filled = list(list(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

list - deepcopy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

if list is dict:
    c_nested_filled = list((i, list(items)) for i in range(100))
else:
    c_nested_filled = list(list(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

list - deepcopy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

if list is dict:
    c_nested_filled = list((i, list(items)) for i in range(100))
else:
    c_nested_filled = list(list(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

set - init (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

# timed code
set(items)
```

set - init (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
set(items)
```

set - init (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
set(items)
```

set - init empty and fill (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
c = set()
for i in items:
    c.add(i)
```

set - init empty and fill (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
c = set()
for i in items:
    c.add(i)
```

set - iterate (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)

# timed code
for _ in c_filled:
    pass
```

set - iterate (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)

# timed code
for _ in c_filled:
    pass
```

set - add unordered (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = set(items)

# timed code
c_filled.add("foo")
```

set - add unordered (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)

# timed code
c_filled.add("foo")
```

set - add unordered (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)

# timed code
c_filled.add("foo")
```

set - in (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = set(items)
v_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
v_rand in c_filled
```

set - in (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)
v_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
v_rand in c_filled
```

set - in (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)
v_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
v_rand in c_filled
```

set - len (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = set(items)

# timed code
len(c_filled)
```

set - len (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)

# timed code
len(c_filled)
```

set - len (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)

# timed code
len(c_filled)
```

set - consume random order (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = set(items)

# timed code
while c_filled:
    c_filled.pop()
```

set - consume random order (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)

# timed code
while c_filled:
    c_filled.pop()
```

set - consume random order (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)

# timed code
while c_filled:
    c_filled.pop()
```

set - copy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = set(items)

# timed code
copy.copy(c_filled)
```

set - copy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = set(items)

# timed code
copy.copy(c_filled)
```

set - copy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = set(items)

# timed code
copy.copy(c_filled)
```

tuple - init (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

# timed code
tuple(items)
```

tuple - init (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
tuple(items)
```

tuple - init (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
tuple(items)
```

tuple - init empty and fill (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
c = tuple()
for i in items:
    c = c + (i,)
```

tuple - init empty and fill (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
c = tuple()
for i in items:
    c = c + (i,)
```

tuple - iterate (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
for _ in c_filled:
    pass
```

tuple - iterate (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
for _ in c_filled:
    pass
```

tuple - in (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = tuple(items)
v_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
v_rand in c_filled
```

tuple - in (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)
v_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
v_rand in c_filled
```

tuple - in (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)
v_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
v_rand in c_filled
```

tuple - len (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = tuple(items)

# timed code
len(c_filled)
```

tuple - len (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
len(c_filled)
```

tuple - len (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
len(c_filled)
```

tuple - consume FIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[0]
    c_filled = c_filled[1:]
```

tuple - consume FIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[0]
    c_filled = c_filled[1:]
```

tuple - consume FIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[0]
    c_filled = c_filled[1:]
```

tuple - consume LIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[-1]
    c_filled = c_filled[:-1]
```

tuple - consume LIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[-1]
    c_filled = c_filled[:-1]
```

tuple - consume LIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
while c_filled:
    _ = c_filled[-1]
    c_filled = c_filled[:-1]
```

tuple - read first (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
c_filled[0]
```

tuple - read first (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
c_filled[0]
```

tuple - read last (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)
i_last = len(range(1000)) - 1 if tuple is dict else -1

# timed code
c_filled[i_last]
```

tuple - read last (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)
i_last = len(range(100000)) - 1 if tuple is dict else -1

# timed code
c_filled[i_last]
```

tuple - read random (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)
i_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
c_filled[i_rand]
```

tuple - read random (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)
i_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
c_filled[i_rand]
```

tuple - read center (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)
i_center = int(len(range(1000)) / 2)

# timed code
c_filled[i_center]
```

tuple - read center (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)
i_center = int(len(range(100000)) / 2)

# timed code
c_filled[i_center]
```

tuple - copy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = tuple(items)

# timed code
copy.copy(c_filled)
```

tuple - copy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = tuple(items)

# timed code
copy.copy(c_filled)
```

tuple - copy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = tuple(items)

# timed code
copy.copy(c_filled)
```

tuple - deepcopy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

if tuple is dict:
    c_nested_filled = tuple((i, tuple(items)) for i in range(100))
else:
    c_nested_filled = tuple(tuple(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

tuple - deepcopy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

if tuple is dict:
    c_nested_filled = tuple((i, tuple(items)) for i in range(100))
else:
    c_nested_filled = tuple(tuple(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

tuple - deepcopy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

if tuple is dict:
    c_nested_filled = tuple((i, tuple(items)) for i in range(100))
else:
    c_nested_filled = tuple(tuple(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

deque - init (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

# timed code
deque(items)
```

deque - init (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
deque(items)
```

deque - init (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
deque(items)
```

deque - init empty and fill (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

# timed code
c = deque()
for i in items:
    c.append(i)
```

deque - init empty and fill (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

# timed code
c = deque()
for i in items:
    c.append(i)
```

deque - iterate (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
for _ in c_filled:
    pass
```

deque - iterate (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
for _ in c_filled:
    pass
```

deque - add right (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
c_filled.append("foo")
```

deque - add right (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
c_filled.append("foo")
```

deque - add right (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
c_filled.append("foo")
```

deque - add left (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
c_filled.appendleft("foo")
```

deque - add left (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
c_filled.appendleft("foo")
```

deque - add left (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
c_filled.appendleft("foo")
```

deque - in (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)
v_rand = random.choice(range(0)) if range(0) else "foo"

# timed code
v_rand in c_filled
```

deque - in (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)
v_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
v_rand in c_filled
```

deque - in (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)
v_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
v_rand in c_filled
```

deque - len (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
len(c_filled)
```

deque - len (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
len(c_filled)
```

deque - len (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
len(c_filled)
```

deque - consume FIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.popleft()
```

deque - consume FIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.popleft()
```

deque - consume FIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.popleft()
```

deque - consume LIFO (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

deque - consume LIFO (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

deque - consume LIFO (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
while c_filled:
    _ = c_filled.pop()
```

deque - read first (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
c_filled[0]
```

deque - read first (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
c_filled[0]
```

deque - read last (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)
i_last = len(range(1000)) - 1 if deque is dict else -1

# timed code
c_filled[i_last]
```

deque - read last (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)
i_last = len(range(100000)) - 1 if deque is dict else -1

# timed code
c_filled[i_last]
```

deque - read random (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)
i_rand = random.choice(range(1000)) if range(1000) else "foo"

# timed code
c_filled[i_rand]
```

deque - read random (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)
i_rand = random.choice(range(100000)) if range(100000) else "foo"

# timed code
c_filled[i_rand]
```

deque - read center (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)
i_center = int(len(range(1000)) / 2)

# timed code
c_filled[i_center]
```

deque - read center (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)
i_center = int(len(range(100000)) / 2)

# timed code
c_filled[i_center]
```

deque - copy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))
c_filled = deque(items)

# timed code
copy.copy(c_filled)
```

deque - copy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))
c_filled = deque(items)

# timed code
copy.copy(c_filled)
```

deque - copy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))
c_filled = deque(items)

# timed code
copy.copy(c_filled)
```

deque - deepcopy (0)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(0))

if deque is dict:
    c_nested_filled = deque((i, deque(items)) for i in range(100))
else:
    c_nested_filled = deque(deque(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

deque - deepcopy (1000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(1000))

if deque is dict:
    c_nested_filled = deque((i, deque(items)) for i in range(100))
else:
    c_nested_filled = deque(deque(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```

deque - deepcopy (100000)
```python
# setup code
import copy
import random
from collections import deque
items = list(range(100000))

if deque is dict:
    c_nested_filled = deque((i, deque(items)) for i in range(100))
else:
    c_nested_filled = deque(deque(items) for _ in range(100))


# timed code
copy.deepcopy(c_nested_filled)
```