It should be noted that randomly split the dataset to be processed always makes the parrallel works in sequential. For sub-datasets in splitted result, some sub-datasets can be huge and require more memory, which results in a situation that all parrallel processes are competing for limited memory.

To avoid this, before starting the parrallel process, test the memory usage on the largest sub-dataset and can:
- collect (relatively) large dataset into a set, forget the parrallel processing and process this set one by one;
- start parrallel computing for the remain datasets.
