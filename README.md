# MOVIE RECOMMENDATION SYSTEM

I have used the [TMDB dataset](https://www.kaggle.com/datasets/ahsanaseer/top-rated-tmdb-movies-10k) for collection of 10,000 movies with some basic parameters like <br>
- overview
- genre
- popularity <br> <br>

> I have used a content-based movie recommendation system and therefore, **no search history** was used. <br><br>

Here, a file named `similarity.pk1` from pickle has not been included due to its size being 700MB. <br>
It contained a 10,000x10,000 matrix storing all possible vector combinations for search values. <br> <br>

The front-end is incredibly basic, done using `streamlit` <br>
Next basic additions planned<br>
- Image leads to the IMDB website of the movie for details
- Changing to new [dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) to include actors, directors, production houses to better align similarity_scores

Regards,<br>
Sunny Gogoi.
