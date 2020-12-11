from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maternity-leave.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# this set's up our db connection to our flask application
db = SQLAlchemy(app)

# this is our model (aka table)
class MaternityLeave(db.Model):
    __tablename__ = "Maternity Leave By Country"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(255), nullable=False)
    weeks_paid = db.Column(db.Float, nullable=False)
    payment_rate = db.Column(db.Float, nullable=False)
    population_2020 = db.Column(db.Integer, nullable=False)
    

@app.route('/', methods=['GET'])
def index():
    table = MaternityLeave.query.all()
    return render_template('index.html', data=table)

# include other views that return html here:
@app.route('/other')
def other():
    return render_template('other.html')

# set up the following views to allow users to make
# GET requests to get your data in json
# POST requests to store/update some data
# DELETE requests to delete some data
@app.route('/api', methods=['GET'])
def get_data():
    table = MaternityLeave.query.all()
    d=[]
    for row in table:
        row_as_dict = {
            #should I include row.id?
            "country": row.country,
            "weeks paid": row.weeks_paid,
            "payment rate": row.payment_rate,
            "population 2020": row.population_2020,
        }
        d.append(row_as_dict)
    return jsonify(d)

#this will allow users to add/update data
@app.route('/api', methods=['POST'])
def add_data():
    #added = {}
    for k,v in request.args.items():
        if not k in d.keys():
            d[k] = v
    return jsonify({"added": request.args, "current": d})
#     if request.method == 'POST':
#         print(request.form)
#         for k,v in request.args.items():
#             print(k,v)
#         return jsonify({})
        
#this will allow the deletion of data
@app.route('/api', methods=['DELETE'])
def delete_data():
    for k,v in request.args.items():
        try:
            d.pop(k)
            deleted[k] = v
        except:
            continue
    return jsonify({"deleted": deleted, "current": d})



if __name__ == '__main__':
    app.run(debug=True)