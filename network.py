from game2 import Layer, Network, sigmoid, relu
from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import numpy as np
l1 = Layer((10,1), None)
l2 = Layer((15,1), 'relu')
l3 = Layer((5,1), 'sigmoid')
n1 = Network([l1,l2,l3])
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route('/layers', methods=["GET","POST"])
@cross_origin()
def hello_world():
    layers = []
    for i in n1.layers:
        layers.append(i.data.size)
    if request.method == 'GET':
        return str(layers)
    elif request.method =='POST':
        n1.transfer(np.zeros(10).reshape(-1,1))
        n1.train(np.ones(5).reshape(-1,1))
        return str(n1.layers[-1].data)

app.run()


