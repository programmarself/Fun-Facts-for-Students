import streamlit as st
import random

# List of fun facts with Urdu translations
fun_facts = [
    {"en": "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
     "ur": "شہد کبھی بگڑتا نہیں۔ آثار قدیمہ کے ماہرین نے قدیم مصری مقبروں میں ایسے برتن دریافت کیے ہیں جو 3,000 سال سے زیادہ پرانے ہیں اور اب بھی کھانے کے قابل ہیں۔"},
    {"en": "A day on Venus is longer than a year on Venus. It takes Venus longer to rotate on its axis than it does to orbit the Sun.",
     "ur": "زہرہ پر ایک دن زہرہ پر ایک سال سے لمبا ہوتا ہے۔ زہرہ کو اپنی محوری گردش مکمل کرنے میں زیادہ وقت لگتا ہے بہ نسبت سورج کے گرد گھومنے کے۔"},
    {"en": "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
     "ur": "آکٹوپس کے تین دل ہوتے ہیں۔ دو خون کو گلے کی طرف پمپ کرتے ہیں، جبکہ تیسرا دل خون کو جسم کے باقی حصے میں پمپ کرتا ہے۔"},
    {"en": "Bananas are berries, but strawberries are not. Botanically, bananas qualify as berries, while strawberries do not.",
     "ur": "کیلے بیری ہیں، لیکن اسٹرابیری نہیں ہیں۔ نباتیاتی طور پر، کیلے بیری کے طور پر شمار ہوتے ہیں، جبکہ اسٹرابیری نہیں ہوتی۔"},
    {"en": "Wombat poop is cube-shaped. This unique shape prevents the poop from rolling away and marks the wombat's territory.",
     "ur": "ومبٹ کا پاخانہ مکعب شکل کا ہوتا ہے۔ یہ منفرد شکل پاخانے کو لڑھکنے سے روکتی ہے اور ومبٹ کی حدود کی نشاندہی کرتی ہے۔"}
]

# Streamlit app layout
st.set_page_config(page_title="Fun Facts for Students", page_icon=":star:", layout="wide")

# Add custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f4f8;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 12px 24px;
        font-size: 18px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stWrite {
        font-size: 20px;
        color: #333;
        margin: 20px 0;
    }
    .fun-fact-box {
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #555;
        padding: 20px;
        background-color: #ffffff;
        border-top: 1px solid #e1e1e1;
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

# App Title
st.title("✨ Fun Facts for Students ✨")

# Add a subtitle
st.subheader("Discover interesting facts and their Urdu translations!")

# Display a random fun fact with Urdu translation
if st.button("Get a Fun Fact"):
    fact = random.choice(fun_facts)
    
    # Create a stylish box for the fact
    st.markdown(f"""
    <div class="fun-fact-box">
        <h2>Fun Fact (English):</h2>
        <p>{fact['en']}</p>
        <hr>
        <h2>Fun Fact (Urdu):</h2>
        <p>{fact['ur']}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer with professional styling
st.markdown("""
    <div class="footer">
        <p><strong>Developed By:</strong> Irfan Ullah Khan</p>
        <p><a href="https://flowcv.me/ikm" target="_blank">https://flowcv.me/ikm</a></p>
        <p><strong>Developed For:</strong> Essential Generative AI Training</p>
        <p><strong>Conducted By:</strong> PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN</p>
    </div>
    """, unsafe_allow_html=True)
