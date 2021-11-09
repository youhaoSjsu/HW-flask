
# from city import app
import flask


app =flask.Flask(__name__,template_folder="city")
@app.route("/")
def hello():
    return render_template('base.html')

if __name__ == "__main__":
    app.run()

