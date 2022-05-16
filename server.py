from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)


@app.route("/users")
def index():

    users = User.get_all()
    print(users)
    return render_template("read_all.html", users=users)


@app.route('/create/user', methods=["POST"])
def create_user():

    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    user_id = User.getUserID(data)[0]['id']
    
    return redirect(f'/show/{user_id}')


@app.route('/show/<int:user_id>') 
def show(user_id):

    data = {'id' : user_id }
    
    user = User.get_one_user(data)

    print(f'========================= {user}')

    return render_template("read_one.html", user = user)


# user clicks add new user and create.html renders
@app.route("/users/new")
def new_user():

    return render_template('create.html')


# delete user button routes to this route
@app.route('/user/<int:user_id>/delete') 
def delete_user(user_id):

    data = { 'id': user_id}

    User.delete_user(data);

    return redirect('/users')


@app.route('/user/<int:user_id>/edit_page')
def edit(user_id):
    
    data = {
        'id': user_id
    }
    user = User.get_one_user(data)

    return render_template('edit.html', user = user)



@app.route('/user/<int:user_id>/edit', methods=['POST'])
def update_user(user_id):

    data = {
        'id' : user_id,
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.update(data)
    user = User.get_one_user(data)

    return redirect( ( f'/show/{user_id}' ) )



            
if __name__ == "__main__":
    app.run(debug=True)
