#!/usr/bin/python2.7
from __future__ import print_function
import os
#import the Natural Language Toolkit
import nltk
#import WordNet, a lexical database for English
from nltk.corpus import wordnet

word_list = []

def get_synset(given_keyword):
    """Return the correct synset for a word based on the user's choice of
    definition"""
    keyword = given_keyword.replace(' ', '_')
    synset_options = None
    if wordnet.synsets(keyword):
        synset_options = wordnet.synsets(keyword)
    if synset_options and len(synset_options) > 1:
        question_for_user = 'Which sense of \''+keyword+'\' did you mean?\n'
        definition_counter = 0
        for synset in synset_options:
            definition_counter += 1
            question_for_user += str(definition_counter)+') ('+synset.pos()+'.) '+synset.definition()+'\n'
        question_for_user += '\nPlease input the number of the closest match:\n'
        answer = raw_input(question_for_user)
        if answer[0] in [str(i) for i in range(10)] and int(answer) in range(1, len(synset_options)+1):
            correct_synset = synset_options[int(answer)-1]
            print("Added '"+keyword+"' sense "+answer+") to your list.\nSearching for related words to add to your word cluster...\n")
            word_list.extend(correct_synset.lemmas())
        else:
            correct_synset = None
            print("Sorry, you entered an incorrect number. Did not add word to list.")
    elif synset_options:
        correct_synset = synset_options[0]
        print("Added '"+keyword+"', "+correct_synset.definition()+", to your list.\nSearching for related words to add to your word cluster...\n")
        word_list.extend(correct_synset.lemmas())
    else:
        print("\nSorry, no definitions found for "+given_keyword)
        correct_synset = None
    return correct_synset

def just_orth():
    """Returns a list of strings from the saved lemma list"""
    wl = []
    for w in word_list:
        wl.append(str(w.name()).replace('_', ' '))
    return wl

def get_related_words():
    """Adds words to the word list that are related in different ways in WordNet
    ."""
    w = raw_input("\nAdd a word to your list:\t")
    synset = get_synset(w)
    if synset:
        related_synsets = []
    # Hypernyms
        hypernyms = synset.hypernyms()
        if hypernyms:
            print("- Added more general words like '"+hypernyms[0].lemmas()[0].name().replace('_', ' ')+"'.")
        related_synsets.append(hypernyms)
    # Hyponyms
        hyponyms = synset.hyponyms()
        related_synsets.append(hyponyms)
        if hyponyms:
            print("- Added more specific words like '"+hyponyms[0].lemmas()[0].name().replace('_', ' ')+"'.")
    # Hypo-hyponyms
        hypohyponyms = []
        for h in hyponyms:
            related_synsets.append(h.hyponyms())
            hypohyponyms.extend(h.hyponyms())
    # Hypo-hypo-hyponyms
        for hh in hypohyponyms:
            related_synsets.append(hh.hyponyms())
    # Holonyms
        holonyms = synset.member_holonyms()
        holonyms.extend(synset.substance_holonyms())
        holonyms.extend(synset.part_holonyms())
        related_synsets.append(holonyms)
        if holonyms:
            print("- Added words like '"+holonyms[0].lemmas()[0].name().replace('_', ' ')+"' that '"+w+"' is a component or member of.")
    # Meronyms
        meronyms = synset.member_meronyms()
        meronyms.extend(synset.substance_meronyms())
        meronyms.extend(synset.part_meronyms())
        related_synsets.append(meronyms)
        if meronyms:
            print("- Added words that are a part of '"+w+"' like '"+meronyms[0].lemmas()[0].name().replace('_', ' ')+"'.")

        related_words = []
        for l in related_synsets:
            for s in l:
                related_words.extend(s.lemmas())
        word_list.extend(related_words)
    else:
        get_related_words()

def view_list():
    """Prints the current word list from the lemma list."""
    print("\nYour Word List:")
    orth_list = just_orth()
    print(', '.join(orth_list))

def get_ch(lemma1, lemma2):
    """Returns the common hypernyms of two lemmas' synsets."""
    ch_lemmas = set()
    ch_synsets = lemma1.synset().common_hypernyms(lemma2.synset())
    lemmas = set()
    for synset in ch_synsets:
        lemmas.update(synset.lemmas())
    for lem in lemmas:
        ch_lemmas.add(lem)
    return ch_lemmas

def lexplore():
    """Adds common hypernyms of all pairs of synsets from the lemma list to the
    word list. Only adds the hypernyms that meet a certain similarity threshold.
    The threshold is based on the first word added to the word list.
    """
    print("\nAttempting to add other words that have something in common with two or more of your related words...\n")
    if len(word_list) > 1:
        ch_lemmas = set()
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                w1 = word_list[i]
                w2 = word_list[j]
                if w1.synset() != w2.synset():
                    ch_lemmas.update(get_ch(w1, w2))
        for hypernym in ch_lemmas:
            if hypernym not in word_list and (hypernym.synset()).path_similarity(word_list[0].synset()) > 0.3:
                word_list.append(hypernym)

def export_list():
    """Export the word list as a comma-separated string to a text file called
    'wordlist.txt'"""
    print("\nExporting list to file")
    f = open('wordlist.txt', 'w')
    text = ', '.join(just_orth())
    f.write(text)
    f.close()
    print("...done! The text file is located in "+os.getcwd()+" and is called 'wordlist.txt'")

def build_word_list():
    get_related_words()
    get_related_words()
    while len(word_list) < 15:
        get_related_words()

def welcome():
    """Print the welcome message."""
    print("  _                 _                 _   _             ")
    print(" | | _____  ___ __ | | ___  _ __ __ _| |_(_) ___  _ __  ")
    print(" | |/ _ \ \/ / '_ \| |/ _ \| '__/ _` | __| |/ _ \| '_ \ ")
    print(" | |  __/>  <| |_) | | (_) | | | (_| | |_| | (_) | | | |")
    print(" |_|\___/_/\_\ .__/|_|\___/|_|  \__,_|\__|_|\___/|_| |_|")
    print("             |_| --------- lexical exploration ---------")
    print("Welcome to Lex-ploration!\n\nLet's lex-plore! To get started, you'll be asked to add a word and confirm which definition of that word you're interested in.")
    print("To get better results, you'll be asked to add more words. After you gather enough words, you'll recieve a word cluster related to the topic you're interested in.")
    print("\nLet's add some words!")

welcome()
build_word_list()
lexplore()
view_list()
export_list()
