from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('about.html')

@app.route('/stacks')
def stacks():
    return render_template('stacks.html')

@app.route('/certificate')
def certificate():
    return render_template('certificate.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)


