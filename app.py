from flask import Flask
from flask_restful import Api
from predict import MostSimilarWord, MostSimilarVerse

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

api = Api(app)

# routes to apis 
api.add_resource(MostSimilarWord, '/similar-word/<string:word>')
api.add_resource(MostSimilarVerse, '/similar-verse/<string:query>')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
