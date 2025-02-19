from flask import Flask,redirect,render_template,url_for,request,flash
from flask_mysqldb import MySQL
from flask_login import LoginManager,login_user,current_user,login_required,logout_user
from flask_wtf.csrf import CSRFProtect
# Importaciones de los py
from config import config
from forms import registerForm, loginForm, contactsForm, editcontactsForm
from models.ModelUser import ModelUser
from models.entities.User import User
import smtplib

app = Flask(__name__)

db = MySQL(app)

csrf = CSRFProtect()

login_manager_app = LoginManager(app)

def sendEmail(email):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("voyexplotar281024@gmail.com","wxzy ipjy spbp higo")
    message = "Subjet: Flask-Contacts\n\n"
    server.sendmail("voyexplotar281024wgmail.com", email,message)
    server.quit()
    print("Correo enviado con exito")
    return "enviado el correo"

# funcion gestionar si el usuario esta con la iniciar sesion esta activa
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db,id)

# funcion para login y mostrar formulario de login
@app.route("/", methods=["GET","POST"])
def login():
    form = loginForm()

    if request.method == "POST" and form.validate():
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User(0,email,password,"")
        
        logged_user = ModelUser.login(db,user)

        if logged_user:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for("contacts"))
            else:
                flash("Valido Contraseña")
                return render_template("login.html")
        else:
            flash("Correo no valido")
    
    if request.method == "GET":
        return render_template("login.html", form=form)
    
    else:
        if current_user.is_authenticated:
            redirect(url_for("contacts"))

# funcion para mostar el register y hacer el register
@app.route("/register", methods=["GET","POST"])
def register():
    form = registerForm()
    if request.method == "POST":
        email = request.form.get("email")
        fullname = request.form.get("fullname")
        password = request.form.get("password")

        user = User(0, email, password, fullname)
        ModelUser.register(db,user)
        sendEmail(email)
        return redirect(url_for("contacts"))
    if request.method == "GET":
        return render_template("register.html",form=form)
    else:
        if current_user.is_authenticated:
            redirect(url_for("contacts"))
    

#funcion para los formularios
@app.route("/contacts", methods=["GET"])
@login_required
def contacts():
    form = contactsForm()
    data =  ModelUser.getcontacts(db,current_user.id)

    if data:
        return render_template("contacts.html", form=form, data=data)
    else:
        return render_template("contacts.html", form=form)

@app.route("/addcontact", methods=["POST"])
@login_required
def addcontacts():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        telefono = request.form.get("telefono")
        
        ModelUser.addcontacts(db,fullname,telefono,current_user.id)
        flash("añadido correctamente {}".format(fullname))
        return redirect(url_for("contacts"))

@app.route("/edit/<string:id>", methods=["GET"])
@login_required
def edit(id):
    form = editcontactsForm() 
    
    cur = db.connection.cursor()
    cur.execute("SELECT * from contacts WHERE id= %s",(id,))
    datos = cur.fetchone()
    valores = {"fullname": datos[1], "telefono": datos[2]}
    form.process(data=valores)
    
    return render_template("update.html",form=form, contacts=datos)

@app.route("/update/<string:id>", methods=["POST"])
@login_required
def update(id):
    if request.method == "POST":
        fullname = request.form.get("fullname")
        telefono = request.form.get("telefono")

        cur = db.connection.cursor()
        cur.execute("UPDATE contacts SET fullname = %s, number = %s WHERE id= %s",(fullname,telefono,id))
        db.connection.commit()

        return redirect(url_for("contacts"))
    
@app.route("/delete/<string:id>")
@login_required
def delete(id):
    cur = db.connection.cursor()
    cur.execute("DELETE FROM contacts WHERE id = %s",(id,))
    db.connection.commit()
    return redirect(url_for("contacts"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

def status_401(error):
    return redirect(url_for("login"))

def status_404(error):
    return "<h1> Pagina no encontrada</h1>"

if __name__ == "__main__":
    app.config.from_object(config["Develop"])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()