from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 1. git status
# 2. git add .
# 3. git commit -m "bich u ch hamaagui"
# 4. git push -u origin main

@app.route('/zoloo')
def hello_zoloo():
    return 'Hello, Zoloo! added some test'

@app.route('/form', methods=['GET', 'POST'])
def render_form():
    message = ''
    if request.method == 'POST':
        text = request.form.get('text')
        message = text.lower()
    return render_template('form.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

