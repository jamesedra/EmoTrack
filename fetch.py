from flask import Flask, render_template, request
import api

## Create a new instance of the Flask class
app = Flask(__name__)

## Define a route for submitting the form data
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    print(f'You entered: {user_input}')
    api.getResponses(user_input)


if __name__ == '__main__':
    app.run(debug=True)