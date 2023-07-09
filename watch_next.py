import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import KeyedVectors

def load_movie_descriptions(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_most_similar_movie(description, movie_descriptions, word_vectors):
    # Convert the input description into a word vector
    words = description.split()
    input_vector = np.mean([word_vectors[word] for word in words if word in word_vectors], axis=0)

    # Compute the cosine similarity between the input description and all movie descriptions
    similarities = cosine_similarity(input_vector.reshape(1, -1), movie_descriptions)[0]

    # Find the index of the most similar movie
    most_similar_index = np.argmax(similarities)

    # Return the title of the most similar movie
    return most_similar_index

# Path to the file containing movie descriptions
file_path = 'movies.txt'

# Load all movie descriptions from the file
movie_descriptions = load_movie_descriptions(file_path)

# Load pre-trained word vectors (e.g., using Word2Vec)
word_vectors = KeyedVectors.load_word2vec_format('word_vectors.bin', binary=True)

# Description of the movie "Planet Hulk"
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# Get the index of the most similar movie
most_similar_index = get_most_similar_movie(description, movie_descriptions, word_vectors)

# Get the title of the most similar movie
most_similar_movie = movie_descriptions[most_similar_index]

print(f"The most similar movie is: {most_similar_movie}")
