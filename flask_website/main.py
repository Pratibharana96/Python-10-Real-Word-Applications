from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
from flask_mail import Mail

# loading all the config data in param variable and pasiing it to the jinja template 
with open('config.json','r') as c:
    params = json.load(c)["params"]
local_server = True
app=Flask(__name__)
# for sending mail with gmail using flask mail
app.config.update (
                MAIL_SERVER= 'smtp.gmail.com',
                MAIL_PORT= '465',
                MAIL_USE_SSL=True,
                MAIL_USERNAME= params['gmail_user'],
                MAIL_PASSWORD= params['gmail_password']
)
mail = Mail(app)
# check if it local url or production url for database connectivity
if (local_server):
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']


db = SQLAlchemy(app)

# sno name email phone_num msg date 
# make contact class save contact data to db
class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(12),nullable=True)
    msg = db.Column(db.String(20),  nullable=False)
# make posts class to fetch posts data
class Posts(db.Model):
    sno=db.Column(db.Integer, primary_key=True) 
    title=db.Column(db.String(80),nullable=False)
    content=db.Column(db.String(120),nullable=False)
    date=db.Column(db.String(80),nullable=True)
    slug=db.Column(db.String(21),nullable=False)
    img_file=db.Column(db.String(21),nullable=False)

@app.route('/')
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_posts']]
    return render_template("index.html",params=params,posts=posts)

@app.route('/contact', methods =['GET','POST'])
def contact():
    if(request.method == 'POST'):
        ''' add entry to the database'''
        name= request.form.get('name')
        email= request.form.get('email')
        phone= request.form.get('phone')
        message= request.form.get('message')
       # sno name email phone_num msg date 
        entry = Contacts(name =name,email =email,phone_num = phone ,date = datetime.now() ,msg= message)
        db.session.add(entry)
        db.session.commit()
        # after commiting data to db now send mail using gmail
        mail.send_message('Hey Pratibha Got New Message From' +name,
        sender=email,
        recipients=[params['gmail_user']],
        body = message + "\n" +phone
        )


        # admin = User(username='admin', email='admin@example.com')
        # guest = User(username='guest', email='guest@example.com')
        
    return render_template("contact.html",params=params)


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('blog.html', params=params, post=post)




if __name__ == "__main__":
    app.run(debug=True)

 