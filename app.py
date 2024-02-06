"""Flask app for Cupcakes"""

import os
from flask import Flask, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", 'postgresql:///cupcakes')

connect_db(app)


@app.get("/api/cupcakes")
def list_all_cupcakes():
    """ Get data about all cupcakes Respond with JSON like: {cupcakes:
    [{id, flavor, size, rating, image_url}, ...]}
    """

    cupcakes = Cupcake.query.all()
    # for cupcake in cupcakes:
    #     print(cupcake)
    #     print(cupcake.serialize())
    serialized = [cupcake.serialize() for cupcake in cupcakes]
    print("cupcakes serialized!:",serialized)

    #serialized = [c.serialize() for c in cupcakes]
    #return jsonify(cupcakes)
    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<id>")
def get_cupcake(id):
    """
        This is a dope docstring
    """
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())