import streamlit as st
import pandas as pd
from datetime import datetime

# --- UI CONFIGURATION (SENIOR-FRIENDLY: LARGE FONTS & HIGH CONTRAST) ---
st.set_page_config(page_title="Senior Wellness Buddy", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #F8F9FA; }
    h1 { color: #1B4332; font-size: 42px !important; }
    h3 { color: #2D6A4F; }
    .stButton>button { 
        height: 3.5em; 
        width: 100%; 
        font-size: 20px; 
        font-weight: bold;
        border-radius: 12px; 
        background-color: #40916C;
        color: white;
    }
    .suggestion-card { 
        background: white; 
        padding: 25px; 
        border-radius: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 10px solid #52B788;
        margin-bottom: 20px; 
    }
    .info-text { font-size: 18px; color: #495057; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. DATA SIMULATION (MOCKING APIS) ---
def get_weather():
    # Simulated weather for Tainan
    return {"temp": 31, "condition": "Sunny", "aqi": "Good"}

def get_recommendations(temp):
    if temp > 30:
        return {
            "recipe": "Chilled Mung Bean Soup",
            "benefit": "Helps cool down the body and provides hydration.",
            "activity": "Morning walk at Tainan Park (Shady areas recommended)"
        }
    return {
        "recipe": "Warm Ginger Tea & Steamed Fish",
        "benefit": "Boosts circulation and provides light protein.",
        "activity": "Indoor light stretching or Museum visit"
    }

# --- 2. CALENDAR & USER BEHAVIOR TRACKING ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Activity', 'Category'])

def log_to_calendar(name, category):
    new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), name, category]], 
                             columns=['Date', 'Activity', 'Category'])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
    st.balloons() # Visual feedback for seniors

# --- 3. MAIN INTERFACE ---
st.title("🌿 Senior Wellness Buddy")

weather = get_weather()
st.info(f"📍 **Location:** Tainan | 🌡️ **Temp:** {weather['temp']}°C | ☀️ **Condition:** {weather['condition']}")

tab1, tab2, tab3, tab4 = st.tabs(["🍽 Nutrition", "🎭 Events", "🚶 Walking", "📅 My Calendar"])

with tab1:
    recs = get_recommendations(weather['temp'])
    st.markdown(f"""
        <div class='suggestion-card'>
            <h3>Today's Recipe: {recs['recipe']}</h3>
            <p class='info-text'><b>Why it's good:</b> {recs['benefit']}</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("I cooked this today!"):
        log_to_calendar(recs['recipe'], "Nutrition")

with tab2:
    event_title = "Traditional Art Exhibition"
    st.markdown(f"""
        <div class='suggestion-card'>
            <h3>Local Event: {event_title}</h3>
            <p class='info-text'>📍 Tainan Art Museum | 🕒 02:00 PM</p>
            <p class='info-text'>A quiet, air-conditioned environment perfect for a cultural afternoon.</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("I will attend this event"):
        log_to_calendar(event_title, "Social/Culture")

with tab3:
    st.markdown(f"""
        <div class='suggestion-card'>
            <h3>Walking Path: {recs['activity']}</h3>
            <p class='info-text'><b>Reminder:</b> Don't forget to bring a water bottle!</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Finished my walk"):
        log_to_calendar("Morning Walk", "Physical")

with tab4:
    st.subheader("Your Activity History")
    if st.session_state.history.empty:
        st.write("No activities recorded yet. Start your journey today!")
    else:
        st.dataframe(st.session_state.history, use_container_width=True)
        
        # Simple Analytics for your Master's Analysis
        st.divider()
        st.subheader("Personalized Insights")
        category_counts = st.session_state.history['Category'].value_counts()
        most_active = category_counts.idxmax()
        st.success(f"Based on your history, you are most interested in **{most_active}** activities. We will suggest more of these for you!")
