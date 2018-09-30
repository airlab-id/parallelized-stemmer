#!/usr/bin/python3

from parallelized_stemmer import ParallelStemmer

def input_cmd():
    stemmer = ParallelStemmer()
    print(stemmer.content_len())

if __name__ == "__main__":
    input_cmd()