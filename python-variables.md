---
tags: kids, variables, strings
languages: python
level: 1
type: lab
---
##Mini-Lab: Variables Practice

###What is a Variable?
We use variables in programming to store pieces of data. Variables can store any type of data (strings, integers, floats, etc). When we name a variable, we use all lowercase letters. For example:
```python
minion = "Kevin"
```
All we've done is defined a variable named `minion` and set it equal to the string `"Kevin"`. Now, any time we tell our program to `print minion`, it will print out `Kevin`.
```python
print minion
print minion
print minion
```
In this example, we should see `Kevin` printed out three times.
```
Kevin
Kevin
Kevin
```
What would happen if we did the following:
```python
name = "Kevin"
name = "Carl"

print name
```
On the first line, we assigned the variable `name` to store `Kevin`. On the next line, we reassigned the value of the variable `name` to store `Carl`. Each variable can only store one value, so all we did was overwrite the value of the `name` variable. When we `print name` on the last line, we will see `Carl` printed out.

What if we want to have more than one word in our variable? Like:
```python
despicable me = "Gru"

print despicable me
```
Python gives us an error! `SyntaxError: invalid syntax`. Python doesn't know what `despicable` is because of the space between the words `despicable` and `me`. Python doesn't recognize `despicable` as a key word (like print) or as a data type, so it throws an error. It's just like when we're creating directories or files in the terminal, the space confuses the computer. Instead, replace spaces with underscores:

```python
despicable_me = "Gru"

print despicable_me
```
###Let's practice!
What will be printed to the screen after running each of these? Talk to a partner and decide on an answer before running your code from a python file that you create called `variables_practice.py`.
???
# Variables Practice

?: What is the outcome of running the code below?
```python
a = 25
b = 36

print a * b
```
[-]

?: What is the outcome of running the code below?
```python
dog = "Ralph"
cat = "Whiskers"

print dog + cat
```
[-]

?: What is the outcome of running the code below?
```python
band = "The Beatles"

print "My favorite band is " + band
```
[-]

?: What is the outcome of running the code below?
```python
first = "BARACK"
last = "OBAMA"
age = 53

print "The president of the US is " + first.capitalize() + " "+ last.capitalize() + " and he is " + str(age) + " years old."
```
[-]

?: What is the outcome of running the code below?
```python
artist_first = "NiCKi"
artist_last = "MiNaj"

print "When I listen to " + artist_first.upper() + " " + artist_last.lower() + " I feel like my brain is melting."
```
[-]

?: What is the outcome of running the code below? Enter your information in the values below
```python
name = "your_name"
age = #your age as an integer
location = "your_hometown"

print "Hi. I'm " + name.upper() + ". I'm from " + location.swapcase() + "and in ten years I'm going to be " + str((age+10))
```
[-]

?: What would be the difference between the product and the sum?
Set `x` equal to 34679, `y` equal to 566 and `z`equal to 47. Output the product of these three numbers. Then output the sum of the three numbers. Assign each of these to a new variable and then find the difference between the product and the sum.
[-]

???
