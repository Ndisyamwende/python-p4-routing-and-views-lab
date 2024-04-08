from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # Print the string in the console
    return input_string  # Return only the string without any HTML markup

@app.route('/count/<int:num>')
def count(num):
    # Include the upper limit number in the count range
    numbers = '\n'.join(str(i) for i in range(num + 1))
    return Response(f'Numbers from 0 to {num}:\n{numbers}', content_type='text/plain')

@app.route('/math/<float:num1>/<operation>/<float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<p>Error: Division by zero.</p>'
    elif operation == '%':
        if num2 != 0:
            result = num1 % num2
        else:
            return '<p>Error: Modulo by zero.</p>'
    else:
        return '<p>Error: Invalid operation.</p>'

    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
