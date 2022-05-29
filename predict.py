from flask_restful import Resource, reqparse
from gensim.models import KeyedVectors, Word2Vec

# model = KeyedVectors.load("models/model.pkl")
model = Word2Vec.load('models/full_grams_cbow_100_twitter.mdl')


class MostSimilarByWord(Resource):

    def post(self):
        '''Outputs the 10 most similar words from the Holy Quran,
        besides their relative similarity scores for the given word.'''

        parser = reqparse.RequestParser()
        parser.add_argument('word')

        args = parser.parse_args()  # creates dict
        word = args['word']

        out = {'results': model.most_similar(word)}

        return out, 200


# Not yet implemented
class MostSimilarByTopic(Resource):

    def post(self):
        '''Outputs the 10 most similar verses from the Holy Quran,
        besides their relative similarity scores for the given topic (one or more words).'''

        out = {'results': 'Not yet implemented'}

        return out, 200
