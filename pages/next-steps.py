import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageOps
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title = 'Next Steps - Altnova',
    page_icon = "🪟",
    initial_sidebar_state='collapsed',
)

st.markdown("""
    <style>
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    
    .block-container {
                    padding-top: 1rem;
                    padding-bottom: 0rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
    </style>
    """, unsafe_allow_html = True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.css-hi6a2p {padding-top: 0rem;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html = True)

st.title("Next Steps")

st.markdown("<p style='padding-top:10px'> </p>", unsafe_allow_html = True)

st.link_button('💬 **Ask A Quote To Restore Your Balcony**', url='https://altnova.be', use_container_width = True)
st.link_button('🙋‍♂️ **Ask Help Since I Have Other Balcony**', url='https://altnova.be', use_container_width = True)
st.link_button('🛠️ **Save Your Balcony**', url='https://altnova.be', use_container_width = True)

if st.button('🕵️‍♂️ **Detect Another Balcony**', use_container_width = True):
     switch_page('app')