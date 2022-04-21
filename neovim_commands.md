#### Comment and Uncomment
Referring to https://stackoverflow.com/a/23063140

**Comment with `#`**:
> 1. visually select the text rows (using V as usual)
> 2. :norm i#\<blank space>

*add a \<blank space> between `#` and the start of each line selected*

**Uncomment `#`**:
> 1. visually select the text as before (or type **gv** to re-select the previous selection)
> 2. :norm xx

*If haven't added a \<blank space>, using one 'x', i.e., ':norm x'*

#### Search and navigate
from https://linuxize.com/post/vim-search/
> Press `n` to find the next occurrence or `N` to find the previous occurrence.

> To search for a whole word, start the search by pressing `/` or `?`, type `\<` to mark the beginning of a word, enter the search pattern, type `\>` to mark the end of a word, and hit Enter to perform the search.

> For example, to search for “gnu” you would use `/\<gnu\>`
