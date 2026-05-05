from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    msg = ""
    name = ""
    age = ""
    email = ""

    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        email = request.form.get("email")

        if name == "" or age == "" or email == "":
            msg = "Fill all data!"
        else:
            msg = "Data submitted successfully!"

    return render_template("home.html", name=name, age=age, email=email, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
