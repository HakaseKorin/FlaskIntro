from datetime import datetime
from flask import Flask, render_template, url_for, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy

# TODO look for web host for app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Task %r>' % self.id
    
class Alarm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(17), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id
        
# Comment out after running once - creates db
#with app.app_context():
#       db.create_all()

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting that task'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

@app.route('/clock', methods=['GET'])
def clock():
    alarms = Alarm.query.all()
    return render_template('clock.html', alarms=alarms)

@app.route('/time_feed')
def time_feed():
    def generate():
        yield datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # return also will work
    return Response(generate(), mimetype='text')

@app.route('/add_alarm', methods = ['GET','POST'])
def add_alarm():
    if request.method == "POST":
        alarm_content = request.form['content']
        new_alarm = Alarm(content=alarm_content)

        try:
            db.session.add(new_alarm)
            db.session.commit()
            return redirect('/clock')
        except Exception as e:
            print("The error is ",e)
            
    else:
        return render_template('add_alarm.html')
    
@app.route('/delete_alarm/<int:id>')
def delete_alarm(id):
    target_alarm = Alarm.query.get_or_404(id)

    try:
        db.session.delete(target_alarm)
        db.session.commit()
        return redirect('/clock')
    except:
        return "There was an issue deleting that alarm"
    
if __name__ == "__main__":
    app.run(debug=True)
