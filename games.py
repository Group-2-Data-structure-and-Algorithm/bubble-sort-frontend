import streamlit as st
import random 

# Background
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fbc2eb, #a6c1ee);
    }
    </style>
    """,
    unsafe_allow_html=True)
st.title("Welcome TO BUBBLE SORT GAME!")
st.image("image1.png.jpg", width=800)
st.markdown("---")

# instructions
st.markdown("""
### How to Play:
1. choose a difficulty level.
2. click **Generate Numbers** to start.
3. use the ** Swap button** to start the list step by step.
            """)

st.markdown("---")

# Difficulty levels and choices
levels = st.selectbox("**Difficulty Level**", ["Easy", "Medium", "Hard"])
choices = st.selectbox("**Choose an option**", ["Show", "Hide"])


if choices == "Show":
    if levels == "Easy":
        st.markdown("""### Intructions:
        1. Sort 6 numbers step ny step.
        2. Focus on learning the basics.
                    """)
    elif levels == "Medium":
        st.markdown("""### Intructions:
        1. Sort 12 numbers.
        2. Practice efficiency.
                    """)
    else:
        st.markdown("""### Intructions:
        1. Sort 20 numbers.
        2. Bubble Sort compares adjacent numbers and swaps them.
        2. Aim for speed and accuracy.
                    """)
st.markdown("---")

if "numbers" not in st.session_state:
    st.session_state.numbers = []

if "moves" not in st.session_state:
    st.session_state.moves = 0

if st.button("Generate Numbers"):
    if levels == "Easy":
        size = 6
    elif levels == "Medium":
        size = 12
    else:
        size = 20   
    
    st.session_state.numbers = random.sample(range(1, 100), size)
    st.session_state.moves = 0

if st.session_state.numbers:
    st.write("##Current List:")
    st.write(st.session_state.numbers)

    i = st.number_input(
        "Choose index to swap with next",
        0,
        len(st.session_state.numbers) - 2,
        step=1
    )

    if st.button("Swap"):
        arr = st.session_state.numbers

        #swap
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        st.session_state.moves += 1

        #feedback
        if arr[i] > arr[i + 1]:
            st.warning(" That swap may not help!")
        else:
            st.success(" Good swap!")

st.write("Moves: ", st.session_state.moves)

if st.session_state.numbers == sorted(st.session_state.numbers):
        st.success(f"🎉 You sorted the list in {st.session_state.moves} moves!")




st.markdown("<H1 STYLE ='color:purple;'>Have Fun While Learning!!<?h1>",
    unsafe_allow_html=True)


    




