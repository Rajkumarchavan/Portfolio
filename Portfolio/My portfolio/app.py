from flask import Flask, render_template
app =Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title = home)


@app.route("/about")
def about():
    return render_template("about.html",title = about)

@app.route("/contact")
def contact():
    return render_template("contact.html",title = contact)

@app.route("/projects")
def projects():
    return render_template("projects.html",title = projects)

if __name__ == "__main__":
    app.run(debug=True)
