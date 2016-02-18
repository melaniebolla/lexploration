from __future__ import print_function

#import the Natural Language Toolkit
import nltk

#import WordNet, a lexical database for English
from nltk.corpus import wordnet

# get_keyword() asks for user input; expects one word.
# To-Do: write test to validate input -- need to catch input that doesn't correspond to a word in wordnet
def get_keyword():
	keyword = raw_input('Enter a keyword to find related words: ')
	return keyword

def get_synset(given_keyword):
	print('loading definitions...')
	keyword = given_keyword
	#get list of synset options
	synset_options = wordnet.synsets(keyword)
	question_for_user = 'Which sense of \''+keyword+'\' did you mean?\n'
	definition_counter = 0
	for synset in synset_options:
		definition_counter += 1
		question_for_user += str(definition_counter)+') ('+synset.pos+'.) '+synset.definition+'\n'
	question_for_user += '\nPlease input the number of the closest match:\n'
	# To-Do: write test to validate input -- need to make sure it's one of the numbers listed and nothing else
	answer = raw_input(question_for_user)
	correct_synset = synset_options[int(answer)-1]
	return correct_synset
			
def get_related_words(correct_synset):
	synset = correct_synset
	related_synsets = []
	related_synsets += synset.hyponyms()
	related_synsets += synset.hypernyms()
# Other ideas for related words:
# Hyponyms of hypernyms (sister terms?)
#	for s in synset.hypernyms():
#		related_synsets += s.hyponyms()
# Proper name hyponyms
#	related_synsets += synset.instance_hyponyms()
# Proper name hypernyms
#	related_synsets += synset.instance_hypernyms()
# Holonyms
#	related_synsets += synset.member_holonyms()
# Could add more relationships
	related_words = []
	for s in related_synsets:
		lemmas = s.lemmas
		for lem in lemmas:
			related_words.append(lem.name)
	return related_words

# To-Do: Allow user to save a list of related words in a "meaning cluster"

# Print related words for the user to look at
def print_related_words(word_list):
	print('\nRelated words: ')
	word_counter = 0
	need_more = None
	for w in word_list:
		word_counter += 1
		pretty_word = w
		pretty_word = pretty_word.replace('_', ' ')
		if word_counter <= 10:
			if word_counter == 10:
				print(pretty_word)
				need_more = raw_input("\nShowing first 10 matches. Show all "+str(len(word_list))+"? (y/n)\n")
			elif word_counter == len(word_list):
				print(pretty_word)
			else:
				print(pretty_word+',', end=' ')
		elif need_more == 'y':
			if word_counter == len(word_list):
				print(pretty_word)
			else:
				print(pretty_word+',', end=' ')		
# Start exploring related words!
def run_session():
	print("Welcome! Let's find the words you're looking for.\n")
	keyword = get_keyword()
	synset = get_synset(keyword)
	all_related_words = get_related_words(synset)
	print_related_words(all_related_words)
	done()

# Check if the user is done looking keywords up. If no, repeat search process. If yes, terminate.
def done():
	answer = raw_input('\nDone? (y/n):\n')
	valid_answer = False
	while valid_answer == False:
		if answer == 'y':
			valid_answer = True
			print("Bye!")
		elif answer == 'n':
			valid_answer = True
			run_session()
		else:
			answer = raw_input('You must answer \'y\' or \'n\':')
		
# Run the program until the user says they're done:
run_session()
