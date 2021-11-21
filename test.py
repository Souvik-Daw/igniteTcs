from flask import Flask,session,render_template,request, redirect,url_for,g
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key=os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/",methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        session.pop('user',None)

        if request.form['password'] == 'password':
            session['user']=request.form['username']
            return redirect(url_for('abc'))
    return render_template('login.html')

@app.route("/abc",methods=['GET', 'POST'])
def abc():
    if g.user: 
        name=session['user'] 
        return render_template('test.html',name=name)   
    return redirect(url_for('home'))   

@app.route("/java",methods=['GET', 'POST'])
def java():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='java',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='java') 
        return render_template('index.html', allTodo=allTodo)
    return redirect(url_for('home'))   
    
@app.route("/cs",methods=['GET', 'POST'])
def cs():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='cs',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='cs')
        return render_template('Cs.html', allTodo=allTodo)
    return redirect(url_for('home')) 

@app.route("/others",methods=['GET', 'POST'])
def others():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='others',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='others')
        return render_template('others.html', allTodo=allTodo)
    return redirect(url_for('home')) 

@app.route("/dh",methods=['GET', 'POST'])
def dh():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='dh',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='dh')
        return render_template('Dh.html', allTodo=allTodo)
    return redirect(url_for('home')) 

@app.route("/ai",methods=['GET', 'POST'])
def ai():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='ai',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='ai')
        return render_template('AI.html', allTodo=allTodo)
    return redirect(url_for('home'))

@app.route("/python",methods=['GET', 'POST'])
def python():  
    if g.user: 
        if request.method == 'POST':
            name=session['user']
            title=request.form['title']
            subject=request.form['subject']
            todo = Todo(category='python',name=name,title=title, desc=subject)
            db.session.add(todo)
            db.session.commit()
        #allTodo = Todo.query.all()
        allTodo=Todo.query.filter_by(category='python')
        return render_template('python.html', allTodo=allTodo)
    return redirect(url_for('home'))

@app.route('/<id>',methods=['GET', 'POST'])
def subject(id):
    if request.method == 'POST':
            name=session['user']
            subject=request.form['subject']
            todo = Todo(category=id,name=name,title='title', desc=subject)
            db.session.add(todo)
            db.session.commit()
    allTodo1=Todo.query.filter_by(category=id)
    allTodo=Todo.query.filter_by(sno=id)
    return render_template('custom.html', allTodo=allTodo,allTodo1=allTodo1)

@app.before_request
def before_request():
    g.user=None

    if 'user' in session:
        g.user=session['user']

@app.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('login.html')

@app.route("/contactus")
def contactus():
    return render_template('contactus.html')

@app.route("/aboutus")
def aboutus():
    return render_template('about.html')

if __name__ == "__main__":
   app.run(debug=True, port=8000)  


    
    
