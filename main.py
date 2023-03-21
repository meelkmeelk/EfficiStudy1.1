from flask import Flask, render_template, request
from datetime import timedelta

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

    total_duration = sum(int(note[1]) for note in notes)
    total_duration_hours = total_duration // 60 

    goal_met = total_duration_hours >= len(notes)

    return render_template('index.html', notes=notes, total_duration=timedelta(minutes=total_duration), goal_met=goal_met)


@app.route('/contact', methods=['GET', 'POST'])
def newfile():
    return render_template('contact.html')

@app.route('/contact-submit', methods=['POST'])
def contact_submit():
    if request.method == 'POST':
        feedback = request.form['feedback']
        with open('feedback.txt', 'a') as file:
            file.write(f"{feedback}\n")
        return render_template('thanks.html')
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=81)


   