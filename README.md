# Typing-practice

A typing practice tool in CLI.  
Written in Python2.

## Build up word database from text files:

```sh
$ bash extract_words_in_files.sh ARTICLE.txt [ARTICLE.txt ...] > WORDS.txt
```
This process only need to do once, unles you want to change the word database.

## Play with the main program:

```sh
$ python typing_linux.py WORDS.txt [WORDS.txt ...]
```

### Pick practice mode

Now there are three of them:

- play with the randomly chosen characters.
- pick words that contains only characters you specify.
- pick words that contain at least one character belongs to characters you specify.

### Press ``` ` ``` to go back

Press ``` ` ``` key at any time you want to go back or leave.  
(except the moment you input character set... because of some implementation issues)
