import flask
from flask import request, jsonify
from flask_cors import CORS
import sqlite3
import uuid
import os
from werkzeug.utils import secure_filename
import json
import os
DATABASE = 'N_E_W.db'

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True
dataModel = ["UUID", "title", "subtitle", "text", "IMG_URL", "labels", "contact", "start", "finish", "hours", "slots"]
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

@app.route('/api/upload', methods=['POST'])
def upload_IMG():
    f = request.form['json']
    file = request.files['file']
    data = json.loads(f)
    print(data)
    filename = secure_filename(file.filename)
    #print(os.path.join("images/", filename))
    file.save(os.path.join("images/", filename))
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    dumper = "INSERT INTO Projects VALUES ('{}','{}',\
        '{}','{}','images/bangle-leaf.jpg',\
            'machine learning,software,hardware','jan@N_E_W.nl',\
                '01-09-2021', '01-12-2021', 10, 10)".format(str(uuid.uuid4()),data['title'],
                data['subtitle'],data['text'])
    print(dumper)
    cur.execute(dumper)
    db.commit()
    db.close()

    return jsonify({'Code': 200 })

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/postproject', methods=['GET'])
def pp():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    dumper = "INSERT INTO Projects VALUES ('{}','Smart',\
        'Programming, testing','testtesttest','images/bangle-leaf.jpg',\
            'machine learning,software,hardware','jan@N_E_W.nl',\
                '01-09-2021', '01-12-2021', 10, 10)".format(str(uuid.uuid4()))
    cur.execute(dumper)
    db.commit()
    db.close()
    return jsonify({'status': 200})

@app.route('/api/set', methods=['GET'])
def test():

    os.remove(DATABASE)

    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute('''CREATE TABLE Projects
               (UUID, title, subtitle, text, IMG_URL, labels, contact, start, finish, hours, slots)''')
    dumper = "INSERT INTO Projects VALUES ('{}','Smartwatch Engineer',\
        'Programming, testing','testtesttest','images/bangle-leaf.jpg',\
            'machine learning,software,hardware','jan@N_E_W.nl',\
                '01-09-2021', '01-12-2021', 10, 10)".format(str(uuid.uuid4()))
    dumper2 = "INSERT INTO Projects VALUES ('{}','Smartwatch Engineer2',\
        'Programming, testing','testtesttest','images/bangle-leaf.jpg',\
            'machine learning,software,hardware','jan@N_E_W.nl',\
                '01-09-2021', '01-12-2021', 10, 10)".format(str(uuid.uuid4()))
    print(dumper)
    cur.execute(dumper)
    
    db.commit()
    cur.execute(dumper2)
    db.commit()
    db.close()
    return jsonify(books)

@app.route('/api/get', methods=['GET'])
def test2():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    f = []
    for row in cur.execute('SELECT * FROM Projects'):
        ab = {}
        for x,y in zip(dataModel, row):
            if x == 'labels':
                y = y.split(',')
                print('okeee')
            ab[x] = y
        f.append(ab)
    db.commit()
    db.close()
    print(row)
    print(dataModel)
    print(f)
    return jsonify(f)

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