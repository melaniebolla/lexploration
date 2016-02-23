#!/usr/bin/python2.7
from __future__ import division
#Imprt the Gutenberg corpus from NLTK
from nltk.corpus import gutenberg
import os
import time

sentence_total = len(gutenberg.sents('austen-emma.txt'))

def get_word_list():
    """Reads in the wordlist file and returns the words as a list."""
    print("Searching book for quotes")
    words = []
    f = open('wordlist.txt', 'r')
    for line in f:
        words.extend(line.split(', '))
    return words

def get_book_sents(word_list):
    """Searches Jane Austen's 'Emma' for the words in the word list.
    The sentences are modified to highlight the found words by changing them to uppercase.
    Then the sentence number (in order from the book) is appended to the front
    of the sentence string.
    Returns a list of strings (sentence # + \s + sentence string).
    """
    book = 'austen-emma.txt'
    book_sents = gutenberg.sents(book)
    sent_nums = set()
    sents_to_return = []
    s_count = 0
    for s in book_sents:
        s_count += 1
        s_str = " ".join(s)
        for w in word_list:
            if ' '+w+' ' in s_str.lower():
                if s_count not in sent_nums:
                    sent_nums.add(s_count)
                    s_str = s_str.replace(' '+w+' ', ' '+w.upper()+' ')
                    s_str = s_str.replace(' '+w.title()+' ', ' '+w.upper()+' ')
                    sents_to_return.append(str(s_count)+' '+s_str)
                else:
                    s_str = s_str.replace(' '+w+' ', ' '+w.upper()+' ')
                    s_str = s_str.replace(' '+w.title()+' ', ' '+w.upper()+' ')
                    sents_to_return[-1] = str(s_count)+' '+s_str
    return sents_to_return

def get_quotes(sent_list):
    """Returns the quotes that match any of the words from the word list as a
    concatenated string in order of appearance in the book. Uses the sentence number to
    add the percentage through the book (as a rough estimate of where to look for the
    quote using a hard copy). """
    sents = sent_list
    quotes = ''
    if sents:
        counter = 0
        for s in sents:
            counter += 1
            s_count, sentence = s.split(' ', 1)
            quote = "\n"+str(counter)+". ("+str(int(round((float(s_count)/sentence_total)*100)))+"%) "+sentence
            quotes += quote
        print(str(counter)+' quotes found!')
        return quotes
    else:
        print("No sentences found! Try again.")
        return None

def export_quotes(quotes):
    """Export string of quotes to a text file called 'quotelist.txt'"""
    if quotes:
        filename = "quotelist.txt"
        f = open(filename, 'w')
        q = quotes
        f.write('Quotes with approximate % through book. Words related to your topic appear in UPPERCASE.\n')
        f.write(q)
        f.close()
        os.startfile(os.getcwd()+"\\"+filename)
        print("\nExporting list to file")
        print("Opening 'quotelist.txt'. You can find 'quotelist.txt' in "+str(os.getcwd()))

def welcome():
    print("We're going to search Jane Austen's 'Emma' to find quotes that have words potentially related to your word cluster.")
    print("There might be sentences that don't seem related. This tool helps expand your search; it doesn't refine your search.")

welcome()
word_list = get_word_list()
sents = get_book_sents(word_list)
quotes = get_quotes(sents)
time.sleep(5)
export_quotes(quotes)
