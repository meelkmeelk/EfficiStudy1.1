from flask import Flask, render_template, request
import csv

app = Flask(__name__, static_folder='static')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        with open('feedback.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, email, message])
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)