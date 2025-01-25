"""
A Flask-based calculator app that supports arithmetic operations
(addition, subtraction, multiplication, and division) via GET requests.
"""

from flask import Flask, request

app = Flask(__name__)

"""
Handles artihmetic operations: 
addition, subtraction, multiplication adn division 
using parameters through GET reqest
Returning: string with chosen operation and a result
"""
@app.route('/calculate')
def calculate():
    """obsluga oeracji artymetycznych"""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op == 'sum':
        result = arg1 + arg2
    elif op == 'sub':
        result = arg1 - arg2
    elif op == 'mul':
        result = arg1 * arg2
    elif op == 'div':
        if arg2 != 0:
            result = arg1 / arg2
        else:
            return "Error: Zero division", 400
    else:
        return "Error: No operation possible", 400

    return f'<b>{arg1} {op} {arg2} = {result}</b>'

if __name__ == "__main__":
    app.run()
