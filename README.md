# Boulder
A programming language called boulder which uses bouldering slang and lingo as it's standard library function names, uses python for the interpreter.

## Current supported functionality:

In version 0.2.0, Boulder implemented support for function definitions. A function definition in boulder looks something like this: 

```HOLD sendAsFloatAndInt(value1) => send(value1)f SLOPER send(value1)i```

`HOLD` is the equivalent of `def` in python, indicating a function definition. Next is the name of the function and the parameters it takes. The `=>` separates the function signature from the function code. Multiple lines of function code are supported by using the `SLOPER` keyword between individual lines. So the above function in Boulder, would have the following equivalent in python:

```
def sendAsFloatAndInt(value1):
  print(float(value1))
  print(int(value1))
```

**NOTE**: The current implementation of function definitions has not been tested thuroughly and should be treated with caution. Please report any bugs. It is currently unclear whether function definitions with multiple parameters are supported by the implementation.

Below are the supported functions as of v0.2.0. Functions added in this version, or simply the newest functions are listed in ***bold italics***.

| Boulder function  | Python equivalent |
| ------------- | ------------- |
| send()  | print() |
| fullSend()  | print() but in all caps |
| crux()  | len() |
| flash()  | str() |
| block()  | int() |
| slab()  | float() |
| jug(list)  | max(list) |
| pivot(list)  | min(list) |
| heelHook(list)  | sorted(list) |
| toeHook()  | type() |
| ***choss()***  | ***custom function which comments on the quality of a certain hold*** |
| ***makeRoutes(routeHeight)***  | ***custom function which animates a bouldering route being created*** |

You can make comments in .boulder program files by using `<=== 420XD69 ===>` at the start of a line, like so:
```
<=== 420XD69 ===> This is a comment in the Boulder programming language!
```

Lines with only whitespace will also be ignored by the interpreter and treated as a comment.

## Example program
An example program would be like so: A file called `helloworld.boulder`, note that the interpreter will ignore any files without the .boulder extension.

```
<=== 420XD69 ===> This is an example boulder program

<=== 420XD69 ===> fullSend() prints the input in capital letters
fullSend("my name is Marc")
```

To run the program using the interpreter, make sure to have the interpreter and your .boulder file in the same directory. Then proceed to run the interpreter with the filename as a command line argument such as:
```
python BoulderInterpreterv0.2.0.py helloworld.boulder
```
The output of the above program would be: 
```
Welcome to the boulder programming language interpreter!
To use this interpreter, please insert the filename of your .boulder program as a command line argument!

<===================================PROGRAM LINES FOUND BELOW==========================================>

<=== 420XD69 ===> This is an example boulder program

<=== 420XD69 ===> fullSend() prints the input in capital letters
fullSend("my name is Marc")

<=====================================PROGRAM EXECUTION BELOW==========================================>

MY NAME IS MARC

<=====================================PROGRAM EXECUTION ABOVE==========================================>

Out of 4 lines processed from helloworld2.boulder, the interpreter recognized and attempted to execute 1
```
