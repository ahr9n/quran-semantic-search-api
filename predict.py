from flask_restful import Resource, reqparse
from gensim.models import KeyedVectors, Word2Vec
import helpers

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

        word = helpers.clean_str(word).replace(" ", "_")
        if word in model.wv:
            most_similar = model.wv.most_similar(word, topn=10)
            for term, score in most_similar:
                term = helpers.clean_str(term).replace(" ", "_")
            return {'results': most_similar}, 200
        else:
            return {'results': 'Word not found'}, 404


# Not yet implemented
class MostSimilarByTopic(Resource):

    def post(self):
        '''Outputs the 10 most similar verses from the Holy Quran,
        besides their relative similarity scores for the given topic (one or more words).'''

        out = {'results': 'Not yet implemented'}

        return out, 200
