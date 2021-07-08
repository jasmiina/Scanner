# Scanner
The program scans given input and returns a symbol table with the found token names and values.
Currently the program recognizes simple Java code provided in a text file.

How to run:
(Note: The module "tabulate" needs to be installed, it can be installed by using pip with the command "python -m pip install tabulate")
The program can be run from command line with the command "python lexical_analyzer.py <file-name.txt>" (the format of the command can depend on the installed Python version and operating system). The test file "input.txt" is provided for testing the program. After scanning is done, the outputted symbol table is saved to "scanner_output.txt".
