from flask import Flask, render_template, request, jsonify, flash, redirect, url_for

# import fucntion from app
import app as service
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or 'default_secret_key_if_not_set'


# Route untuk Home
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    res, err = service.loginWithApi(username, password)
    print(f"res: {res}, err: {err}")  

    if err is not None:
        flash(f"{err}")
        return redirect(url_for("index"))
    elif res and len(res) > 0 and err is None:
        return redirect(url_for("dashboard"))
    else:
        flash("Login failed, please try again.")
        return redirect(url_for("index"))

@app.route("/form-register")
def form_register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    nama = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    
    res, err = service.registerwithApi(nama, username, password)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("index"))
    elif res:
        flash("register berhasil")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("register"))

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        res, err = service.hapusData(id)
        if err is not None:
            return jsonify({"error": str(err)}), 400
        elif res:
            return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/form-update/<int:id>", methods=["GET"])
def formUpdate(id):
    res, err = service.getDataId(id)
    if err is not None:
        flash(f"{err}")
        return redirect(url_for("dashboard"))
    print(res)

    user_data = {
        "id": res.get("id"),
        "nama": res.get("nama"),
        "jabatan": res.get("jabatan"),
        "department": res.get("department")
    }

    return render_template("form_update.html", user=user_data)

@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    id = request.form.get("id")
    nama = request.form.get("nama")
    jabatan = request.form.get("jabatan")
    department = request.form.get("department")
    
    res, err = service.updateData(id, nama, jabatan, department)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("formUpdate", id=id))
    elif res:
        flash("update berhasil")
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("dashboard"))

@app.route("/tambah-data")
def tambah_data():
    return render_template("tambah_data.html")


@app.route("/tambah", methods=["POST"])
def tambah():
    nama = request.form.get("name")
    jabatan = request.form.get("jabatan")
    department = request.form.get("department")
    
    res, err = service.tambahData(nama, jabatan, department)
    if err != None:
        flash(f"{err}")
        return redirect(url_for("tambah-data"))
    elif res:
        flash("data berhasil ditambahkan")
        return redirect(url_for("dashboard"))
    else:
        return redirect(url_for("tambah-data"))
    

@app.route("/dashboard")
def dashboard():
    res, err = service.getData()
    if err is not None:
        flash(f"{err}")
        return redirect(url_for("index"))
    
    for data in res:
        print(data)
    
    datas = [
        {"id": data.get("id"), "nama":data.get("nama"), "jabatan": data.get("jabatan"), "department": data.get("department")}
        for data in res
    ]
    return render_template("dashboard.html", data = datas)

if __name__ == '__main__':
    app.run(debug=True)
