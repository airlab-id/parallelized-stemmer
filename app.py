from components import main

def input_cmd():
    input_query = input("String to stemm: ")
    str_input = str(input_query)
    result_stem = main.Stem(str_input)
    print("result: " + result_stem)