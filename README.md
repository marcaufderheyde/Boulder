# Boulder
A programming language called boulder which uses bouldering slang and lingo as it's standard library function names, uses python for the interpreter.

## Current supported functionality:

In version 0.1.0, Boulder implemented support for nested function calls, i.e., `send(crux("Marc"))`. However, nested function calls do not support parameter typing as of yet, this only works for single function calls, like so: `block(10)s`, where s types the parameter 10 as a string rather than the default int implementation. 

Below are the supported functions as of v0.1.0. Functions added in this version are listed in ***bold italics***.

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
python BoulderInterpreter.py helloworld.boulder
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
