# K-Cores Algorithm

<p align="center">
  <img src="https://i.stack.imgur.com/l3RQc.png">
</p>

###### *This repository depicts an implementation of the k-cores algorithm for the self-titled assignment implemented in the context of the course "Algorithms and Data Structures". This is a course of the [Department of Management Science and Technology](https://www.dept.aueb.gr/en/dmst) (DMST) of Athens University of Economics and Business (AUEB), under the supervision of professor [Mr. Panagiotis Louridas](https://github.com/louridas).*

### *Main Functionality:*

*By running this source code in your local machine, you will be able to select a graph of your own preference (in the format indicated at the uploaded example file) and produce the k-core value for each node of your graph.*

### *Example Applications*

* Example Graph 

This file contains a simple graph in order to check if the output of the algorithm, produces the correct results

> Run Algo

```
python k_cores.py human_brain_functional_activations.txt
```

* Human Brain Functional Activations 

This file contains a graph of 638 nodes and 18625 edges. The nodes depict different parts of the human brain and the edges refer to the parts that become active at the same time. For info can be found [here](https://sites.google.com/site/bctnet/datasets)

> Run Algo

```
python k_cores.py human_brain_functional_activations.txt
```

* Barabási – Albert Graph

This file contains a graph was created as an extend of the model from Albert and Barabási. For info can be found [here](http://barabasi.com/f/83.pdf)

> Run Algo

```
python k_cores.py ebag.txt
```



# Implementation


### *Linux Environment*


> Clone the repository

```
git clone https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-1.git
```

> Navigate to directory

```
cd dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-1
```

> Install python3

```
sudo apt-get install python3
```

> Sync python

```
alias python=python3
```

> Run 

```
python k_cores.py <filename>
```

> Compare Algo Results with Solution 

```
python k_cores.py <filename> > k_cores_results
diff k_cores_results <filename_solution>
```