from flask import Flask, jsonify, request, render_template
from models import db, Cupcake, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
toolbar = DebugToolbarExtension()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'JDOS'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

@app.route('/')
def show_cupcakes():
    return render_template('list-cupcakes.html')

@app.route('/api/cupcakes')
def all_cupcakes():
    cupcakes = Cupcake.query.all()
    cupcakes = [cp.serialize() for cp in cupcakes]

    return jsonify(cupcakes=cupcakes)

@app.route('/api/cupcakes/<int:cp_id>')
def cupcake(cp_id):
    cupcake = Cupcake.query.get_or_404(cp_id)

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    res = request.json
    cupcake = Cupcake(flavor=res['flavor'], size=res['size'], rating=res['rating'], image=res['image'])

    db.session.add(cupcake)
    db.session.commit()

    cupcake_json = jsonify(cupcake=cupcake.serialize())

    return (cupcake_json, 201)

@app.route('/api/cupcakes/<int:cp_id>', methods=['PATCH'])
def update_cupcake(cp_id):
    res = request.json
    cupcake = Cupcake.query.get_or_404(cp_id)
    cupcake.flavor = res['flavor']
    cupcake.size = res['size']
    cupcake.rating = res['rating']
    cupcake.image = res['image']

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cp_id>', methods=['DELETE'])
def delete_cupcake(cp_id):
    cupcake = Cupcake.query.filter_by(id=cp_id).delete()
    db.session.commit()

    return jsonify(msg="deleted")