from flask import render_template, url_for, flash, redirect
# from city.forms import TopCities
# from city.__init__ import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instance of the Flask class
app = Flask(__name__)
app.config.from_mapping(
            SECRET_KEY = 'it-dont-matter'
            )


top_cities =["Paris","London", "Rome","Tahiti"]
name = 'Youhao Chen'

@app.route("/", methods=['GET', 'POST'])
@app.route("/home/", methods=['GET', 'POST'])

def home():
    
    form = TopCities()
    
    if form.validate_on_submit():
        flash(f'Form Submitted for {form.city_name.data}!',category='success')
        return redirect(url_for('home'))
    
    return render_template("home.html",
            title = title,
            name = name,
            form =form)
if __name__ == "__main__":
    app.run()

