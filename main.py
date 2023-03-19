from flask import Flask, render_template, request
import os

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        subject = request.form['subject']
        duration = request.form['duration']
        print(f"Received subject: {subject} and duration: {duration}")
        with open('notes.txt', 'a') as file:
            file.write(f"{subject}, {duration}\n")
          
    with open('notes.txt', 'r') as file:
        notes = [line.strip().split(',') for line in file.readlines()]
    return render_template('index.html', notes=notes)
  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
  