Rename column names after using pandas `groupby()`, from https://pbpython.com/groupby-agg.html
```python
multi_df = df.groupby(['embark_town', 'class'],
                    as_index=False).agg({'fare': ['sum', 'mean']})

multi_df.columns = [
'_'.join(col).rstrip('_') for col in multi_df.columns.values
]
```
