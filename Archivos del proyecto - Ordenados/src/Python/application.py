# docs @ http://flask.pocoo.org/docs/1.0/quickstart/

from flask import Flask, jsonify, request, render_template, redirect, url_for, request, make_response
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_json())  # parse as JSON

        answer =make_response(jsonify({"message": "Que rico"}),200)

        return answer

    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

@app.route('/test')
def test_page():
    # look inside `templates` and serve `index.html`
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app on port 5000 in debug mode