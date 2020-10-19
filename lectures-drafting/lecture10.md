---
author: Mark Fontenot, PhD
subtitle: Intro to Python for CS and Data Science
title: CS 1340:Fall 2020:Lecture 10
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---
# Control Structure Review

## `if` statements

```python
x = 10
if x == 10:
    print('x is', x)
else:
    print('x is not 10')
```

## `if`s 

```{.python .run}
x = 10
y = 20

if x == 10 and y != 10:
    print('Isn\'t this fun?')
elif y == 20:
    print('Can\'t you tell that y is 20?')
else:
    print('Go Home!')
```

## `for`

```{.python .run}
for x in range(5, 10):
    print (x)
```

## `for`

```{.python .run}
names = ['Mark', 'Brian', 'Amanda']

for name in names:
    print(name)

```

# Algorithm Development

## Find the Best Grade

```{.python .run}
grades = [88, 92, 76, 94, 95, 93, 99, 89, 82]
# Which students (index) got the highest score? 
```



