from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        name = request.form['name']
        users.append({'id': len(users) + 1, 'name': name})
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = next((u for u in users if u['id'] == id), None)
    if request.method == 'POST':
        user['name'] = request.form['name']
        return redirect(url_for('index'))
    return render_template('update.html', user=user)

@app.route('/delete/<int:id>')
def delete(id):
    global users
    users = [u for u in users if u['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


