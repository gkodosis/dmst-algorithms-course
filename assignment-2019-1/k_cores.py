import sys

# get input file from cmd
input = sys.argv[1]

# function to count unique nodes 
def count_nodes(): 
	with open(input, 'r') as graph:
		unique_list = [] 
		for line in graph:
			nodes = [int(x) for x in line.split()]
			if nodes[0] not in unique_list: 
				unique_list.append(nodes[0])
			if nodes[1] not in unique_list:
				unique_list.append(nodes[1])
	return len(unique_list)

# store function's result
V = count_nodes()
# degree
d = [0] * V
# potential
p = [0] * V
# algo results
core = [0] * V
# potential node
pn = []
# top element
t = []
# old potential node
opn = []
# new potential node
npn = []
# degree dictionary
degree = {}

"""Priority Queue as a Min-Heap Functions"""
def create_pq():
    return []

def add_last(pq, c):
    pq.append(c)

def root(pq):
    return 0

def set_root(pq, c):
    if len(pq) != 0:
        pq[0] = c

def get_data(pq, p):
    return pq[p]

def children(pq, p):
    if 2*p + 2 < len(pq):
        return [2*p + 1, 2*p + 2]
    else:
        return [2*p + 1]

def parent(p):
    return (p - 1) // 2

def exchange(pq, p1, p2):
    pq[p1], pq[p2] = pq[p2], pq[p1]

# based on weight
def insert_in_pq(pq, c):
    add_last(pq, c)
    i = len(pq) - 1
    while i != root(pq) and get_data(pq, i)[0] < get_data(pq, parent(i))[0]:
        p = parent(i)
        exchange(pq, i, p)
        i = p

def extract_last_from_pq(pq):
    return pq.pop()

def has_children(pq, p):
    return 2*p + 1 < len(pq)

# based on weight
def extract_min_from_pq(pq):
    c = pq[root(pq)]
    set_root(pq, extract_last_from_pq(pq))
    i = root(pq)
    while has_children(pq, i):
        # Use the data stored at each child as the comparison key
        # for finding the minimum.
        j = min(children(pq, i), key=lambda x: get_data(pq, x)[0])
        if get_data(pq, i)[0] < get_data(pq, j)[0]:
            return c        
        exchange(pq, i, j)
        i = j
    return c

# fuction to exchange tuples
def update_pq(pq, old, new):
    if old in pq:
        pq[pq.index(old)] = new
        i = pq.index(new)
        while i!= root(pq) and get_data(pq, i)[0] < get_data(pq, parent(i))[0]:
        	p = parent(i)
        	exchange(pq, i, p)
        	i = p

# function to calculate the degree of nodes
def count_degree():
	with open(input, 'r') as graph:
		for line in graph:
			nodes = [int(x) for x in line.split()]
			if nodes[0] not in degree:
				degree[nodes[0]] = []
			if nodes[1] not in degree:
				degree[nodes[1]] = []
			degree[nodes[0]].append(nodes[1])
			degree[nodes[1]].append(nodes[0])
		for d in degree:
			degree[d] = len(degree[d])
	return dict(sorted(degree.items()))

# store function's result
d = count_degree()

# min heap
mh = create_pq()

# function to initialize the variables
def initialize():
	for v in d.keys():
		p[v] = d[v]
		core[v] = 0
		pn = [p[v], v]
		insert_in_pq(mh, pn)
	return mh

# call function
initialize()
# neighboors dictionary
g = {}

# function to find the neighboors of a node
def neighboors():
	with open(input, 'r') as graph_input:
		for line in graph_input:
			nodes = [int(x) for x in line.split()]
			if len(nodes) != 2:
				continue
			if nodes[0] not in g:
				g[nodes[0]] = []
			if nodes[1] not in g:
				g[nodes[1]] = []
			g[nodes[0]].append(nodes[1])
			g[nodes[1]].append(nodes[0])
	return g

# store function's result
n = neighboors()

# function to find the k-cores
def k_cores():
	while len(mh) > 0:
		t = extract_min_from_pq(mh)
		core[t[1]] = t[0]
		if len(mh) != 0:
			for v in n[t[1]]:
				d[v] -= 1
				opn = [p[v], v]
				p[v] = max(t[0], d[v])
				npn = [p[v], v]
				update_pq(mh, opn, npn)
	return core

# store function's result
k = k_cores()

# function to print results
def print_results():
	for i,x in enumerate(k):
		print(i,x)

# call function
print_results()