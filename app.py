import streamlit as st

data = {
    'fruit': 'apple',
    'book': 'maths',
    'game': 'football',
    'details': {
        'level1': {'level2': {'level3': {'a': 'b'}}}
    }
}

st.json(data)