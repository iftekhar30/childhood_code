import os
from pathlib import Path
from most_frequent_word import most_frequent_word
from collections import Counter


source_dir = "/home/jannatulf/Documents/python code/"
files = os.listdir()


with open("/home/jannatulf/Downloads/summary.txt", 'w') as s:
    for fyle in files:
        if Path(fyle).suffix == ".txt":
            with open(fyle, 'r') as f:
                text = f.read()
                #counter = Counter(text)
                #counter.
                mfw = most_frequent_word(text, 3)
                line_count = len(text.splitlines())
                word_count = len(text.split()) 
                s.write(f"File Name: {fyle}\n")
                s.write(f"Most frequent words: {mfw}\n")
                s.write(f"Word Count: {word_count}\n")
                s.write(f"Line Count: {line_count}\n")
                s.write(str(text.split().count("game")))
                s.write("\n")
                




