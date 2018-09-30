#!/usr/bin/python3

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

class ParallelStemmer():
    def __init__(self):
        self.list_of_sentences = open("./resources/dataset_teks.txt").readlines()

    def content_len(self):
        return len(self.list_of_sentences)

    def stem(self, sentence):
        # create stemmer
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        # stemming process
        return stemmer.stem(sentence)