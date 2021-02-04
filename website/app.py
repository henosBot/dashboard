import streamlit as st
import website.database as db
# from website.bot import bot
import traceback

def start():
    st.set_page_config(
        page_title='henos bot',
        page_icon='https://i.imgur.com/urHOoK3.png',
        initial_sidebar_state='collapsed',
    )

    st.text('This website is under development, please wait until complete')
    code = st.text_area('Enter Code Here:')
    try:
        exec(code)
    except:
        st.error(traceback.format_exc())