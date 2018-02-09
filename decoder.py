from __future__ import division

def decode_text(INPUT, WINDOW):
	
	sentence_list = []
	ommitted_words = []
	entity_list = {}
	value_list = {}
	line_info = 0
	with open('terminal.txt','r') as f:
		for line in f.read().splitlines():
			if line == '#':
				line_info += 1
				continue
			elif line == '':
				continue
			else:
				if line_info == 0:
					ommitted_words.append(line)
				elif line_info == 1:
					couple = line.split(':')
					entity_list[couple[0]]=couple[1]
				elif line_info == 2:
					couple = line.split(':')
					value_list[couple[0]]=float(couple[1])
				elif line_info == 3:
					sentence_list.append(line)
				else:
					break
				
	
	tags_list = []
	sentence_value = {}
	for sentence in sentence_list:
		tags_sentence = []
		for word in sentence.split(' '):
			 if not word in ommitted_words:
				 tags_sentence.append(word)
		tags_list.append(tags_sentence)

	
	userInput = INPUT
	
	for entity in entity_list.keys():
		userInput = userInput.replace(entity,entity_list[entity])
	
	WINDOW.addstr("\nModified user input: {}".format(userInput))

	
	words_list = {}
	for line_list in tags_list:
	    for word in line_list:
	        if not(word in words_list.keys()):
	            words_list[word] = 0
	
	
	for word in userInput.split(' '):
	    WINDOW.addstr("\n"+ word)
	    if word in words_list.keys():
	        for entry in tags_list:
	            if word in entry:
	                for associate in entry:
	                    if not(associate == word):
							#Evaluate importance of keyword
							if associate in value_list.keys():
								words_list[associate] += value_list[associate]
							else:
								words_list[associate] += 1
	
	#words_ranking = sorted(words_list.items(), key=lambda x : x[1], reverse=True)
	list_values = {}
	count = 0
	for line in tags_list:
		lineLength = len(line)
		lineValue = 0
		lineValueSquared = 0
		for word in line:
			lineValue += words_list[word]
			lineValueSquared += words_list[word]*words_list[word]
		variance = lineValueSquared/lineLength - (lineValue/lineLength)*(lineValue/lineLength)
		weight = lineValue/(0.5+variance)
		list_values[sentence_list[count]] = weight
		count += 1
		#print(" %" + "Length : {} , lineValue : {} , lineValueSquared : {},  Variance : {}".format(lineLength, lineValue, lineValueSquared, lineValueSquared/lineLength - (lineValue/lineLength)*(lineValue/lineLength)))
	list_values  = sorted(list_values.items(), key=lambda x: x[1], reverse=True)
	
	return list_values[0][0]
	
