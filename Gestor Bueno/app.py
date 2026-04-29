app.route("/")
def home():
    return render_template("login.html")

# REGISTRO
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users_collection.find_one({"username": username}):
            return redirect(url_for("register"))

        hashed_password = bcrypt.hash(password)
        users_collection.insert_one({
            "username": username,
            "password": hashed_password
        })

        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if users_collection.find_one({"username": username}):
            return register_html() + "<p>Usuario ya existe</p>"

        hashed_password = bcrypt.hash(password)

        users_collection.insert_one({
            "username": username,
            "password": hashed_password
        })

        return redirect("/")

    return register_html()

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = users_collection.find_one({"username": username})

    if not user or not bcrypt.verify(password, user["password"]):
        return login_html("Datos incorrectos")

    return login_html("Login exitoso")






if __name__ == "__main__":
    app.run(debug=True)