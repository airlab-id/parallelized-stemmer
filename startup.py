#!/usr/bin/python3

from parallelized_stemmer import ParallelStemmer

def main():
    stemmer = ParallelStemmer()
    stemmer.parallel_stem(3)

if __name__ == "__main__":
    main()