import operator, time, string
import numpy as np

if __name__ == "__main__":
	tab = "\t"
	lines = [line.strip() for line in open('wsj00-18.tag') if "\t" in line or "\n" in line]
	words = [lines[i].split(tab,1)[0].lower() for i in xrange(len(lines))]
	#words = [''.join(c for c in s if c not in string.punctuation) for s in words]
	#words = [s for s in words if s]
	d_words = list(set(words))
	
	d = {}
	# get top 1000 most frequent words
	for word in words:
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	topD = dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[900:950])

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
	
	last_word = words[len(words)-1]
	if last_word in top_words:
		fd[word][0][d_words.index(prevw)] += 1
		fd[word][1][d_words.index('')] += 1
	t1 = time.time()
	print("Time: {}".format(t1-t0))

	"""
	for k,v in fd.iteritems():
		fd[k][0] = [float(i)/sum(fd[k][0]) for i in fd[k][0]]
		fd[k][1] = [float(i)/sum(fd[k][1]) for i in fd[k][1]]
	"""

	"""
	fd = {}
	t0 = time.time()
	len_d_words = len(d_words)
	#enum_list = enumerate(words)
	for word in top_words:
		indices = []
		for i in xrange(words):
			if words[i] == word:
				indices.append(i)
		#indices = [i for i, x in enum_list if x == word]
		for k in indices:
			prevw = words[k - 1]
			nextw = words[k + 1]
			if word not in fd:
				fd[word] = []
				fd[word].append([])
				fd[word].append([])
				fd[word][0] = [0] * len_d_words
				fd[word][1] = [0] * len_d_words
			fd[word][0][d_words.index(prevw)] += 1
			fd[word][1][d_words.index(nextw)] += 1
	t1 = time.time()
	print("Time: {}".format(t1-t0))
	#for k,v in fd.iteritems():
	"""






