# Python Containers Comparison
 
About the measurements
- Each test case executed 10 000 times
- 3 test cases / scenario; 0, 1000, and 100 000 items in the container
- **Not** executed in a perfect sterile environment
  - This means that there could be (and are) variances in the results that do
  not reflect the real performance perfectly and therefore small differences 
  should be ignored. It is also possible that a larger differences could
  be incorrect, though less likely. That said, you are free to read the
  source code and to run the tests yourself if you don't trust the results
  or just want to verify. Do point out if you find mistakes though.
  - Due to this I'm intending to re-run the tests at some point in an 
  environment where nothing else is happening and hopefully with a larger
  item count.

# The tested code / test case

To keep this neat and clean, the tested code (setup + timed part) 
for each test case are in [TESTED_CODE.md](./TESTED_CODE.md)

# Full results

To keep this neat and clean, the full results table including
each test case is in [RESULTS.md](./RESULTS.md)

# Conclusions

TODO: To include relevant results to each section

## init
Initialising an empty collection and filling it after the fact is always
*much* slower than initialising the collection with the values.

#### 100 000  items
`list` and `tuple` are about the same with `deque` _possibly_ being
slightly slower (might be just the aforementioned non-sterile test environment).
`set` takes almost 4x as long as `list` and `dict` is by far the slowest taking
~17x as long as `list`.

#### 1000 items
The differences are, unsurprisingly, less pronounced than with larger 
number of items, though `dict` is by far the slowest taking over 4x as long as `list`.

## filling
There is not much difference in appending between `dict`, `list`, and `deque`.  
Adding to `set` is a bit slower than appending to the others.  
Prepending to a collection is *much* faster on `deque` than on `list`.  

## iteration
`list`, `tuple`, and `deque` are the winners here with `dict` and `set`
being about the same at ~50% slower than the others. 
It's worth noting however that iterating a `dict` will iterate the keys, 
but often you'd also be interested in the values and `dict` items iteration 
is by far the slowest as it takes almost twice the time it takes to iterate
`dict` keys.

## read
No big differences except `deque` is the fastest for reading last item and 
by far the slowest for reading from the middle. 

## consume

#### FIFO
Unsurprisingly, FIFO on `dict` is a horrible idea, 
though it's not exactly a good idea to use `list` either 
when `deque` beats both of them hands down.

#### LIFO
With LIFO the order is the same with `deque` beating `list` 
which in turn beats `dict`, but the differences are much smaller.

#### Unordered
Since `set` is unordered it can't support FIFO/LIFO, 
but if the order is not important it's a valid option as it's performance
is on level with `deque`.

## `in` check
`dict` _keys_ and `set` are by far the fastest, so if doing many `if` checks
or especially if that's the sole use case for the collection, 
go with `set` if you don't require key-value collection.

