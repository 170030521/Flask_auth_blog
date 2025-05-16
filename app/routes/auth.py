from flask import request,session,render_template,url_for,redirect,flash
from app import app
from app.models import db,User,Blog
from datetime import timedelta
from app.routes.blog import view_all_blogs

app.secret_key="secret key"
app.permanent_session_lifetime = timedelta(minutes=5)
# session.permanent = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def view():
    return "you are in the right track"
        
@app.route("/register",methods=["GET"])  
def register_get():
    return render_template("register.html")    
 
@app.route('/register', methods=['POST'])
def register_post():
    name=request.form["name"]
    email=request.form["email"]
    age=request.form["age"]

    if db.session.query(User).filter_by(email=email).first():
        flash("Email already exists","error")
        return redirect(url_for("register_get"))
    else:
        session.permanent = True
        session["name"] = name
        session["age"] = age
        session["email"] = email

        user=User(name=name,email=email,age=age)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login_get"))

@app.route("/login",methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_post():
    name=request.form["name"]
    email=request.form["email"]

    if db.session.query(User).filter_by(name=name,email=email).first():
        session["name"] = name
        session["email"] = email
        flash("You are successfully logged in","success")
        return redirect(url_for("view_get"))
            
    else:
        flash("Invalid username or email","error")
        return redirect(url_for("login_get"))

@app.route("/view",methods=["GET"])  
def view_get():
    return render_template("layout1.html")

@app.route("/view",methods=["POST"])
def view_post():
    name=request.form["name"]
    title=request.form["title"]
    content=request.form["content"]

    blog=Blog(name=name,title=title,content=content)
    db.session.add(blog)
    db.session.commit()    
    return redirect(url_for("view_all_blogs"))      

def logout():
    session.clear()
    return redirect(url_for("login"))


    
