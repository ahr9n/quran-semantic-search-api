from flask import Flask
from flask_restful import Api
from predict import MostSimilarByWord, MostSimilarByTopic

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

api = Api(app)

# routes to apis 
api.add_resource(MostSimilarByWord, '/similar-word')
api.add_resource(MostSimilarByTopic, '/similar-topic')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
