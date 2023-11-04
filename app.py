from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #main page
def main(): 
    return render_template('index.html')


@app.route('/next')
def next_page():
    return render_template('next.html')


if __name__ == "__main__":
    app.run(debug = True)