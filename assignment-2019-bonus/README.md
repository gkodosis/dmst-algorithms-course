# Spanning Trees - kMST Problem 

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/16/Euclidean_minimum_spanning_tree.svg/300px-Euclidean_minimum_spanning_tree.svg.png">
</p>

###### *This repository depicts an implementation of the heuristic provided from [this paper](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.703.1725&rep=rep1&type=pdf) for the kMST problem, prepared for the self-titled bonus-assignment in the context of the course "Algorithms and Data Structures". This is a course of the [Department of Management Science and Technology](https://www.dept.aueb.gr/en/dmst) (DMST) of Athens University of Economics and Business (AUEB), under the supervision of professor [Mr. Panagiotis Louridas](https://github.com/louridas).*

### *Main Functionality:*

*There is a plynomial-time algorithm that given n points in the Euclidean plane and a positive integer k <= n (nodes-points), constructs a tree spanning at least k of these points such that the total length of the tree is at most O(k^1/4) times that for a minimum -length tree spanning any k of these points.*

*In this repository, we implement a python script that depicts a heuristic for the kMST problem for points on the plane and a proof of its performance guarantee.* 

*With inline-comments, each part of the code is being explained so as everyone can understand the way the kMST problem is being solved.*



# Implementation


### *Linux Environment*

> Clone the repository

```
git clone https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-bonus.git
```

> Navigate to directory

```
cd dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-bonus
```

> Sync python

```
alias python=python3
```

> Run 

```
python kmst.py <filename> <k>
```

### *Examples*

> Example 1

```
In [1]:  python kmst.py example_graph_1.txt 20
```

<p align="center">
  <img src="https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/blob/master/assignment-2019-bonus/example_graph_1_output.png?raw=true">
</p>

> Example 2

```
In [1]:  python kmst.py example_graph_2.txt 10
```

<p align="center">
  <img src="https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/blob/master/assignment-2019-bonus/example_graph_2_output.png?raw=true">
</p>

> Example 3

```
In [1]:  python kmst.py example_graph_3.txt 25
```

<p align="center">
  <img src="https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/blob/master/assignment-2019-bonus/example_graph_3_output.png?raw=true">
</p>

###### *A detailed view of the best-scoring (lowest) spanning tree for each example, is printed in your cmd after executing the script*