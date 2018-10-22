---
title:
  Improved demo on testing functions
author:
  Jiahao Cai
date:
  Oct, 8, 2018
---


## 0. Some modifications

I have edited the `LOG` macro in the annotated C source file, add delimiter to the log format:

```c
static FILE *log_file;
static const char log_dir[] = "./temp/";
static char path[100] = "./temp/";
static char delimiter[] = "$$";
#define LOG(msg) \
    do {\
        strcat(path, __func__);\
        strcat(path, delimiter);\
        strcat(path, msg);\
        strcat(path, delimiter);\
        log_file = fopen(path, "w");\
        memset(path + sizeof(log_dir) - 1, 0, sizeof(path) - sizeof(log_dir));\
        fclose(log_file);\
    } while(0)
```

Now each log entry is like, which can be easily splitted:

```c
open("./temp/parse_string$$=='\"'$$", O_WRONLY|O_CREAT|O_TRUNC, 0666) = 3
```

The signature of `{"normal": "whatever"}` will be:

```c
*******
=='{'
!='}'
=='\"'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
=='\"'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
==':'
=='\"'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
!='\"'
!='\\'
=='\"'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
!='\\'
!=','
=='}'
*******
```
