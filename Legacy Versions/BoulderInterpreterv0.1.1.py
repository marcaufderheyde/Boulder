import sys
import time

# Welcome to the Boulder programming language interpreter v0.1.1
# Please refer to the official documentation which can be found here on GitHub:
# https://github.com/marcaufderheyde/Boulder
# The slang/lingo used in the language definition is based on this article 
# from the independent: https://www.independent.com/2008/05/15/guide-bouldering-lingo/
#
# Fixes: 
# ==>   NESTED function calls, i.e., send(flash(jug([1,2,3]))), now support parameter typing
#
# Roadmap:
# ==>   Unless bugs are found, v0.2.0 will include the ability to define functions in .boulder
#       porgrams.


# Function wrappers for variations of standard functions
def printCaps(input):
    print(input.upper())
    
def sketchyRock():
    print("I don't know man, looks pretty suss to me!")
    
def routeAnim(length = 22):
    converted_length = length
        
    if type(length) is not int:
        converted_length = int(length)

    bar = [
        " [u          ]\n [u          ]",
        " [ =         ]\n [ =         ]",
        " [  =        ]\n [  =        ]",
        " [           ]\n [           ]",
        " [       =   ]\n [       =   ]",
        " [    =      ]\n [    =      ]",
        " [     =     ]\n [     =     ]",
        " [           ]\n [           ]",
        " [    =      ]\n [    =      ]",
        " [      \    ]\n [      \    ]",
        " [  =        ]\n [  =        ]",
        " [ u         ]\n [ u         ]",
    ]
    
    i = 0
    print("\nEND")
    while i < converted_length:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        i += 1
    print("\nSTART\n")


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
    "toeHook": type,
    "choss": sketchyRock,
    "makeRoute": routeAnim
    
}

# Reference for which boulder functions print output so we know when to show the ouput manually
printer_funcs = ["send", "fullSend", "makeRoute"]

printer_funcs_no_input = ["choss"]

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
        #try:    
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
            
            # We need to carry on our calculation through function calls in the bottom while loop
            current_computation = ""
                            
            # Ability to comment in .boulder program files and leave empty lines
            if("<=== 420XD69 ===>" in line or len(line) == 0):
                continue

            # Let's split our line into function call and arguments
            # The final component will be the inner most parameter along
            # with any parameter typings
            components = line.strip(")").split("(")

            # Depending on where the param type is placed in the call, we get different
            # numbers of param_types, but we need one for each function call
            param_types = components[len(components) - 1].split(")")[1:]
            
            if len(param_types) != len(components[:-1]):
                while len(param_types) < len(components[:-1]):
                    param_types.append("")
            
            # Take a reference of the final function call to decide whether to print result representation
            final_call = components[0]

            index = len(components) - 1
            original_index = len(components) - 1
            
            # The parameters we get go from inner most to outer, so reverse indexxing
            # to the function calls which we get as outer most to inner
            param_index = 0
            
            while len(components) > 0 and (index - 1) >= 0:
                                
                # Bouldering functions can specify the type of the parameters by adding a letter after the
                # last parentheses
                param_type = param_types[param_index]

                # Are we at the inner most call? If yes, set our initial param for carry on computation
                if(index == original_index):
                    current_computation = components[index].split(")")[0].strip("\"")

                # But there is a caveat, we don't want printer functions for instance to change the param type
                # and invalid or unsupported types should be ignored and reset to default string
                if(components[index-1] in printer_funcs or components[index-1] in printer_funcs_no_input or param_type not in ['s', 'i', 'f']):
                    param_type = 's'
                                                    
                match param_type:
                    # s forces parameters to be of type string
                    case "s":
                        # If we can find the function name in our documentation dictionary, it's a valid line
                        if(components[index-1] in documentation):
                            lines_recognized += 1
                            
                            format_supported = False
                                                        
                            # We need to make sure our parameters are in the correct format i.e., an empty string cannot be converted to int
                            format_supported = current_computation != ''

                            # Just print directly if supported with no input
                            if(components[index-1] in printer_funcs and format_supported):
                                documentation[components[index-1]](current_computation)
                                
                            # Just print directly if supported with no input
                            elif(components[index-1] in printer_funcs_no_input):
                                documentation[components[index-1]]()
                                
                            # List functions require some tweaking for the params as they're coming as strings    
                            elif(components[index-1] in list_funcs and format_supported):
                                list_param = current_computation.split(")")[0].strip("\"").strip("[").strip("]").split(",")
                                result = documentation[components[index-1]](list_param)
                                current_computation = result
                                
                            # Otherwise provide a representation of the computation
                            elif(format_supported):                                  
                                result = documentation[components[index-1]](current_computation)
                                current_computation = result
                            
                            else:
                                result = documentation[components[index-1]](current_computation)
                                current_computation = result

                                
                        else:
                            lines_unrecognized += 1
                            error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
                    
                    # i forces parameters to be of type int
                    case "i":
                        # If we can find the function name in our documentation dictionary, it's a valid line
                        if(components[index-1] in documentation):
                            lines_recognized += 1
                            
                            format_supported = False
                                                        
                            # We need to make sure our parameters are in the correct format i.e., an empty string cannot be converted to int
                            format_supported = current_computation != ''
                            
                            # Just print directly if supported
                            if(components[index-1] in printer_funcs and format_supported):
                                documentation[components[index-1]](int(current_computation))
                                
                            # Just print directly if supported with no input
                            elif(components[0] in printer_funcs_no_input):
                                documentation[components[index-1]]()
                            
                            # List functions require some tweaking for the params as they're coming as strings    
                            elif(components[index-1] in list_funcs and format_supported):
                                list_param = current_computation.split(")")[0].strip("\"").strip("[").strip("]").split(",")
                                int_list_param = [int(el) for el in list_param]
                                result = documentation[components[index-1]](int_list_param)
                                current_computation = result
                                
                            # Otherwise provide a representation of the computation
                            elif(format_supported):
                                result = documentation[components[index-1]](int(current_computation))
                                current_computation = result
                                
                            # If format is not supported, we have encountered an empty string as our parameter, so treat as such
                            else:
                                result = documentation[components[index-1]](int(current_computation))
                                current_computation = result
                        else:
                            lines_unrecognized += 1
                            error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
                    
                    # f forces parameters to be of type float
                    case "f":
                        # If we can find the function name in our documentation dictionary, it's a valid line
                        if(components[index-1] in documentation):
                            lines_recognized += 1
                            
                            format_supported = False
                                                        
                            # We need to make sure our parameters are in the correct format i.e., an empty string cannot be converted to int
                            format_supported = current_computation != ''
                            
                            # Just print directly if supported with input
                            if(components[index-1] in printer_funcs and format_supported):
                                documentation[components[index-1]](float(current_computation))
                                
                            # Just print directly if supported with no input
                            elif(components[index-1] in printer_funcs_no_input):
                                documentation[components[index-1]]()
                            
                                
                            # List functions require some tweaking for the params as they're coming as strings    
                            elif(components[index-1] in list_funcs and format_supported):
                                list_param = current_computation.split(")")[0].strip("\"").strip("[").strip("]").split(",")
                                int_list_param = [float(el) for el in list_param]
                                result = documentation[components[index-1]](int_list_param)
                                current_computation = result
                                
                            # Otherwise provide a representation of the computation
                            elif(format_supported):
                                result = documentation[components[index-1]](float(current_computation))
                                current_computation = result
                            else:
                                result = documentation[components[index-1]](current_computation)
                                current_computation = result
                        else:
                            lines_unrecognized += 1
                            error_log = error_log + "Interpreter failed to recognize line " + str(total_lines) + ", please check the function name is correct: " + line + "\n"
                
                # Reset our param type to the default and move on to the next function call
                param_type = "s"
                del components[index]
                index -= 1
                param_index += 1
                
            if(final_call not in printer_funcs and final_call not in printer_funcs_no_input):
                print("Result of: " + line + " is: " + str(current_computation) + " which is of type: " + str(type(current_computation)))

                
        #except Exception as e:
        #    print("\nBoulderInterpreter encountered an error on line " + str(total_lines) + ":\n" + str(e))
        print("\n<=====================================PROGRAM EXECUTION ABOVE==========================================>\n")
                
        print("Out of " + str(total_lines) + " lines processed from " + sys.argv[1] + ", the interpreter recognized and attempted to execute " + str(lines_recognized) + "\n")
        print(error_log)
    

if __name__ == "__main__":
    main()
    