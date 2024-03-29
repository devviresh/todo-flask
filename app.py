from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join('todo.db')

print('evv: ',os.environ.get('DATABASE_URL'))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(400), nullable=False)
    date_created=db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title} - {self.desc}"
        # return super().__repr__()



@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method=='POST':
        title=request.form['title']
        desc=request.form['desc']
        todo =Todo(title=title,desc=desc)
        db.session.add(todo)
        db.session.commit()
    all_todo = Todo.query.all()
    # print(all_todo)
    return render_template('index.html',alltodo=all_todo)
    # return 'Hello, Viresh!'



@app.route('/show')
def home_go():
    all_todo = Todo.query.all()
    print(all_todo)
    return 'Welcome to home!'




@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    print(todo)
    return redirect('/')




@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method == 'POST':
        print('post')
        title=request.form['title']
        desc=request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    
    todo = Todo.query.filter_by(sno=sno).first()
    db.session

    return render_template('update.html',todo=todo)

# if __name__ == "__main__":
#     app.run(debug=True)