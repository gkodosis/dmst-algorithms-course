import argparse
from math import sin, cos, radians, ceil
import json
import sys

# get json file from cmd
json_data = sys.argv[1]

# lsystem
lsystem = {}

# read json file
def initialize():
	with open(json_data) as f:
		lsystem = json.load(f)
	return lsystem

# get json file's data
lsystem = initialize()

# functions to get data
def axiom():
	return lsystem['axiom']

def order():
	return lsystem['order']

def rules():
	return lsystem['rules']

def step_length():
	return lsystem['step_length']

def start_angle():
	return lsystem['start_angle']

def left_angle():
	return lsystem['left_angle']

def right_angle():
	return lsystem['right_angle']

# store data 
axiom = axiom()
order = order()
rules = rules()
step_length = step_length()
start_angle = start_angle()
left_angle = left_angle()
right_angle = right_angle()

# create rules
def create_rules(rules, state):
	result = list()
	for c in state:
		result.append(rules.get(c, c))
	return "".join(result)	

# first itteration
steps = [axiom]

# Apply the rules at each iteration
def apply_rules():
	for i in range(1, order + 1):
		steps.append(create_rules(rules, steps[i-1]))
	return steps[-1]

# store rules
after_rules = apply_rules()

# change direction
def rotate_direction(step, angle, directed_angle):
   	angle += directed_angle
   	return angle

# rotate based on agle
def rotate_point(x, y, angle):
    # rotate point
    s = sin(radians(angle))
    c = cos(radians(angle))
    # apply rotations
    new_x = round((step_length * c + x), 2)
    new_y = round((step_length * s + y), 2)
    return (new_x, new_y)

# parse steps and convert to drawing instructions
def parse_step(stack=[], a_stack=[]):
	x = start_angle
	y = start_angle
	angle = start_angle
	file = open(sys.argv[2], 'w')
	for step in after_rules:
		if step in 'F' or step in 'G':
			new_x, new_y = rotate_point(x, y, angle)
			file.write(str((x,y)) + ' ' + str((new_x, new_y)) + '\n')
			x, y = new_x, new_y
		elif step == '+':
			angle = rotate_direction(step, angle, left_angle)
		elif step == '-':
			angle = rotate_direction(step, angle, right_angle)
		elif step == '[':
			stack.append((x,y))
			a_stack.append(angle)
		elif step == ']':
			(x,y) = stack.pop()
			angle = a_stack.pop()
		else:
			pass

# call parser
parse_step()

# handle output based on parameters
if sys.argv[2] == '-m':
	print(after_rules)