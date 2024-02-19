from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/special')
def special():
    return render_template('special.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/chefs')
def chefs():
    return render_template('chefs.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/reserve')
def reserve():
    return render_template('reserve.html')



if __name__ == '__main__':
    app.run(debug=True)
