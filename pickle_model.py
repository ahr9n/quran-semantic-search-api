from gensim.models import KeyedVectors, Word2Vec

# Download aravec_3_twitter vectors: https://archive.org/download/full_grams_cbow_300_twitter
# Then, load the vectors directly from the file.

# NOTE: Only 1m out of vectors loaded to speed up the model performance
model = KeyedVectors.load_word2vec_format(
    'data/ksucca_full_cbow.bin', binary=True, limit=1000000)


# Pickle the model
model.save("models/model.pkl")