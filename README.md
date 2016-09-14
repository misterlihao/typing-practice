# typing-practice

A typing practice tool in CLI.  
Written in Python.

## Usage

First, extract words from articles:

```sh
$ bash extract_words_in_files.sh ARTICLE.txt [ARTICLE.txt ...] > WORDS.txt
```

Then run the Python script whenever you want:

```sh
$ python typing_linux.py WORDS.txt [WORDS.txt ...]
```
