If you have thousands of millions of files under a single directory, show *n* files:
```bash
ls -U | head -10
```
from https://askubuntu.com/a/815736

---
Using `cd` to go up multiple directory levels, from https://superuser.com/a/449705
```bash
# go up two levels
cd ../..
# go up three levels
cd ../../..
```

---
Count the number of files in a directory, from https://askubuntu.com/a/405875
```bash
$ tree share/some/directory/ | tail -1
558 directories, 853 files

$ tree -L 2 share/some/directory/ | tail -1
120 directories, 3 files
```

Check the size of a directory, from https://askubuntu.com/a/1226
```bash
du -hs /path/to/directory
```

Check disk usages, 
```bash
df -BM
// df -BG
```
*`df -BM` shows with unit as "MB", `df -BG` for "GB"*

Use `xdg-open` to open files within terminal

`ls -lh <path> [| head -10]` shows 10 files with their properties, `h` means the human readable mode
