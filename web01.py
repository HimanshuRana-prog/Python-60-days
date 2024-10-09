import streamlit as st
import function01

todos = function01.get_todo()


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("Enter your Productivity")

for todo in todos:
    st.checkbox(todo)