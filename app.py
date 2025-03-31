import streamlit as st

# getting posters from tmdb
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9584edeed0cecc4ecf3d4930f0197bc8&language=en-US".format(movie_id)
    # Using postman -> interact with API
    # Using observation, poster in 'poster_path'
    # Needs to be converted to json before using
    data = requests.get(url).json()
    poster = data['poster_path']
    link = "https://image.tmdb.org/t/p/w500/" + poster
    # link = "https://api.themoviedb.org/" + poster -> wrong link
    return link

# loading data sets using pickle
import pickle
movies = pickle.load(open("movies_list.pk1",'rb'))
sim = pickle.load(open("similarity.pk1",'rb'))

# using streamlit for UI
st.header("Movie Recommender System")

# choosing movie titles
movies_list = movies['title'].values

# making it more presentable
import streamlit.components.v1 as components
imageCarouselComponent = components.declare_component("image-carousel-component", path="movie_images/public")
imageUrls = [
    fetch_poster(1632),
    fetch_poster(299536),
    fetch_poster(17455),
    fetch_poster(2830),
    fetch_poster(429422),
    fetch_poster(9722),
    fetch_poster(13972),
    fetch_poster(240),
    fetch_poster(155),
    fetch_poster(598),
    fetch_poster(914),
    fetch_poster(255709),
    fetch_poster(572154)
    ]
imageCarouselComponent(imageUrls=imageUrls, height=200)

# dropdown list
val = st.selectbox("Select movie", movies_list)

#the main engine function for recommendations
def recommend(movie):
    #movie -> title of the movie searched
    index = movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(sim[index])), reverse=True, key = lambda vector:vector[1])
    recom_list = []
    recom_poster = []
    for i in distance[1:6]:
        recom_list.append(movies.iloc[i[0]].title)
        recom_poster.append(fetch_poster(movies.iloc[i[0]].id))
    return recom_list, recom_poster

# recommendation button for result display with poster
if st.button('Show recommendation'):
    movies_recommended, poster = recommend(val)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movies_recommended[0])
        st.image(poster[0])
    with col2:
        st.text(movies_recommended[1])
        st.image(poster[1])
    with col3:
        st.text(movies_recommended[2])
        st.image(poster[2])
    with col4:
        st.text(movies_recommended[3])
        st.image(poster[3])
    with col5:
        st.text(movies_recommended[4])
        st.image(poster[4])


