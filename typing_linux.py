class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


getch = _GetchUnix()

import sys
import os
import random

def read_typing(string):
    print string
    l = len(string)
    i = 0
    while i < l:
        c = getch()
        if c == string[i]:
            i += 1
            sys.stdout.write('^')
            #sys.stdout.write(c)
        elif c == '`':
            break

def prompt_test():
    os.system('clear')
    print 'Enter to start, ` to exit'
    while True:
        s = getch()
        if s == '`':
            return False
        elif s == '\r':
            return True

def ask_for_char_set():
    os.system('clear')
    return raw_input('enter a string as char set\n\n>')

def get_all_words(checker):
    for file_name in sys.argv:
        f = open(file_name, "r")
        words = []
        for word in f:
            word = word.lstrip().rstrip()
            if checker(word):
                words.append(word)
        f.close()
    return words

def pick_words(char_set):
    # XXX:this should be called only once for every char_set
    words = get_all_words(lambda word: all((char in char_set) for char in word))
    if not words:
        return '`'

    picked_words = random.sample(words, 5)
    return ' '.join(picked_words)

def pick_words2(char_set):
    # XXX:this should be called only once for every char_set
    words = get_all_words(lambda word: any((char in word) for char in char_set))
    if not words:
        return '`'

    picked_words = random.sample(words, 5)
    return ' '.join(picked_words)

def generate_string(char_set):
    cnt_char = 0
    generated_words = []
    while cnt_char < 25:
        r = random.randint(1, 7)
        string = ''
        for i in range(r):
            c = char_set[random.randint(0, len(char_set)-1)]
            string += c

        generated_words.append(string)
        cnt_char += r

    return ' '.join(generated_words)

def practice_typing(gen_str_func):
    char_set = ask_for_char_set()
    while True:
        if not prompt_test():
            break
        os.system('clear')
        s = gen_str_func(char_set)
        read_typing(s)

if __name__ == '__main__':
    os.system('clear')
    random.seed()
    gen_str_funcs = [generate_string, pick_words, pick_words2]
    while True:
        os.system('clear')
        print 'enter ` to exit'
        print 'enter 0 to practice characters'
        print 'enter 1 to practice words (all chars are in set)'
        print 'enter 2 to practice words (contain at least on char in set)'

        c = getch()
        if c.isdigit():
            n = ord(c) - ord('0')
            if n < len(gen_str_funcs):
                practice_typing(gen_str_funcs[n])
        elif c == '`':
            break
