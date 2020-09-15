---
author: Mark Fontenot, PhD
subtitle: Intro to Python for CS and Data Science
title: CS 1340:Fall 2020:Lecture 07
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---
# Types - The Highlights

## Strings - 1

- **string literal** - 'SMU'
  - something enclosed in quotes
- **sequence type** - an ordered collection of items
  - `'SMU'` is really like `S` `M` `U`
  - The position in the sequence is called the **index**
  - **Indexes** start at **0**
 
## Strings - 2

(you know this already, but ...)

```{.python .run}
school_mascot = 'Peruna'
print (school_mascot)
print ('school_mascot')

```

## Strings - 3

- You can find the length of a _sequence_ by using the `len()` function

```{.python .run}
school_mascot = 'Peruna'
print(len(school_mascot))
```

## Strings - 4

- String Concatenation 

```{.python .run}
f_name = 'Mark'
l_name = 'Fontenot'
full_name = f_name + ' ' + l_name
```

(as we saw last week...)

- you cannot directly modify a string
  - you have to create a new string with what you want
  - … just a reminder
 
## Lists - 1

- **list** - a container that stores related values together 
- created using square brackets `[]`

```{.python .run}
universities = ['smu', 'tcu', 'utd', 'uta']
for school in universities:
    print (school)
```






