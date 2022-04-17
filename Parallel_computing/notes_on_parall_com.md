It should be noted that randomly split the dataset to be processed always makes the parrallel works in sequential. For sub-datasets in splitted result, some sub-datasets can be huge and require more memory, which results in a situation that all parrallel processes are competing for limited memory.

To avoid this, before starting the parrallel process, test the memory usage on the largest sub-dataset and can:
- collect (relatively) large dataset into a set, forget the parrallel processing and process this set one by one;
- start parrallel computing for the remain datasets.

**In Ubuntu system**, one can refer to https://stackoverflow.com/a/53475728
```python
from pathlib import Path
from resource import getpagesize

PAGESIZE = getpagesize()
PATH = Path('/proc/self/statm')


def get_resident_set_size() -> int:
    """Return the current resident set size in bytes."""
    # statm columns are: size resident shared text lib data dt
    statm = PATH.read_text()
    fields = statm.split()
    return int(fields[1]) * PAGESIZE


data = []
start_memory = get_resident_set_size()
for _ in range(10):
    data.append('X' * 100000)
    print(get_resident_set_size() - start_memory)
```
If used in pieces of codes, 
```python
start_memory = get_resident_set_size()
# put codes here
mem_used = get_resident_set_size() - start_memory
print('memory used: {} Mb'.format(round(mem_used/1024, 2)))
```

*another approach is suggested by https://stackoverflow.com/a/45679009 , based on [tracemalloc](https://docs.python.org/3/library/tracemalloc.html) in Python 3.4 onwards. Need further learning and confirmation.*
