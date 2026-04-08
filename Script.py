import streamlit as st
import pandas as pd
from datetime import datetime

# --- UI CONFIGURATION (OPTIMIZED FOR ELDERLY) ---
st.set_page_config(page_title="Senior Wellness Buddy", layout="centered")

st.markdown("""
    <style>
    /* Làm cho toàn bộ font chữ to hơn */
    html, body, [class*="st-"] {
        font-size: 22px;
    }
    .main { background-color: #F0F4F8; }
    h1 { color: #1B4332; font-size: 48px !important; }
    h2 { color: #2D6A4F; font-size: 36px !important; }
    
    /* Tùy chỉnh các nút bấm cực lớn */
    .stButton>button { 
        height: 4em; 
        width: 100%; 
        font-size: 24px !important; 
        font-weight: bold;
        border-radius: 20px; 
        background-color: #2D6A4F;
        color: white;
        margin-top: 10px;
    }
    /* Thẻ nội dung (Cards) */
    .suggestion-card { 
        background: white; 
        padding: 30px; 
        border-radius: 20px; 
        box-shadow: 0 6px 12px rgba(0,0,0,0.1);
        border-left: 15px solid #52B788;
        margin-bottom: 25px; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. DATA SIMULATION ---
def get_weather():
    return {"temp": 31, "condition": "Sunny"}

# Dữ liệu mẫu cho sự kiện
events_data = [
    {
        "title": "Tainan Heritage Photo Expo",
        "location": "Tainan Art Museum Building 1",
        "time": "02:00 PM - 05:00 PM",
        "detail": "A nostalgic journey through Tainan's history with 200+ rare photos.",
        "cost": "Free for Seniors"
    }
]

# --- 2. LOGIC & CALENDAR ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Activity', 'Category'])

def log_activity(name, category):
    new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), name, category]], 
                             columns=['Date', 'Activity', 'Category'])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
    st.balloons()

# --- 3. MAIN INTERFACE ---
st.title("🌿 Senior Wellness Buddy")
weather = get_weather()
st.subheader(f"📍 Tainan: {weather['temp']}°C | {weather['condition']}")

# Các tiêu đề dạng câu hỏi để kích thích người dùng
tabs = st.tabs([
    "🍎 What to eat today?", 
    "🎊 Where to go?", 
    "💪 Feeling active?", 
    "📅 My Journey"
])

# TAB 1: NUTRITION & YOUTUBE
with tabs[0]:
    st.header("What would you like to cook?")
    st.markdown(f"""
        <div class='suggestion-card'>
            <h3>Recipe: Braised Chicken with Ginger</h3>
            <p><b>Benefit:</b> Great for circulation and easy on the stomach.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Nhúng Video YouTube (Ví dụ: Một video dạy nấu ăn cho người già)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Thay bằng link video thực tế
    
    if st.button("I cooked this healthy meal!"):
        log_activity("Cooked Braised Chicken", "Nutrition")

# TAB 2: EVENTS
with tabs[1]:
    st.header("Any interesting events nearby?")
    for event in events_data:
        st.markdown(f"""
            <div class='suggestion-card'>
                <h3>{event['title']}</h3>
                <p>📍 <b>Location:</b> {event['location']}</p>
                <p>🕒 <b>Time:</b> {event['time']}</p>
                <p><b>About:</b> {event['detail']}</p>
                <p style='color: green;'><b>Cost:</b> {event['cost']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"I'm interested in {event['title']}"):
            log_activity(event['title'], "Social")

# TAB 3: PHYSICAL ACTIVITY (Bao gồm đi dạo, đọc sách, v.v.)
with tabs[2]:
    st.header("How would you like to move?")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class='suggestion-card'><h3>Outdoor Walk</h3><p>Enjoy the fresh air at Tainan Park.</p></div>""", unsafe_allow_html=True)
        if st.button("Walked in the park"):
            log_activity("Park Walk", "Physical")
            
    with col2:
        st.markdown("""<div class='suggestion-card'><h3>Quiet Reading</h3><p>Read 'The Old Man and the Sea'.</p></div>""", unsafe_allow_html=True)
        if st.button("Read a book"):
            log_activity("Reading Time", "Mental")

# TAB 4: CALENDAR & ANALYSIS
with tabs[3]:
    st.header("What have we achieved together?")
    if st.session_state.history.empty:
        st.info("Your calendar is empty. Let's start an activity!")
    else:
        st.table(st.session_state.history)
        
        # Phân tích xu hướng (Research logic)
        st.divider()
        st.subheader("Our Insights for You")
        top_cat = st.session_state.history['Category'].value_counts().idxmax()
        st.success(f"You seem to love **{top_cat}** activities! We'll find more of these for you.")
