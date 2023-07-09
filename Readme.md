# Movie Recommendation System using Word Vector Similarity

This project is a movie recommendation system that suggests the most similar movie based on the word vector similarity of movie descriptions. It uses word embeddings to calculate the similarity between movie descriptions and provides recommendations based on that similarity.

## Getting Started

### Prerequisites

- Docker installed on your system

### Installation

1. Clone the repository to your local machine.

```shell
git clone https://github.com/photo-grammer/movies
```

2. Navigate to the project directory.

```shell
cd movie-recommendation-system
```

3. Build the Docker image using the provided Dockerfile.

```shell
docker build -t watch-next-app .
```

### Usage

1. Ensure the Docker image is built successfully.

2. Run a container from the Docker image.

```shell
docker run -it watch-next-app
```

3. The script will start running inside the Docker container and prompt you to enter a movie description. 

4. Enter the description of a movie you have watched.

5. The system will recommend the title of the most similar movie based on word vector similarity.

## Customization

If you want to use your own word vectors, you can replace the placeholder code in the `watch_next.py` script with your own or use pre-trained word vectors from sources like Word2Vec, GloVe, or fastText.

To modify the movie descriptions, add or remove movies from the `movies.txt` file.

