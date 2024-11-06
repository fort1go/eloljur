from flask import Flask, render_template
app = Flask(__name__, template_folder="templates", static_folder="templates/eljur_files")

@app.route("/")
def hello():
    return render_template("eljur.html")

if __name__ == "__main__":
    app.run()