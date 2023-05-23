import sys

# Function wrappers for variations of standard functions
def printCaps(input):
    print(input.upper())

# Dictionary to contain our references from .boulder functionality to python functions defined in the interpreter
documentation = {
    "send":print,
    "fullSend": printCaps,
    "crux": len,
    "flash": str,
    "block": int,
    "slab": float,
    "jug": max,
    "pivot": min,
    "heelHook": sorted,
    "toeHook": type
}

# Reference for which boulder functions print output so we know when to show the ouput manually
printer_funcs = ["send", "fullSend"]

# Reference for functions which work on lists
list_funcs = ["jug", "pivot", "heelHook"]

# Main function which is run on command line
def main():

    # Our default parameter type is a string
    param_type = "s"

    # Some variables to track the success of our interpretation
    lines_recognized = 0
    lines_unrecognized = 0
    total_lines = 0
    error_log = ""

    # Some welcome text to indicate correct usage
    print("Welcome to the boulder programming language interpreter!")
    print("To use this interpreter, please insert the filename of your .boulder program as a command line argument!\n")
    print("<===================================PROGRAM LINES FOUND BELOW==========================================>\n")
    
    
    # If there is only one command line argument, nothing to interpret, so exit
    if(len(sys.argv) == 1):
        exit(0)
        
    # Otherwise continue and try to interpret
    elif(len(sys.argv) > 1):
        program_lines = None
        
        # We need to exit if our filename doesn't contain .boulder
        if(".boulder" not in sys.argv[1]):
            exit(0)
            
        # If we've made it here, we havea  valid program file with .boulder which we can attempt to interpret
        with open(sys.argv[1], "r") as file1:
        
            # Save the program lines for processing
            program_lines = file1.read()
            print(program_lines)
            program_lines = program_lines.split("\n")

        print("\n<=====================================PROGRAM EXECUTION BELOW==========================================>\n")

        # Begin processing the program lines
        for line in program_lines:
            total_lines += 1
            
            # Ability to comment in .boulder program files and leave empty lines
            if("<=== 420XD69 ===>" in line or len(line) == 0):
                continue

            # Let's split our line into function call and arguments
            components = line.strip(")").split("(")
            
            # Bouldering functions can specify the type of the parameters by adding a letter after the
            # last parentheses
            if(len(components[1].split(")")) == 2):
                param_type = components[1].split(")")[1]
                
            match param_type:
                case "s":
                    # If we can find the function name in our documentation dictionary, it's a valid line
                    if(components[0] in documentation):
                        lines_recognized += 1
                        
                        # Just print directly if supported
                        if(components[0] in printer_funcs):
                            documentation[components[0]](components[1].strip("\""))
                            
                        # List functions require some tweaking for the params as they're coming as strings    
                        elif(components[0] in list_funcs):
                            list_param = components[1].strip("\"").strip("[").strip("]").split(",")
                            result = documentation[components[0]](list_param)
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                            
                        # Otherwise provide a representation of the computation
                        else:
                            result = documentation[components[0]](components[1].strip("\""))
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                    else:
                        lines_unrecognized += 1
                        error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
                
                case "i":
                    # If we can find the function name in our documentation dictionary, it's a valid line
                    if(components[0] in documentation):
                        lines_recognized += 1
                        
                        # Just print directly if supported
                        if(components[0] in printer_funcs):
                            documentation[components[0]](int(components[1].split(")")[0].strip("\"")))
                            
                        # List functions require some tweaking for the params as they're coming as strings    
                        elif(components[0] in list_funcs):
                            list_param = components[1].split(")")[0].strip("\"").strip("[").strip("]").split(",")
                            int_list_param = [int(el) for el in list_param]
                            result = documentation[components[0]](int_list_param)
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                            
                        # Otherwise provide a representation of the computation
                        else:
                            result = documentation[components[0]](int(components[1].split(")")[0].strip("\"")))
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                    else:
                        lines_unrecognized += 1
                        error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
            
                case "f":
                    # If we can find the function name in our documentation dictionary, it's a valid line
                    if(components[0] in documentation):
                        lines_recognized += 1
                        
                        # Just print directly if supported
                        if(components[0] in printer_funcs):
                            documentation[components[0]](float(components[1].split(")")[0].strip("\"")))
                            
                        # List functions require some tweaking for the params as they're coming as strings    
                        elif(components[0] in list_funcs):
                            list_param = components[1].split(")")[0].strip("\"").strip("[").strip("]").split(",")
                            int_list_param = [float(el) for el in list_param]
                            result = documentation[components[0]](int_list_param)
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                            
                        # Otherwise provide a representation of the computation
                        else:
                            result = documentation[components[0]](float(components[1].split(")")[0].strip("\"")))
                            print("Result of: " + line + " is: " + str(result) + " which is of type: " + str(type(result)))
                    else:
                        lines_unrecognized += 1
                        error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
            
            # Reset our param type to the default
            param_type = "s"
    
        print("\n<=====================================PROGRAM EXECUTION ABOVE==========================================>\n")
                
        print("Out of " + str(total_lines) + " lines processed from " + sys.argv[1] + ", the interpreter recognized and attempted to execute " + str(lines_recognized) + "\n")
        print(error_log)
    

if __name__ == "__main__":
    main()
    