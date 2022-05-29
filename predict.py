from statistics import mode
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from gensim.models import KeyedVectors, Word2Vec
import helpers

model = KeyedVectors.load("models/model.pkl")
# model = Word2Vec.load('models/full_grams_cbow_100_twitter.mdl')


class MostSimilarWord(Resource):

    def get(self, word):
        '''Outputs the 10 most similar words from the Holy Quran,
        besides their relative similarity scores for the given word.'''

        most_similar = model.most_similar(word, topn=10)

        out = []
        for term, score in most_similar:
            term = helpers.clean_str(term).replace(" ", "_")
            out.append((term, score))

        return make_response(jsonify({'results': out}), 200)


class MostSimilarVerse(Resource):

    def get(self, query):
        '''Outputs the 10 most similar words from the Holy Quran,
        besides their relative frequency scores for the given query.'''

        out = helpers.get_most_similar_verses(query, model)

        return make_response(jsonify({'results': out}), 200)