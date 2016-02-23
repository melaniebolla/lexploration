# Lex-ploration: lexical exploration
## Requirements
This program requires NLTK 3.0, NLTK data, and Python 2.7.
To download the NLTK, follow the instructions at [nltk.org/install.html](http://www.nltk.org/install.html). Then install the required data [here](http://www.nltk.org/data.html).
The specific data packages required are 'gutenberg' and 'wordnet'.

## Running Lexploration
Run Lexploration by running lexploration.py with Python 2.7. This program requires user input, which will be explained in the **About** section below.

## About
###Aim of this program:
The aim of this program is to facilitate the finding of relevant sentences on a specific topic by user-led semantic expansion of two or more keywords.
Right now the scope is limited to searching the novel 'Emma' by Jane Austen, but could be expanded to search over multiple Project Gutenberg books, or even other types of text.
The program uses the [WordNet](https://wordnet.princeton.edu/) NLTK package to expand keywords into lists of related words. These semantically related word lists are used as input to the search function, which outputs a text file of all sentences including those words.

###Motivation:
English essays rely on analysis of a few well chosen quotes or scenes for the work to ilustrate the essay writer's point.
Finding these important quotes and scenes in the work can be challenging, even if a searchable, online version of the text can be found.

For example, if you've decided to write a paper on the role of food in a novel, on your own you might come up with a list of words like "food", "drink", "meal", and "eating". This program allows the user to grow that list much larger in less time, because it provides a long list of words related in meaning to 'food', like 'petit four' and 'baked goods' and words like 'chomp' and 'savoring' for the word 'eating', which are not direct synonyms, but still closely related to the input words 'food' and 'eating'. It would be tedious for a person to search for lots of specific types of food, but it's easy for a computer.

###Advantage over a standard thesaurus:
One advantage of using this program to expand your search is that it tries to find words with meanings that are related to multiple words in your word list. After you've expanded at least two words into semantically-related word lists, the program combines those lists, then takes each pair of words and looks if they have any higher-level words in common that are similar to the word you started your search with.

Another advantage over using a thesaurus is that it automatically adds words that aren't just synonyms of the word you searched for, but instead are related in a variety of ways to your word. Possible relationships include hypernymy, hyponymy, holonymy, and meronymy. You can read more about these relationships [here](https://en.wikipedia.org/wiki/WordNet#Database_contents).

The search function of this program aggregates the search results for all words in a comma separated list, and only diplays each sentence of the book once, rather than returning the same quote every time for a different word if multiple words on your list happen to appear in the same sentence.
This means that you can search a book for hundreds of words in a short amount of time.

###Limitations:
Because semantic disambiguation is an unsolved problem in NLP and the point of this program is to expand searches rather than to refine them, this program does not try to distinguish different senses of a word in the text; instead, it returns all string-matched words (matching case and allowing for "title case", meaning the first letter of the word is capitalized). There are ways to improve the output, such as running a part-of-speech tagger over the words and only returning matches where the part-of-speech of the search term matches that of the target. This would eliminate spurious matches, but also introduces room for error, especially if the program is expanded to search over less-structured text.

###Room for improvement:
Allowing for user interaction with the word list would help identify words they're not interested in and allow them to refine their search if necessary.
Currently, the user can manually edit the text file output by the lexplore.py program, but they have to be careful to preserve the ", " between each word in order to make sure each word is correctly searched for in the search.py of the program.
The lexplore function could also be made more robust by adding verb- and adjective-specific semantic relationships to the keyword expansion function. Right now, best results are achieved by searching for nouns (which seem to be the most natural part of speech to search for as keywords).
