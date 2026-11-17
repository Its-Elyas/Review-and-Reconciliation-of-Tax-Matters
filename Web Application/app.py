from flask import Flask, render_template


app = Flask(__name__)

import sys, os
databse_path = os.path.dirname(os.path.abspath(sys.argv[0]))


# Configure SQLite database
app.config['SECRET_KEY'] ='7b723680345c43e4c8f0711d9f3c17b77546cdb1682a83c8'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{databse_path}/database/Alarm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

from extension import db
db.init_app(app=app)


#--routes sections--#
# User

@app.route('/')
def dashboard():
    return render_template('companies.html')

















from models.models import *
with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run(
        port=8080,
        debug=True,
        )
    