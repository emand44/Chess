from flask import Flask, jsonify
from Bræt import Skakbræt

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_board')
def get_board():
    bræt = Skakbræt()
    # Konverter brættet til en JSON-venlig format
    def brik_repr(brik):
        return {
            'farve': brik.farve,
            'navn': brik.navn
        } if brik else None

    bræt_repr = [[brik_repr(brik) for brik in række] for række in bræt.bræt]
    return jsonify(bræt_repr)

if __name__ == '__main__':
    app.run(debug=True, port=5500)
