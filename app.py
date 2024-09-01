import streamlit as st
import random

# List of fun facts
fun_facts = [
    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
    "A day on Venus is longer than a year on Venus. It takes Venus longer to rotate on its axis than it does to orbit the Sun.",
    "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
    "Bananas are berries, but strawberries are not. Botanically, bananas qualify as berries, while strawberries do not.",
    "Wombat poop is cube-shaped. This unique shape prevents the poop from rolling away and marks the wombat's territory."
]

# Streamlit app layout
st.title("Fun Facts for Students")

# Add custom CSS for styling
st.markdown("""
    <style>
    .stButton button {
        background-color: #FF6347;
        color: white;
        border-radius: 12px;
        padding: 10px;
        font-size: 16px;
        border: none;
    }
    .stButton button:hover {
        background-color: #FF4500;
    }
    .stWrite {
        font-size: 18px;
        color: #333;
        padding: 10px;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #555;
    }
    .footer a {
        color: #1E90FF;
        text-decoration: none;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    </style>
    """, unsafe_allow_html=True)

# Display a random fun fact
if st.button("Get a Fun Fact"):
    fact = random.choice(fun_facts)
    st.write(fact)

# Footer
st.markdown("""
    <div class="footer">
        <p><strong>Developed By:</strong> Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm" target="_blank">https://flowcv.me/ikm</a></p>
        <p><strong>Developed For:</strong> Essential Generative AI Training</p>
        <p><strong>Conducted By:</strong> PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </div>
    """, unsafe_allow_html=True)
