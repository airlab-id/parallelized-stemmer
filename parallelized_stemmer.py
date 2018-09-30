#!/usr/bin/python3

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
from dask import delayed
import time

class ParallelStemmer():
    DELIMETERS = "\"", "\'", "{", "}", "(", ")", "[", "]", ">", "<", "_", "=", "+", "|", "\\", ":", ";", " ", ",", ".", "/", "?", "~", "!", "@", "#", "$", "%", "^", "&", "*", "\r", "\n", "\t", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    
    def __init__(self):
        self.list_of_sentences = open("./resources/dataset_teks.txt").readlines()

    def tokenizing(self, text):
        regexPattern = '|'.join(map(re.escape, self.DELIMETERS))
        texts = re.split(regexPattern, text.lower())
        return texts

    def content_len(self):
        return len(self.list_of_sentences)

    def stem(self):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        self.execute_stem(stemmer, self.list_of_sentences, 0, self.content_len())
        
    def parallel_stem(self, total_process):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        
        d = int(self.content_len()/total_process)

        for i in range(total_process - 1):
            self.parallelized_execute_stem(stemmer, self.list_of_sentences, int(i * d), int((i+1) * d))

        self.parallelized_execute_stem(stemmer, self.list_of_sentences, int(d * (total_process - 1)), self.content_len)

    def execute_stem(self, stemmer, list_of_sentences, start, end):
        start_time = time.time()

        index = int(start)
        end_index = int(end)

        for i in range(index, end_index):
            words = self.tokenizing(list_of_sentences[i])
            for word in words:
                if word:
                    print(i, stemmer.stem(word))
        end_time = time.time()
        print("elapsed time in seconds", end_time - start_time)

    @delayed
    def parallelized_execute_stem(self, stemmer, list_of_sentences, start, end):
        start_time = time.time()

        index = int(start)
        end_index = int(end)

        for i in range(index, end_index):
            words = self.tokenizing(list_of_sentences[i])
            for word in words:
                if word:
                    print(i, stemmer.stem(word))
        end_time = time.time()
        print("elapsed time in seconds", end_time - start_time)

