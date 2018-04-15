import operator,time

if __name__ == "__main__":
	tab = "\t"
	lines = [line.strip() for line in open('wsj00-18.tag') if "\t" in line or "\n" in line]
	words = [lines[i].split(tab,1)[0].lower() for i in xrange(len(lines))]
	d_words = list(set(words))
	
	d = {}
	# get top 1000 most frequent words
	for word in words:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	topD = dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[:1])

	top_words = []
	for k,v in topD.iteritems():
		top_words.append(k)

	fd = {}
	t0 = time.time()
	len_d_words = len(d_words)
	#prevw = words[0]
	prevw = ''
	for i in range(0,len(words)-1):
		# need a try except block here
		word = words[i]
		nextw = words[i+1]
		if word in top_words:
			if word not in fd:
				fd[word] = []
				fd[word].append([])
				fd[word].append([])
				fd[word][0] = [0] * len_d_words
				fd[word][1] = [0] * len_d_words
				#print "here1"
			#print "here2"
			fd[word][0][d_words.index(prevw)] += 1
			#print "here"
			fd[word][1][d_words.index(nextw)] += 1
		prevw = word
	t1 = time.time()
	print("Time: {}".format(t1-t0))
	last_word = words[len(words)-1]
	if last_word in top_words:
		fd[word][0][d_words.index(prevw)] += 1
		fd[word][1][d_words.index('')] += 1

		#if word not in fd:
		#	fd[word] = []
		#	fd[word][0] = [0] * len_word_set
		#	fd[word][1] = [0] * len_word_set
		#	fd[word][0][word_set.index[prevw]] += 1
		#	fd[word][1][word_set.index[nextw]] += 1

	"""
	fd = {}
	for k,v in topD.iteritems():
		fd[k] = []
		#fd[k].append({})
		#fd[k].append({})
		fd[k].append(zd_1)
		fd[k].append(zd_2)

	
	prev = lines[0].split(tab,1)[0]
	#fd[prev][0][prev] = 0
	for i in range(1,len(lines) - 1):
		word = lines[i].split(tab,1)[0]
		next_word = lines[i+1].split(tab,1)[0]
		#fd[word][0][word] = 0 # prev
		#fd[word][1][word] = 0 # next
		#fd[word]
		if word in top_words:
			fd[word][0][prev] += 1
			fd[word][1][next_word] += 1
		prev = word
	"""
	"""
	# need to check for last word, since going to len(lines) - 1
	last_word = lines[len(lines)-1].split(tab,1)[0]
	if last_word in top_words:
		fd[last_word][0][prev] += 1
	"""



	#topD[k] = 0 # may not need this

	#zd = dict.fromkeys(d, 0)
	#for k,v in d.iteritems():
	#	d[k] = 0

	#print zd
	#zd_1 = zd
	#zd_2 = zd
	#del zd
	






