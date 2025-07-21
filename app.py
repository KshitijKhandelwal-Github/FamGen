import streamlit as st
import familytree as ft
import pandas as pd

st.set_page_config(page_title='FamGen - Generate a Family Tree', layout='wide')
with st.container():
    col1, col2, col3 = st.columns((3, 5, 2))
    with col2:
        with st.container():
            col1, col2, col3 = st.columns((1, 10, 1))
            with col2:
                st.write("# Welcome to FamGen")
                st.markdown("### A simple and easy way to generate a family tree.")
                st.markdown("### Just follow these simple steps:")
                st.markdown("##### 1. Upload a file with the following template.")
                st.markdown('##### 2. Hit "Generate Family Tree".')
                st.markdown("##### 3. Wait for the magic to happen.")
                st.markdown("##### Voila! Your required family tree has been generated.")

file = st.file_uploader("### Upload your file:", type=['xlsx', 'xls', 'csv'])

with st.container():
    col1, col2, col3 = st.columns((5, 2, 5))
    with col2:
        st.markdown("""
            <style>
                button[kind='primary']{
                    background-color: transparent;
                    color: white;
                    border: 0.2px solid white;
                }
                button[kind='primary']:hover{
                    background-color: green;
                    border-color: lightgreen;
                }
            </style>
        """, unsafe_allow_html=True)
        button = st.button("Generate Family Tree", type='primary')

if button and file is not None:
    with st.container():
        col1, col2, col3 = st.columns((1, 10, 1))
        with col2:
            st.graphviz_chart(ft.CreateTree(file), use_container_width=False)

@st.cache_data
def cacheImage(file):
    tree = ft.CreateTree(file)
    return tree.pipe(format='png')

if button and file is not None:
    with st.container():
        col1, col2, col3 = st.columns((1, 10, 1))
        with col2:
            treeImg = cacheImage(file)
            st.download_button(label='Download Tree as Image', data=treeImg, file_name='familytree.png', mime='image/png')

st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background: #262730;
        color: white;
        text-align: center;
        padding: 10px 0;
        z-index: 100;
    }
    </style>
    <div class="footer">
        Made with ❤️ by Kshitij &nbsp;|&nbsp;
        <a href="https://github.com/KshitijKhandelwal-Github" style="color:#fff;" target="_blank">GitHub</a> &nbsp;|&nbsp;
        <a href="https://www.linkedin.com/in/kshitij--khandelwal/" style="color:#0A66C2;" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)