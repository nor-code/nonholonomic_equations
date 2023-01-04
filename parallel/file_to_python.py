map_file_expression = {
    1: ["./expression/expression1.py", "expand_expression1.txt"],
    2: ["./expression/expression2.py", "expand_expression2.txt"],
    3: ["./expression/expression3.py", "expand_expression3.txt"],
    4: ["./expression/expression4.py", "expand_expression4.txt"],
    5: ["./expression/expression5.py", "expand_expression5.txt"],
    7: ["./expression/expression7.py", "expand_expression7.txt"],
}

for i in [1, 2, 3, 4, 5, 7]:
    with open(map_file_expression[i][0], '+w') as exp:
        exp.write()
