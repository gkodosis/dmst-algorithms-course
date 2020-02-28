from collections import defaultdict
from matplotlib import pyplot
from scipy.sparse.csgraph import minimum_spanning_tree
import pandas as pd
import numpy as np
import sys

# get input file from cmd
input = sys.argv[1]
# create dictionary
g = {}

# function to initialize the graph
def graph(): 
	with open(input, 'r') as graph_input:
		g = dict(enumerate(line.strip('\n').split(', ') for line in graph_input))
	return g

# store graph
g = graph()
# store number of graph's points
number_of_points = len(g)

# calcute euclidean distance of 2 points
def euclidean_distance(a,b):
	a = np.array([float(a[0]), float(a[1])])
	b = np.array([float(b[0]), float(b[1])])
	return np.sqrt(np.sum((a-b)**2))

# check if a point lines inside a circle of
# center: x_c, y_c and radious: r_c
def point_in_circle(p, x_c, y_c, r_c):
	if (float(p[0]) - x_c)**2 + (float(p[1]) - y_c)**2 <= r_c**2:
		return True
	else:
		return False

# set k variable from cmd
k = int(sys.argv[2])
# initialize empty dictionary to store fs
final_score = {}
# iterrate over all possible point-pairs
for i in range(1, number_of_points+1):
	for j in range(i+1, number_of_points):
		p1 = g[i]
		p2 = g[j]
		# (1) Contruct the circle
		x_c = (float(p1[0]) + float(p2[0])) / 2
		y_c = (float(p1[1]) + float(p2[1])) / 2
		d = 2*np.sqrt(3)*euclidean_distance(p1,p2)
		# (2) Check number of points inside the circle
		s_c = []
		for _, point in g.items():
			if point_in_circle(point, x_c, y_c, d/float(2)):
				s_c.append(point)
		# if less than k point fall inside the circle,
		# move on with the next pair
		if len(s_c) < k:
			continue
		# (3) Else, create the square circumscribing the circle
		# top left corner of square
		Q_a = (x_c - d/2, y_c + d/2)
		# top right corner of square
		Q_b = (x_c + d/2, y_c + d/2)
		# bottom right corner of square
		Q_c = (x_c - d/2, y_c - d/2)
		# bottom left corner of square
		Q_d = (x_c - d/2, y_c - d/2)
		# (4) Divide Q rectangle into k square cells with
		# side: diameter/sqrt(k)
		side = d/np.sqrt(k)
		mini_squares = defaultdict(list)
		selected_points = []
		for q_x in range(k):
			for q_y in range(k):
				# create the corners of the mini squares inside Q square
				mini_d = (Q_d[0] + q_x * side, Q_d[1] + q_y * side)
				mini_c = (Q_d[0] + (q_x+1) * side, Q_d[1] + q_y * side)
				mini_b = (Q_d[0] + (q_x+1) * side, Q_d[1] + (q_y+1) * side)
				mini_a = (Q_d[0] + q_x * side, Q_d[1] + (q_y+1) * side)
				# (5) Check for every point in s_c if it lies inside the min square
				for node in s_c:
					if ((float(node[0]) >= float(mini_d[0])) and (float(node[0]) <= float(mini_b[0])) and
					(float(node[1]) >= float(mini_d[1])) and (float(node[1]) <= float(mini_b[1]))):
						# if in rectangle
						mini_squares[str(q_x)+"_"+str(q_y)].append(node)
		# create sort list of (mini_square index, number of points) based
		# on how many points are in the mini_square
		sorted_list = [(index, mini_squares[index]) for index in sorted(mini_squares, 
						key=lambda index: len(mini_squares[index]), reverse=True)]
		# add each batch of points found in the mini rectangles
		# to the final list of selected points
		for m_index, batch_of_points in sorted_list:
			selected_points.extend(batch_of_points)
			# if we have reached or exceeded the k needed,
			if len(selected_points) >= k:
				# arbitrarily discard points
				selected_points = selected_points[:k]
				break
		# (6) Create the undirected graph of these selected points to be used
		# as input for the minimum spanning tree between them according to:
		# https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.sparse.csgraph.minimum_spanning_tree.html
		selected_points = sorted(selected_points)
		input_graph = np.zeros((len(selected_points), len(selected_points)))
		# create the upper triangular distance matrix for the undirected
		# graph of the selected points
		for s_i, p_i in enumerate(selected_points):
			for s_j in range(s_i+1, len(selected_points)):
				p_j = selected_points[s_j]
				input_graph[s_i, s_j] = euclidean_distance(p_i, p_j)
		# compute the mst of these data
		mst = minimum_spanning_tree(input_graph, overwrite=False)
		# (7) Form the solution produced from the mst created
		# For the i,j pair save the following:
		# the minimum spanning tree on these points
		# the score for this spanning tree (lower the better)
		# the selected points on which the spanning tree is created
		final_score[str(i)+"_"+str(j)] = {'MST': mst.toarray(), 'Value': mst.sum(), 'Points': selected_points}

# Output: Find the best-scoring (lowest) spanning tree
# initialize a large score
min_value = 10000000
min_value_key = -10000000
for k,v in final_score.items():
	if min_value > v['Value']:
		min_value = v['Value']
		min_value_key = k

print(min_value_key, final_score[min_value_key])

# Extra: Visualization of algo's behaviour
# set width, height
fig = pyplot.figure(figsize=(20,20))
# scatter points of graph with red color
pyplot.scatter([round(float(p[0]),2) for p in g.values()], [round(float(p[1]),2) for p in g.values()], color='red', s=10)
# iterate inside non-zero points of the mst
for pair_id in np.argwhere(final_score[min_value_key]['MST'] > 0):
	p1 = final_score[min_value_key]['Points'][pair_id[0]]
	p2 = final_score[min_value_key]['Points'][pair_id[1]]
	# conect the nodes with a blue line
	pyplot.plot([float(p1[0]), float(p2[0])], [float(p1[1]), float(p2[1])], c='blue')
# display result
pyplot.show()





				
