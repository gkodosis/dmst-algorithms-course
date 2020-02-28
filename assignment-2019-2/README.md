# Broken Telephone

<p align="center">
  <img src="http://q3research.com/wp-content/uploads/2014/02/Screen-Shot-2014-02-12-at-10.31.09-AM.png">
</p>

###### *This repository depicts an implementation of a "broken telephone application" for the self-titled assignment implemented in the context of the course "Algorithms and Data Structures". This is a course of the [Department of Management Science and Technology](https://www.dept.aueb.gr/en/dmst) (DMST) of Athens University of Economics and Business (AUEB), under the supervision of professor [Mr. Panagiotis Louridas](https://github.com/louridas).*

### *Main Functionality:*

*By running this source code in your local machine, you will be able to find the shortest path leading you from a starting word of your choice to another one. This problem is called "Broken Telephone" due to the fact that it is parallelized with the process of transfering a message from one person to another.*

*As in reality, we are trying to depict this situtation of altering a word from mouth to mouth, by providing the fastest way (if existed) to travel from a start to a target word.* 

*Each step depicted at the final output of the algorithm, refers to one modificitation done to the previous step-word (1 insertion or 1 deletion or 1 change of letters).*



# Implementation


### *Linux Environment*


> Clone the repository

```
git clone https://github.com/dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-2.git
```

> Navigate to directory

```
cd dmst-algorithms-course/gkodosis-algo-assignments/assignment-2019-2
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
python word_morph.py <filename> <start_node> <target_word>
```

### *Examples*

> Run 

```
In [1]:  python word_morph.py word_dict.txt life death
```
  life, lift, left, heft, heat, heath, death
