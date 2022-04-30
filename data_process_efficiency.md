When your research has a lot to do with large-scale data, it is critical to make your data organized.

This [blog](https://towardsdatascience.com/csv-files-for-storage-no-thanks-theres-a-better-option-72c78a414d1d) introduced the column-based data format, Apache Parquet, and I also want to know what drawbacks are along with it. Borrow from [this answer](https://stackoverflow.com/a/36831549),
> Columnar is great when your input side is large, and your output is a filtered subset: from big to little is great. Not as beneficial when the input and outputs are about the same.

This may guides how to choose your data format. Since Parquet can also be read back as row-based data (`pandas.read_parquet()`), and it takes less disk space to store in Parquet so that you may consider using this format as a priority.

Read more

https://www.opendatablend.io/blog/querying-large-parquet-files-with-pandas
