---
author: Mark Fontenot, PhD
subtitle: Intro to Python for CS and Data Science
title: CS 1340:Fall 2020:Lecture 14  
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---

# Repetition Practice

## Empty Square

- write code to draw an empty square based upon a value entered by the user.  If the user entered 6, the output should be: 
```python
******
*    * 
*    *
*    *
*    *
******    

```

## Right Triangle

- write code to draw a right leaning right triangle based upon the value entered by the user. If the user entered 6, the output should be:
```txt
     * 
    **
   ***
  ****
 *****
******
```
- … Now do it and only output the outline of the triangle. 

# Functions

## A Function is .. 

- A **function** is a named set of statements. 

- Parts
  - **function definition** - the new functions name and the statements that make up the function
  - **function call** - the invocation of the function (asking the function to be executed)
 
## Functions We've Seen

- `print(...)`
- `int(...)`
- `readlines(...)`

- These aren't magic... someone somewhere wrote code that is executed every time you call them. 

## Function Example

```python
def some_function():
  human_years = 3
  dog_multiplier = 7

  dog_age = human_years * dog_multiplier
  print(dog_age)
```

```python
some_function()
```

## Pizza Area

```{.python .run}

def print_pizza_area():
   pi_val = 3.14159265

   pizza_diameter = 12.0
   pizza_radius = pizza_diameter / 2.0
   pizza_area = pi_val * pizza_radius * pizza_radius
   print('{:.1f} inch pizza is {:.3f} square inches'
       .format(pizza_diameter, pizza_area))

print_pizza_area()
```

## Function - Some Details

- `def fun_name():` <-- Don't forget the ()
- Functions need to be defined above any calls to that function
- Each line of code inside a function should be indented one level
- Functions can contain other control structures such as ifs and loops

## Function Parameters

- **Parameter** - a piece of data that is needed for a function to execute
  - Example: A function to calculate a tip will need the amount of the check
- **Argument** - an actual value that is used in a function call to pass to a parameter

```python
def tip_calculator(check_amount):
  tip_percentage = .2
  print ("20% tip on", check_amount, "is", tip_percentage)

tip_calculator(34.21)
```
- **check_amount** is the parameter; **34.21** is the argument. 


## Multiple Parameters

- a function can take multiple parameters.  
- separate each parameter with a comma.

```{.python .run}
def fountain_volume(length, width, depth):
  volume = length * width * depth
  print("The fountain is", volume, "cubic feet")

fountain_volume(10, 5, 2)
```






