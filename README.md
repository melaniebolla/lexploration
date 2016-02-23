# Lex-ploration: lexical exploration
## Requirements
This program requires NLTK 3.0, NLTK data, and Python 2.7.
To download the NLTK go to [nltk.org](http://www.nltk.org/install.html). Then install the required data [here](http://www.nltk.org/data.html).
The specific packages required are 'gutenberg' and 'wordnet'.
## Running Lexploration
Run Lexploration by running lexploration.py with Python 2.7. This program requires user input, which will be explained in the **About** section below.

## About
###Aim of this program:
The aim of this program is to facilitate the finding of relevant quotes on a specific topic.
Right now the scope is limited to searching the novel 'Emma' by Jane Austen.
The program uses WordNet, "a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. Synsets are interlinked by means of conceptual-semantic and lexical relations."

###Motivation:
English essays rely on analysis of a few well chosen quotes or scenes for the work to ilustrate the essay writer's point.
Finding these important quotes and scenes in the work can be challenging, even if a searchable, online version can be found.
For example, if you've decided to write a paper on the role of food in a novel, on your own you might come up with a list of words like "food", "drink", "meal", and "eating". This program provides a long list of words like "petit four" and "baked goods" when you input "food" and words like "chomp" and "savoring" when you input "eating", which are not direct synonyms, but still closely related to the input words "food" and "baking". It would be tedious for a person to search for lots of specific types of food, but it's easy for a computer.

###Advantage over a standard thesaurus:
The advantage of using this program to expand your search is that it tries to find words with meanings that are related to multiple words in your word list. Another advantage is that it automatically adds words you might not think would help your search, but can.
The search function of this program aggregates the search results for all words in a comma separated list, and only diplays each sentence of the book once, rather than returning the same quote every time for a different word if multiple words on your list happen to appear in the same sentence.
This means that you can search a book for hundreds of words in a short amount of time.

###Example of usage:

###How this program could be expanded to other domains:
Lexploration can be used whenever you need a long list of related words.

###Limitations:
Because semantic disambiguation is an unsolved problem in NLP and the point of this program is to expand searches rather than to refine them, this program does not try to distinguish different senses of a word in the text, but instead returns all string-matched words (matching case and allowing for "title case", meaning the first letter of the word is capitalized).

###Room for improvement:
Allowing for user interaction with the word list would help identify words they're not interested in.
The user can manually edit the text file output by the lexplore program, but they have to be careful to preserve the ", " between each word in order to make sure each word is correctly searched for in the search section of the program.
