import string
from tabulate import tabulate


#Scans given input for tokens and returns a symbol table with found token token names and values.
#If invalid input is found, prints it to the console.
def scan(input, digit, posdigit, letter, type, boolean, keyword, arithmetic, comparison, brace, paren, bracket, whitespace):
    symbol_table = []

    temp_token = "" #temp_token will be used to test if input matches tokens
    i = 0
    # Starting to scan input:
    while i < len(input):

        # Skip whitespace
        if input[i] in whitespace:
            pass

        # Testing for tokens that can start with a letter (TYPE, BOOLEAN, KEYWORD, IDENTIFIER)
        elif input[i] in letter:
            while input[i] in letter:
                temp_token += input[i]
                i += 1
            else:
                i -= 1
                # Testing for TYPE
                if temp_token in type:
                    symbol_table += [["TYPE", temp_token]]
                    temp_token = ""

                # Testing for BOOLEAN
                elif temp_token in boolean:
                    symbol_table += [["BOOLEAN", temp_token]]
                    temp_token = ""

                # Testing for KEYWORD
                elif temp_token in keyword:
                    symbol_table += [["KEYWORD", temp_token]]
                    temp_token = ""

                # Testing for IDENTIFIER:
                else:
                    if input[i+1] == "_" or input[i+1] in digit: #Testing to see if identifier continues
                        i += 1
                        while input[i] in letter or input[i] in digit or input[i] == "_":
                            temp_token += input[i]
                            i += 1
                        else:
                            i -= 1
                            symbol_table += [["IDENTIFIER", temp_token]]
                            temp_token = ""
                    else:
                        symbol_table += [["IDENTIFIER", temp_token]]
                        temp_token = ""

        # Testing for IDENTIFIERs that start with _ (underscore):
        elif input[i] == "_":
            temp_token += input[i]
            i += 1
            while input[i] in letter or input[i] in digit or input[i] == "_":
                temp_token += input[i]
                i += 1
            else:
                i -= 1
                symbol_table += [["IDENTIFIER", temp_token]]
                temp_token = ""


        # Testing for INT (only positive numbers):
        elif input[i] in posdigit:
            temp_token += input[i]
            i += 1
            while input[i] in digit:
                temp_token += input[i]
                i += 1
            else:
                symbol_table += [["INT", temp_token]]
            i -= 1
            temp_token = ""

        # Testing for INT (just the value 0):
        elif input[i] == "0":
            symbol_table += [["INT", "0"]]

        # Testing for tokens that can start with - (INT, ARITHMETIC)
        elif input[i] == "-":
            # If input continues with digits it's INT, otherwise it's ARITHMETIC
            if input[i+1] in digit:
                temp_token += "-"
                i += 1
                while input[i] in digit:
                    temp_token += input[i]
                    i += 1
                else:
                    symbol_table += [["INT", temp_token]]
                i -= 1
                temp_token = ""
            else:
                symbol_table += [["ARITHMETIC", input[i]]]

        # Testing for the rest of ARITHMETIC:
        elif input[i] in arithmetic:
            symbol_table += [["ARITHMETIC", input[i]]]

        # Testing for tokens that can start with = (ASSIGN, COMPARISON)
        elif input[i] == "=":
            if input[i+1] == "=": # if next character is "="
                symbol_table += [["COMPARISON", "=="]]
            else:
                symbol_table += [["ASSIGN", input[i]]]

        # Testing for rest of COMPARISON tokens:
        elif input[i] == "<" or input[i] == ">" or input[i] == "!":
            temp_token += input[i]
            if input[i+1] == "=":
                temp_token += "="
            symbol_table += [["COMPARISON", temp_token]]
            temp_token = ""
            i += 1

        # Testing for TERMINATE:
        elif input[i] == ";":
            symbol_table += [["TERMINATE", input[i]]]

        # Testing for BRACE:
        elif input[i] in brace:
            symbol_table += [["BRACE", input[i]]]

        # Testing for PAREN:
        elif input[i] in paren:
            symbol_table += [["PAREN", input[i]]]

        # Testing for BRACKET:
        elif input[i] in bracket:
            symbol_table += [["BRACKET", input[i]]]

        # Testing for SEPERATE:
        elif input[i] == ",":
            symbol_table += [["SEPERATE", input[i]]]

        #Testing for STRING
        elif input[i] == "\"":
            temp_token += input[i]
            i += 1
            while input[i] in letter or input[i] in digit or input[i] == " ":
                temp_token += input[i]
                i += 1
            else:
                #Testing if string contains symbols that are not allowed:
                if input[i] == "\"":
                    temp_token +=  "\""
                    symbol_table += [["STRING", temp_token]]

                else:
                    print("ERROR: Invalid input for STRING: ", input[i])
                    # Skip rest of the string:
                    while input[i] != "\"":
                        i += 1
            temp_token = ""


        # Testing for CHAR
        elif input[i] == "\'":
            # CHAR has always three characters:
            temp_token += input[i]
            i += 1
            if input[i] in digit or input[i] in letter or input[i] == " ":
                temp_token += input[i] #digit, letter or blank
                i += 1
                temp_token += input[i]
                symbol_table += [["CHAR", temp_token]]
            else:
                print("ERROR: Invalid input for CHAR: ", input[i])
                i += 1
            temp_token = ""

        #If input[i] is not recognized
        else:
            print("ERROR: Invalid input ", input[i])
        i += 1

    # When scanning is ready:
    return symbol_table
