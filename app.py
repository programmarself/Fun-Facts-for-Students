import streamlit as st
import random

# Define a list of fun facts
fun_facts = [
    'Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.',
    'A group of flamingos is called a "flamboyance."',
    'Octopuses have three hearts and blue blood.',
    'Bananas are berries, but strawberries are not.',
    'An adult human body is made up of about 60% water.',
    'A day on Venus is longer than a year on Venus.',
    'Humans share 60% of their DNA with bananas.',
    'The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.',
    'A cow-bison hybrid is called a "beefalo."',
    'The longest word in the English language is "pneumonoultramicroscopicsilicovolcanoconiosis."',
    'Slugs have four noses.',
    'A newborn kangaroo is the size of a lima bean.',
    'There are more stars in the universe than grains of sand on all the Earth’s beaches.',
    'Wombat poop is cube-shaped.',
    'A group of owls is called a "parliament."',
    'Sharks have been around longer than trees.',
    'A jiffy is an actual unit of time: 1/100th of a second.',
    'You can hear a blue whale’s heartbeat from more than 2 miles away.',
    'A single strand of spaghetti is called a "spaghetto."',
    'Elephants can’t jump.',
    'The shortest war in history lasted just 38 to 45 minutes.',
    'There are more than 1,500 different types of bananas.',
    'The unicorn is Scotland’s national animal.',
    'A "moment" technically refers to 90 seconds.',
    'The majority of your brain is fat.',
    'Hot water freezes faster than cold water, a phenomenon known as the Mpemba effect.',
    'Peanuts are not nuts; they are legumes.',
    'The heart of a shrimp is located in its head.',
    'Polar bear skin is black.',
    'Dolphins have names for each other.',
    'The longest place name in the world has 85 letters.',
    'Kangaroos can’t walk backward.',
    'The human nose can detect over 1 trillion different scents.',
    'Venus is the hottest planet in our solar system.',
    'An octopus’s brain is shaped like a donut.',
    'More than 80% of the ocean is unexplored.',
    'The dot over the letters “i” and “j” is called a “tittle.”',
    'The human body has around 206 bones.',
    'There are about 200 distinct types of tomatoes.',
    'A snail can sleep for three years.',
    'Pineapples take about two years to grow.',
    'A giraffe’s tongue is black.',
    'Cows have best friends and can become stressed when separated.',
    'In Japan, there is a museum dedicated entirely to rocks that look like faces.',
    'A “Baker’s dozen” means 13 items, not 12.',
    'The longest musical performance in history is by John Cage and lasts 639 years.',
    'The average person walks the equivalent of five times around the world in their lifetime.',
    'The Great Wall of China is not visible from the Moon with the naked eye.',
    'A group of pandas is called an “embarrassment.”',
    'One light year is about 5.88 trillion miles.',
    'A “murder” is a group of crows.',
    'The human eye can distinguish about 10 million different colors.',
    'A baby octopus is the size of a flea when it is born.'
]

# Function to get a random fun fact
def get_fun_fact():
    return random.choice(fun_facts)

# Streamlit application code
st.set_page_config(page_title="Student Fun App", page_icon=":tada:")

# Add CSS for styling
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 36px;
            color: #4CAF50;
        }
        .fact {
            font-size: 20px;
            color: #333;
            margin-bottom: 20px;
        }
        .footer {
            text-align: center;
            font-size: 16px;
            color: #555;
            margin-top: 50px;
        }
        .footer a {
            color: #1E90FF;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .urdu-text {
            font-family: 'Jameel Noori Nastaleeq Kasheeda', serif;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">Welcome to the Student Fun App!</div>', unsafe_allow_html=True)

# Display fun fact
if st.button("Get Fun Fact"):
    fun_fact = get_fun_fact()
    st.markdown(f'<div class="fact">{fun_fact}</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Developed By: Irfan Ullah Khan<br>
        <a href="https://flowcv.me/ikm">https://flowcv.me/ikm</a><br>
        Developed For: Essential Generative AI Training<br>
        Conducted By: PAK ANGELS, iCodeGuru, ASPIRE PAKISTAN
    </div>
""", unsafe_allow_html=True)
