import streamlit as st
import website.database as db
# from website.bot import bot

def start():
    st.set_page_config(
        page_title='henos bot',
        page_icon='https://imgur.com/a/urHOoK3',
        initial_sidebar_state='collapsed',
    )

    st.text('This website is under development, please wait until complete')
