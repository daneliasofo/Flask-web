from flask import Flask, render_template, request, flash, redirect, url_for
from forms.registration_form import RegistrationForm

app = Flask(_Qoutes_)

Quotes_list = [
    "თუ ერთ ადამიანს მაინც აქვს შენი იმედი, საკმარისია იმისთვის, რომ არ დანებდე.","როცა საკუთარი თავის მარტო გადარჩენას ისწავლი, შეუძლებელს შეძლებ.","სიკეთეს შენი სიამოვნებისთვის უნდა აკეთებდე და არა სხვის დასანახად."
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/Quotes")
def Quotes():
    return render_template("Quotes.html", Quotes=Quotes_list)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.username.data, form.email.data, form.password.data)
        flash("Thanks for registering")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)

print(_Qoutes_)

if _Qoutes_ == "_main_":
    app.run(debug=True)
