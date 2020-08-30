---
author:
- Mark Fontenot, PhD
subtitle: Intro to Python for CS and Data Science
title: CS 1340:Fall 2020:Lecture 03
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---


# Finishing up Slides from Thursday

## Basic Output


`print(...)`


- Notice:
  - printed in mono-spaced font
  - ... means other stuff will be put there 
  - () indicate a method or function call

```{.python}
print('Hello')
print('World')
print('Hello World')
```
`'Hello'`, `'World'` are called **string literals**. 

## `print(...)`

```{.python}
name = 'Mark'
print(name)
```

- You can print **string literals** OR values contained in variables. 
- What is the variable in this example? 

```{.python}
print('Hello', end='')
print('World', end='')
```

- What will this print?

## Can you do it?

> Use print statements to draw a diamond shape. 

\vspace{1cm}

> Use print statements to draw a heart shape.

# New Stuff

## Printing On Different Lines

- Options:
  - use separate `print()` statements
  - embed `\n` in string literal

```python
    print('Hello')
    print('World')
    print('Hello\nWorld')

```

## Printing Multiple things with `print(...)`


  
```{.python .run}
age = 19
print('I\'m currently', age, 'years old.')
age = age + 1
print('On my next birthday, I will be', age, 'years old.')
```
\vspace{.5cm}



