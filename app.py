from flask import Flask, render_template, request, redirect, url_for
from models import Student, session
app = Flask(__name__)


@app.route('/index')
def index():
    students = session.query(Student).all()
    return render_template('index.html', students=students)


@app.route('/details/<int:id>')
def details(id):
    s = session.query(Student).get(id)
    return render_template('details.html', s=s)


@app.route('/delete/<int:id>')
def delete(id):
    s = session.query(Student).get(id)
    return render_template('delete.html', s=s)


@app.route('/update', methods=['GET', 'POST'])
def update(id):
    st = session.query(Student).get(id)
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        st.name = n
        st.email = e
        session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', st=st)


@ app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        n = request.form['name']
        e = request.form['email']
        new_st = Student(name=n, email=e)
        session.add(new_st)
        session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')


@ app.route('/accounts')
def accounts():
    return render_template('accounts.html')


@ app.route('/posts')
def posts(): return render_template('posts.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
