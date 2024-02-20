from views import FeedView,AddPostView
from services import get_feed, add_posts
import streamlit as st 

AddPostView(add_posts)
st.write("____")
FeedView(get_feed)
