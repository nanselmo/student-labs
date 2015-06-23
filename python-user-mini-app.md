---
  tags: raw_input(), variables, strings, interpolation
  languages: python
  level: 1
  type: lab
---

## User Input Mini App
Let's build a simple input/output app. The main objective is to create an application that _takes in user input, does something with that input, and then prints out an output_.

### Gets
The first thing we need to do is take in user input with the `raw_input()` method. When an executed Ruby program hits the method `raw_input()`, the program is going to pause and wait for the user to enter text into the terminal.

The way `raw_input()` takes in data from the user is important to remember. It does not interpret the data entered, it merely returns exactly what the user enters, the raw data. The second thing to remember is that `raw_input()` also takes one line of input, so once the user presses enter, their input data is complete.

### The Challenge: A Visit to My Favorite City
You're going to build a program that plans tourists' visits to your favorite city. Create a new file with `touch trip.py` in terminal. Open `trip.py` with Atom to start writing your program - `open -a Atom trip.py`.

You'll want to ask the user where they would like to stay, what sites they want to visit, what food they want to eat, and how many nights they want to stay. For each question, you'll take in input from the user and store each piece in a variable. <img src="https://s3.amazonaws.com/after-school-assets/greetings.jpg" align="right" width="300" hspace="20">

Once you have that input stored, you'll want to use string methods (like upper(), lower(), captialize(), etc) to put the input in a proper format. You can always take a look at the Python documentation [here](https://docs.python.org/2/library/stdtypes.html) to learn more about string methods you can use.

Your final output should use *string interpolation* to output the data in a full summary of their trip itinerary.

Remember, you can execute your code by typing `python trip.py` in terminal from inside the directory of this lab.
