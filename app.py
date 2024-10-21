import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name'] # The value is the name sent in
    message = request.form['message'] #The value will be the second name entered

    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods=['GET'])
def wave():
    name = request.form['name'] # The value is the name sent in

    return f"I am waving at {name}"


# -------------COUNT VOWELS -------

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text'] # The value is the name sent in
    vowels = 'aeiou'
    count = 0
    for letter in text:
        if letter in vowels:
            count += 1
    return f'There are {count} vowels in "{text}"'

# -------------SORT NAMES -------

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names'] # The value is the name sent in
    name_list = names.split(',')
    name_list.sort()
    return ','.join(name_list)

# -------------GET NAMES -------

@app.route('/names', methods=['POST'])
def get_names():
    name_list = ['Julia', 'Alice', 'Karim']
    add = request.form['add']
    names_to_add = add.split(',')
    for name in names_to_add:
        name_list.append(name)   
    name_list.sort()
    return ', '.join(name_list)



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

