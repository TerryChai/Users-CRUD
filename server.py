from flask import Flask, render_template, request, redirect

from users import Users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

# MAIN #
@app.route('/users')
def users():
    return render_template("users.html", users=Users.get_all())

# NEW USER PAGE #
@app.route('/users/new')
def new():
    return render_template("new_user.html")

# ADD NEW USER #
@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    Users.save(request.form)
    return redirect('/users')

# EDIT USER INFO #
@app.route('/user/edit/<int:id>')
def edit(id):
    data ={
        "id":id
    }
    return render_template("edit_user.html", user=Users.get_one(data))

# SHOWS USER'S INFO IN A DIFFERENT PAGE #
@app.route('/user/show/<int:id>')
def show(id):
    data ={
        "id":id
    }
    return render_template("show_user.html", user=Users.get_one(data))

@app.route('/user/update', methods=['POST'])
def update():
    Users.update(request.form)
    return redirect('/users')

# DESTROY/DELETE USER #
@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        "id": id
    }
    Users.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)