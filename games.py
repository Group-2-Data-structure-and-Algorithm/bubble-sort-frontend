import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    }
    </style>
    """,
    unsafe_allow_html=True)

st.title("BUBBLE SORTING GAME")
st.image("image1.png", width=200)
st.markdown("---")

st.markdown("""
### How to Play:
1. Choose a difficulty level.
2. Click **Generate Numbers** to start.
3. Use the **Swap buttons** to sort the list step by step.
""")

st.markdown("---")


levels = st.selectbox("**Difficulty Level**:", ["Easy", "Medium", "Hard"])
choices = st.selectbox("**Choose an option**", ["Show", "Hide"])


if choices == "Show":
    if levels == "Easy":
        st.markdown("""### Instructions:
        1. Sort 6 numbers step by step.
        2. Focus on learning the basics.
        """)
    elif levels == "Medium":
        st.markdown("""### Instructions:
        1. Sort 12 numbers.
        2. Practice efficiency.
        """)
    else:
        st.markdown("""### Instructions:
        1. Sort 24 numbers.
        2. Bubble Sort compares adjacent numbers and swaps them.
        3. Aim for speed and accuracy.
        """)
st.markdown("<h1 style='color:purple;'>Have Fun While Learning!!</h1>",
    unsafe_allow_html=True)



    




