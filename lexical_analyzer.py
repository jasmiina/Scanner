import string
from tabulate import tabulate
import scanner
import sys
import glob
import os.path

#Scans input file for tokens and outputs them as a symbol table.
#Possible tokens: TYPE, INT, CHAR, BOOLEAN, STRING, IDENTIFIER, KEYWORD, ARITHMETIC, ASSIGN, COMPARISON, TERMINATE,
#BRACE, PAREN, BRACKET, SEPERATE, WHITESPACE

#Makes lists of accepted input for predefined tokens like BOOLEAN and TYPE and returns them
def define_lists ():
    digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posdigit = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    letter = list(string.ascii_letters) #all uppercase and lowercase English letters

    type = ["int", "String", "char", "boolean"]
    boolean = ["true", "false"]
    keyword = ["if", "else", "while", "return", "class"]
    arithmetic = ["+", "-", "*", "/"]
    comparison = ["<", ">", "==", "!=", "<=", ">="]
    brace = ["{", "}"]
    paren = ["(", ")"]
    bracket = ["[", "]"]
    whitespace = ["\t", "\n", " "]

    return digit, posdigit, letter, type, boolean, keyword, arithmetic, comparison, brace, paren, bracket, whitespace

if __name__ == "__main__":
    digit, posdigit, letter, type, boolean, keyword, arithmetic, comparison, brace, paren, bracket, whitespace = define_lists()
    
    #Getting user input via command line arguments:
    try:
        filename = sys.argv[1]
        file_detected = os.path.isfile(filename)
    except(IndexError):
        print("IndexError: input missing, please give input file.")

    if ( file_detected ):
        
        #Opening and reading the input file:
        f = open(filename, "r")
        input_file = f.read()
        f.close()
        
        #Starting the scanner. Scanner scans the input and returns a symbol table with token names and values
        symbol_table = scanner.scan(input_file, digit, posdigit, letter, type, boolean, keyword, arithmetic, comparison, brace, paren, bracket, whitespace)
    
        #Fixing symbol_table formatting:
        headers = "Token name", "Token value"
        symbol_table_tabulated = tabulate(symbol_table, headers)
    
        #Printing the table to console for convenience:
        print("INPUT:\n", input_file)
        print("\nSYMBOL TABLE:")
        print(symbol_table_tabulated)
    
        #Writing the symbol table to a text-file:
        try:
            with open('scanner_output.txt', 'w') as f:
                f.write(symbol_table_tabulated)
            print("\nTable written to \"scanner_output.txt\".")
        #UnicodeEncodeError can happen if the minus sign (−) has been used instead of a regular line (-)
        except (UnicodeEncodeError):
            print("UnicodeEncodeError occurred.")
    else:
        print('Invalid argument')