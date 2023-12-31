from flask import Flask, render_template, request, jsonify
import backend
import queue
import random

app = Flask(__name__)

@app.route('/') #main page
def main(): 
    return render_template('index.html')


listy = [] 
@app.route('/receive_form_data1', methods=['POST', 'GET'])
def receive_form_data1():
    Q1 = queue.Queue() 
    #global listy
    if request.method == 'POST':
        data = request.json
        listy.append(data['firstInput'])
        print(listy)
        Q1.put(data)
        return jsonify({"response": "Form data received!", "receivedData": data})
    
    elif request.method == 'GET':
        cargo = listy
        print(listy)
        print(cargo)
        return jsonify(cargo)
    

@app.route('/receive_form_data2', methods=['POST'])
def receive_form_data2():
    data = request.json  # This contains the data sent from the front end
    print(data)  # You can process the data here as needed
    return jsonify({"response": "Form data received!", "receivedData": data})

@app.route('/receive_form_data3', methods=['POST'])
def receive_form_data3():
    data = request.json  # This contains the data sent from the front end
    print(data)  # You can process the data here as needed
    return jsonify({"response": "Form data received!", "receivedData": data})


@app.route('/receive_form_data4', methods=['POST'])
def receive_form_data4():
    data = request.json  # This contains the data sent from the front end
    print(data)  # You can process the data here as needed
    return jsonify({"response": "Form data received!", "receivedData": data})

@app.route('/receive_form_data5', methods=['POST'])
def receive_form_data5():
    data = request.json  # This contains the data sent from the front end
    print(data)  # You can process the data here as needed
    return jsonify({"response": "Form data received!", "receivedData": data})

@app.route('/receive_form_data6', methods=['POST'])
def receive_form_data6():
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