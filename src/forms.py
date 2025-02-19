from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo,Email

class registerForm(FlaskForm):
    fullname = StringField("Escribe tu nombre", validators=[
        DataRequired(),
        Length(min=8,max=35)
    ])
    email = EmailField("Correo Eletronico", validators=[
        DataRequired(),
        Length(min=8,max=30),
        Email()
    ])
    password = PasswordField("Contraseña", validators=[
        DataRequired(),
        Length(min=6, max=8),
        EqualTo("confirme")
    ])
    confirme = PasswordField("Repite la contraseña", validators=[
        DataRequired(),
        Length(min=6,max=8)
    ])
    submit = SubmitField("Registrarse")

class loginForm(FlaskForm):

    email = EmailField("Correo Eletronico", validators=[
    DataRequired(),
    Length(min=8,max=30),
    Email()
    ])

    password = PasswordField("Confirma Contraseña", validators=[
        DataRequired(),
        Length(min=6, max=8),
    ])

    submit = SubmitField("Iniciar sesion")

class contactsForm(FlaskForm):
    fullname = StringField("Nombre contacto:", validators=[
        DataRequired(),
        Length(min=4,max=13)
    ])    
    telefono = StringField("Numero contacto:",validators=[
        DataRequired(),
        Length(min=3,max=9)
    ])
    submit = SubmitField("agregar")

class editcontactsForm(FlaskForm):
    fullname = StringField("Nombre contacto:", default="", validators=[
        DataRequired(),
        Length(min=4,max=13)
    ])    
    telefono = StringField("Numero contacto:", default="",validators=[
        DataRequired(),
        Length(min=3,max=9)
    ])
    submit = SubmitField("modificar")