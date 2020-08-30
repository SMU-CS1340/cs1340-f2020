---
author:
- Mark Fontenot, PhD
subtitle: Intro to Python for CS and Data Science
title: CS 1340:Fall 2020:Lecture 02
institute: Southern Methodist University
fontsize: 18pt
theme: metropolis
aspectratio: 169
---

## Reminders

- Slack
- Zybooks (hopefully you did the assignment due before class today?)
- Anaconda? 

# Getting Started


## All computer programs have ...

1. Input -

\vspace{1cm}

2. Processing -

\vspace{1cm}

3. Output -


## Drawing with the Turtle

\begin{center}
    \includegraphics[width=0.7\textwidth]{./assets/turtle-algo.png}
\end{center}

1. What's the input?
2. What's the processing?
3. What's the output?

## Challenge on your own time ..

Can you draw 'SMU' (block letters of course) with the Turtle?


## Humans vs. Computers

- Humans don't understand long strings of 1's and 0's 
- Computers don't understand  

``` {.python}
        print('Hello 1340')
```

\begin{center}
  \huge So what do we do???
\end{center}

## General _Algo_ for Programming

1. You write source code in a code editor or IDE (Integrated Development Environment)
2. Save it with a file extension of `.py`.  Example: `project01.py`
3. Use the Python interpreter to execute the source code.  
    - `python project01.py`
    - OR could be `python3 project01.py`
4. Back to Step 1 to add more code. 

## Converting Python Code to Machine Code

- Python is an **interpreted** language
  - as your program is running, the Python Interpreter / Runtime is converting source code to machine code one line by line. 
  - The alternative is a **compiled** language which converts all the source code to machine code before you run your program. 

\begin{center}
  \includegraphics[width=0.5\textwidth]{./assets/code-to-machine.png}
\end{center}

## Interactive Python 

- `python somescript.py` - runs the code inside somescript.py
- `python` - Starts the **interactive interpreter**
    - each line of code is interpreted right after you type it. 


\begin{center}
    \includegraphics[width=0.5\textwidth]{./assets/interactive_code.png}
\end{center}


## Elements of Python Code

- **statement** -
\vspace{.5cm} 
- **variable** - 
\vspace{.5cm}
- **expression** - 
\vspace{.5cm}
- **assignment** - 

## Some Python Code

```{.python}
def advance_cars():
    """Calculate new positions of the cars"""
    global car1_speed, car1_location
    global car2_speed, car2_location
    car1_speed += car1_acceleration
    car1_speed = car1_top_speed if car1_speed > car1_top_speed else car1_speed
    car1_location += car1_speed

    car2_speed += car2_acceleration
    car2_speed = car2_top_speed if car2_speed > car2_top_speed else car2_speed
    car2_location += car2_speed
```

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