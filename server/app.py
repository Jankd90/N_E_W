import flask
from flask import request, jsonify
import sqlite3
import uuid
DATABASE = 'N_E_W.db'

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]




@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/set', methods=['GET'])
def test():
    import os
    os.remove(DATABASE)

    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute('''CREATE TABLE Projects
               (UUID, Title, Subtitle, Text, IMG_URL, Labels, Contact, Start, Finish, Hours, Slots)''')
    dumper = "INSERT INTO Projects VALUES ('{}','Smartwatch Engineer',\
        'Programming, testing','testtesttest','images/bangle-leaf.jpg',\
            '[machine learning, software, hardware]','jan@N_E_W.nl',\
                '01-09-2021', '01-12-2021', 10, 10)".format(str(uuid.uuid4()))
    print(dumper)
    cur.execute(dumper)
    db.commit()
    db.close()
    return jsonify(books)

@app.route('/api/get', methods=['GET'])
def test2():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    for row in cur.execute('SELECT * FROM Projects'):
        print(row)
    db.commit()
    db.close()
    return jsonify(books)

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)