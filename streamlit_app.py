import streamlit as st
st.write("""
         # Matrix Completion
         """
         )
st.write("This is a simple matrix completion calculator")

# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your Matrix", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
