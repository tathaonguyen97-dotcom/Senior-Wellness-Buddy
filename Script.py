import streamlit as st
import pandas as pd
from datetime import datetime

# --- UI CONFIGURATION ---
st.set_page_config(page_title="Senior Wellness Buddy", layout="wide")

# Custom CSS for the Competition-Ready Interface
st.markdown("""
    <style>
    /* Global Font Size for Seniors */
    html, body, [class*="st-"] {
        font-size: 22px;
        font-family: 'Segoe UI', sans-serif;
    }
    
    header {visibility: hidden;}
    
    /* Fixed Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1B4332;
        min-width: 380px !important;
    }

    /* Top Right Title */
    .top-right-title {
        position: absolute;
        top: -60px;
        right: 10px;
        color: #1B4332;
        font-size: 50px !important;
        font-weight: 800;
        text-align: right;
    }

    /* Dashboard Cards */
    .content-card {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-top: 10px solid #52B788;
        margin-bottom: 30px;
    }

    /* Buttons */
    .stButton>button {
        height: 3.5em;
        font-size: 22px !important;
        border-radius: 15px;
        background-color: #40916C;
        color: white;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1B4332;
        transform: translateY(-2px);
    }
    
    /* Sidebar Text */
    .sidebar-text { color: #D8F3DC; font-size: 22px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA ---
today_date = datetime.now().strftime("%A, %d %B %Y")
weather_info = "📍 Tainan | 🌡️ 31°C Sunny"

# --- SIDEBAR (LEFT) ---
with st.sidebar:
    st.markdown(f"<p style='color: white; font-size: 20px;'>{today_date}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='sidebar-text'><b>{weather_info}</b></p>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<h2 style='color: white;'>How are you today?</h2>", unsafe_allow_html=True)
    
    # Large Vertical Navigation
    menu = st.radio(
        label="Select a section:",
        options=["🍎 What to eat today?", "🎊 Where to go?", "💪 Feeling active?", "📅 My Journey"],
        index=0,
        label_visibility="collapsed"
    )
    st.write("---")
    st.markdown("<p style='color: #95D5B2; font-size: 16px;'>Version 2.0 - Tainan Excellence</p>", unsafe_allow_html=True)

# --- MAIN CONTENT (RIGHT) ---
st.markdown("<h1 class='top-right-title'>Senior Wellness Buddy</h1>", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Activity', 'Category'])

def log_activity(name, category):
    new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), name, category]], 
                             columns=['Date', 'Activity', 'Category'])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
    st.toast(f"Logged: {name}", icon="🌟")

# MENU LOGIC
if menu == "🍎 What to eat today?":
    st.header("Healthy Nutrition for You")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class='content-card'>
                <h3>Recipe: Steamed Fish with Ginger</h3>
                <p><b>Why?</b> Soft texture, high protein, and warm ginger is perfect for digestion.</p>
                <p><b>Quick Steps:</b> Clean fish, add ginger slices, steam for 10 mins, add light soy sauce.</p>
            </div>
        """, unsafe_allow_html=True)
        st.subheader("🎵 Listen to some music")
        # Video 1: Classic Relaxing Song (Teresa Teng - The Moon Represents My Heart)
        st.video("https://www.youtube.com/watch?v=-Be2mjtG08k") 

    with col2:
        st.subheader("👨‍🍳 Cooking Tutorial")
        # Video 2: Actual Cooking Video for Steamed Fish
        st.video("https://www.youtube.com/watch?v=M9Nn79Y6QzM")
        if st.button("I cooked this healthy meal!"):
            log_activity("Cooked Steamed Fish", "Nutrition")

elif menu == "🎊 Where to go?":
    st.header("Local Events in Tainan Area")
    st.markdown("""
        <div class='content-card'>
            <h3>📍 Tainan Senior Morning Tai Chi</h3>
            <p><b>Location:</b> Tainan Park (Main Plaza)</p>
            <p><b>Time:</b> 07:30 AM - 08:30 AM</p>
            <p><b>Detail:</b> A free, gentle exercise session for seniors. All skill levels welcome!</p>
        </div>
        <div class='content-card'>
            <h3>📍 Traditional Tea Tasting Class</h3>
            <p><b>Location:</b> Chihkan Tower Cultural Hall</p>
            <p><b>Time:</b> 02:00 PM - 03:30 PM</p>
            <p><b>Detail:</b> Learn about local tea varieties and enjoy free samples of Oolong tea.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("I'm heading out to an event!"):
        log_activity("Attended Local Event", "Social")

elif menu == "💪 Feeling active?":
    st.header("Body & Mind Enrichment")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class='content-card'>
                <h3>Physical Activity</h3>
                <p><b>Suggestion:</b> 20-minute walk at Anping Canal.</p>
                <p>The path is flat, safe, and offers a beautiful breeze from the water.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Finished my daily walk"):
            log_activity("Anping Canal Walk", "Physical")
    
    with c2:
        st.markdown("""
            <div class='content-card'>
                <h3>Mental Activity</h3>
                <p><b>Suggestion:</b> Read 'Tainan's Hidden Gems'</p>
                <p>Spend 30 minutes reading to keep your mind sharp and discover your city.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Finished my reading time"):
            log_activity("Reading History", "Mental")

elif menu == "📅 My Journey":
    st.header("Your Personal Wellness Record")
    if st.session_state.history.empty:
        st.info("Your journey starts today! Try one of the activities above.")
    else:
        # Display table with bigger font
        st.dataframe(st.session_state.history, use_container_width=True)
        
        # RESEARCH COMPONENT: Pattern Analysis
        st.markdown("<div class='content-card'><h3>📊 Behavioral Insight</h3>", unsafe_allow_html=True)
        top_cat = st.session_state.history['Category'].value_counts().idxmax()
        st.write(f"Excellent! Your record shows you are very consistent with **{top_cat}** activities.")
        st.write("We will prioritize these types of recommendations to fit your lifestyle.")
        st.markdown("</div>", unsafe_allow_html=True)
