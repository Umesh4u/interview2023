from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
import secrets


secret_key = secrets.token_hex(16)
app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/flask_app_new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, unique=True,primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(80))

admin = Admin(app, name='Admin Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, db.session))

@app.route('/user/login', methods=['GET'])
def index():
    users = User.query.all()
    user_list=[]
    for user in users:
        user_data={
            'id':user.id,
            'user_name':user.user_name,
            'password':user.password
        }
        user_list.append(user_data)

    return jsonify({'users': user_list})


if __name__ == '__main__':
    app.run(debug=True)