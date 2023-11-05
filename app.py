from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

@app.route('/') #main page
def main(): 
    return render_template('index.html')


@app.route('/receive_form_data', methods=['POST'])
def receive_form_data():
    data = request.json  # This contains the data sent from the front end
    print(data)  # You can process the data here as needed
    return jsonify({"response": "Form data received!", "receivedData": data})


@app.route('/one')
def court1():
    return render_template('one.html')

@app.route('/two')
def court2():
    return render_template('two.html')

@app.route('/three')
def court3():
    return render_template('three.html')

@app.route('/four')
def court4():
    return render_template('four.html')

@app.route('/five')
def court5():
    return render_template('five.html')

@app.route('/six')
def court6():
    return render_template('six.html')

if __name__ == "__main__":
    app.run(debug = True)