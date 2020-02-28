import sys
from Levenshtein import *
from collections import deque
# get dictionary file from cmd
dictionary_file = sys.argv[1]
# get start word from cmd
sw = sys.argv[2]
# get target word from cmd
tw = sys.argv[3]
# max system's value
MAX_INT = sys.maxsize

# calculate levenshtein distance
def levenshtein(wd, nw):
	return distance(wd, nw)

# read dictionary file
def initialize():
	dic = []
	with open(dictionary_file, 'r') as dictionary:
		for line in dictionary:
			dic.append((line.strip('\n')))
	return dic

# store words to dic
dic = initialize()

"""" Tree Insertion Functions """

def is_empty(bk):
	if len(bk) == 0:
		return True
	else:
		return False

def set_root(bk, w):
	bk[w] = {}

def get_root(bk):
	for b in bk.keys():
		return b

def get_word(n):
	return str(n)

def get_child(bk, n, dist):
	for k,v in get_children(bk,n).items():
		if v == dist:
			return k

def get_children(bk, n):
	return bk.get(n)

def get_branch_label(bk, n, c):
	for k in get_children(bk,n).keys():
		if k == c:
			return get_children(bk,n)[k]

def add_child(bk, p, dist, w):
	bk[p][w] = dist

# function to insert a word in the
# bk-tree, creating the proper structure
def bk_tree_insert(bk, word):
	if is_empty(bk):
		set_root(bk, word)
		return
	node = get_root(bk)
	while node != None:
		node_word = get_word(node)
		distance = levenshtein(word, node_word)
		parent = node
		node = get_child(bk, node, distance)
		if node == None:
			add_child(bk, parent, distance, word)

# create the bk-tree
def bk_tree():
	bk = {}
	for d in dic:
		bk[d] = {}
		bk_tree_insert(bk,d)
	return bk

# store the bk data structure
bk = bk_tree()

""" Tree Search Functions """

def create_set():
	return set()

def create_queue():
	return deque()

def enqueue(pq, c):
	pq.append(c)

def is_queue_empty(pq):
	if len(pq) == 0:
		return True
	else:
		return False

def add_to_set(set, dist, n):
	set.add((dist, n))

# function to search for all the words,
# lying in a specific radius at the bk-tree
def bk_tree_search(bk, word, r):
	results = create_set()
	to_check = create_queue()
	enqueue(to_check, get_root(bk))
	while not is_queue_empty(to_check):
		node = to_check.pop()
		node_word = get_word(node)
		distance = levenshtein(word, node_word)
		if distance <= r:
			add_to_set(results, distance, node_word)
		l = distance - r
		h = distance + r
		children = get_children(bk, node)
		for child in children:
			d = get_branch_label(bk, node, child)
			if l <= d <= h:
				enqueue(to_check, child)
	return results

# function using dijkstra's structure, but a
# star's criteria in order to form correctly the 
# predecessor and weight-distance of each node 
def a_star(g, s):
	nodes = g.keys()
	dist = [ MAX_INT for v in nodes ]
	dist[list(nodes).index(s)] = 0
	pred = [ -1 for v in nodes ]
	pq = dist[:]
	chosen_word = str(sw)
	while chosen_word != str(tw):
		u = pq.index(min(pq))
		pq[u] = MAX_INT
		chosen_word = list(nodes)[u]
		for (w, v) in bk_tree_search(g, list(nodes)[u], 1):
			temp_v = list(nodes).index(v)
			if dist[u] != MAX_INT and dist[temp_v] > dist[u] + levenshtein(v,tw):
				dist[temp_v] = dist[u] + levenshtein(v,tw)
				pred[temp_v] = u
				pq[temp_v] = dist[temp_v]
	return (pred, dist)

# store predecessors and distance
pred, dist = a_star(bk, sw)

# function to get the path wanted
# using the pred list
def get_path(pred, t, s):
	path = []
	while pred[t] != -1:
		path.append(t)
		t = pred[t]
	path.append(s)
	return path[::-1]

# store the result of get_path from start to target word
result = get_path(pred, list(bk).index(tw), list(bk).index(sw))

# function to print the result
def print_result():
	if len(result) != 0:
		print(', '.join([list(bk)[i] for i in result]))
	else:
		print(sw)

# print desired output
print_result()