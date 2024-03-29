from typing import Callable
from models import Post
import streamlit as st 
import datetime

class AddPostView:
    def __init__(self, add_post_func:Callable[[Post],bool]):
        user_name_text = st.text_input("Displayed name?")
        post_text = st.text_input("Whats in your mind?")
        clicked = st.button("Post")
        if clicked:
            post = Post(
                creator_name=user_name_text,
                content=post_text,
                posting_date=datetime.datetime.now()
            )
            
            did_add = add_post_func(post)
            
            if did_add:
                st.success("Post added!")
            else:
                st.error("Error adding post")