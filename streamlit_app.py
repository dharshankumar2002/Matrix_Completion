import streamlit as st
st.write("""
         # Matrix Completion
         """
         )
st.write("This is a simple matrix completion calculator")

# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your Matrix", "")
 
status = st.radio("Select Algotihm: ", ('Singular Value Thresholding', 'Gradient Descent', 'Augmented Lagrange Multipliers'))
         
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = "Wait a minute..."
    st.success(result)
         
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    st.write(mat)
