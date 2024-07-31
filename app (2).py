# app.py

import streamlit as st
from latest import execute_query

def main():
    st.title("CHAT WITH MY DATABASE")

    query = st.text_input("Enter your query:")

    if st.button("Run Query"):
        if query:
            result = execute_query(query)
            st.write("Output:")
            st.write(result)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()





