from astpretty import pprint as astpp
from pprintpp import pprint
import StringIO
import os, ast


def main():
    f = open("test.py", "r")
    source = f.read()
    n = ast.parse(source)
    astpp(n)

    tests = [func for func in n.body if type(func) == ast.FunctionDef and func.name[:5] == "test_"]
    pprint(tests)

    for test in tests:
        print write_test(test)


def write_test(test):
    output = StringIO.StringIO()
    name = test.name[:1].upper() + test.name[1:]
    output.write("func {}(t testing.T) {{\n".format(name))

    # get the expressions for the function and convert
    exprs = [expr for expr in test.body if type(expr) == ast.Expr]
    for expr in exprs:
        output.write(format_expr(expr))

    output.write("}")

    out =  output.getvalue()
    output.close()
    return out

def format_expr(expr):
    pass



"""
Thoughts

funcs.go file for storing the functions to start with
- stores all called functions and can be read in at startup
- Some kind of map python func -> go func
- ultimately want this to be the main way this tool works. function/code mappings are defined and executed, when a piece of python code isn't defined a stub is generated.

parse the imports for the code, import/lookup the modules so they can be accessed (be good to keep the namespaces seperate). When dealing with a function call this should allow us to find the code for it and parse it into an ast thus allowing an effective function stub to be generated. The consideration here is that python functions have position args and keyward args whereas go only supports positional. We want to generate legitimate go functions versus go functions that have to parse their arguments just to figure out what they are.
"""


if __name__ == "__main__":
    main()
