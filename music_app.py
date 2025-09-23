import streamlit as st
import pickle
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# 🔑 Spotify API credentials (replace with yours)
client_id = '24bc1612dee54160b21040d88a9ea982'
client_secret = 'eed167c695e84a849646829a0cce9c61'

# Setup Spotify API authentication
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 🚀 Fetch Spotify track image
def fetch_poster(music_title):
    results = sp.search(q=music_title, type='track', limit=1)
    if results['tracks']['items']:
        return results['tracks']['items'][0]['album']['images'][0]['url']
    else:
        return "https://via.placeholder.com/300"

# 🧠 Recommender logic
def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_music = []
    recommend_music_poster = []
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommend_music.append(music_title)
        recommend_music_poster.append(fetch_poster(music_title))
    return recommend_music, recommend_music_poster

# 📦 Load data
music_dict = pickle.load(open('musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)
similarity = pickle.load(open('similarities.pkl', 'rb'))

# 🎵 Streamlit UI
st.title('🎵 Music Recommendation System')
selected_music_name = st.selectbox('Select a song you like:', music['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_music_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
