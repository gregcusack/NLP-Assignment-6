import operator, time, string
import numpy as np
from sklearn.preprocessing import normalize
from sklearn.cluster import KMeans
from itertools import groupby
from operator import itemgetter

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
	topD = dict(sorted(d.iteritems(), key=operator.itemgetter(1), reverse=True)[0:1000])

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
				fd[word] = np.zeros((2,len_d_words))
			fd[word][0][d_words.index(prevw)] += 1
			fd[word][1][d_words.index(nextw)] += 1
		prevw = word
	
	last_word = words[len(words)-1]
	if last_word in top_words:
		fd[word][0][d_words.index(prevw)] += 1
		fd[word][1][d_words.index('')] += 1
	
	t1 = time.time()
	print("Time1: {}".format(t1-t0))

	t0 = time.time()
	X = np.empty([0,len_d_words*2])
	index = 0
	for k,v in fd.iteritems():
		#print k
		fd[k] = normalize(fd[k], axis=1, norm='l1')
		v = np.concatenate((fd[k][0],fd[k][1]))
		X = np.append(X, np.array([v]), axis=0)
		#X[0][index]
		index += 1

	t1 = time.time()
	print("Time2: {}".format(t1-t0))

	kmeans = KMeans(n_clusters=25, random_state=0).fit(X)
	print(kmeans.labels_)

	a = zip(kmeans.labels_, fd)
	a = sorted(a, key=lambda x: x[0])
	b = [(k, list(list(zip(*g))[1])) for k, g in groupby(a, itemgetter(0))]
	print(b)


	"""
	>>> keys = ['a', 'b', 'c']
	>>> values = [1, 2, 3]
	>>> dictionary = dict(zip(keys, values))
	>>> print(dictionary)
	{'a': 1, 'b': 2, 'c': 3}
	"""




