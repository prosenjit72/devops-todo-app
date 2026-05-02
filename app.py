from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database — Docker Compose দিলে PostgreSQL, না হলে SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 'sqlite:///todos.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database table — প্রতিটা Todo এর structure
class Todo(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Home — সব todo দেখাও
@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# নতুন todo add
@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        db.session.add(Todo(task=task))
        db.session.commit()
    return redirect('/')

# Done/Undone toggle
@app.route('/toggle/<int:id>')
def toggle(id):
    todo = Todo.query.get_or_404(id)
    todo.done = not todo.done
    db.session.commit()
    return redirect('/')

# Delete
@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)