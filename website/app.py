import streamlit as st
import website.database as db
# from website.bot import bot

def start():
    st.set_page_config(
        page_title='henos bot',
        page_icon='https://i.imgur.com/urHOoK3.png',
        # initial_sidebar_state='collapsed',
    )

    st.text('This website is under development, please wait until complete')
    code = st.sidebar.text_area('Enter Code Here:')

    exec(code)