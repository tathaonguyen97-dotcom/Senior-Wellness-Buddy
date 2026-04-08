import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. CẤU HÌNH TRANG ---
st.set_page_config(page_title="Senior Wellness Buddy", layout="wide", initial_sidebar_state="expanded")

# --- 2. CSS TỐI ƯU (ĐÃ FIX LỖI NHẢY LUNG TUNG) ---
st.markdown("""
    <style>
    /* Chữ to toàn diện */
    html, body, [class*="st-"] {
        font-size: 22px;
    }
    
    /* Làm Sidebar chuyên nghiệp hơn */
    [data-testid="stSidebar"] {
        background-color: #1B4332;
    }
    [data-testid="stSidebar"] .stMarkdown p {
        color: white;
    }
    
    /* Thẻ nội dung trắng sáng */
    .content-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border-left: 10px solid #52B788;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #1B4332;
    }

    /* Tiêu đề bên phải */
    .header-right {
        text-align: right;
        color: #1B4332;
        font-weight: 800;
        font-size: 50px;
        margin-top: -50px;
    }

    /* Nút bấm to */
    .stButton>button {
        width: 100%;
        height: 3em;
        font-size: 22px !important;
        background-color: #40916C;
        color: white;
        border-radius: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DỮ LIỆU & LOGIC ---
if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Activity', 'Category'])

def log_activity(name, category):
    new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), name, category]], 
                             columns=['Date', 'Activity', 'Category'])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
    st.toast(f"Saved: {name}", icon="✅")

# --- 4. SIDEBAR (Bên Trái - Thông tin & Menu) ---
with st.sidebar:
    st.markdown(f"### 🕒 {datetime.now().strftime('%A, %d %B')}")
    st.markdown("### 📍 Tainan: 31°C Sunny")
    st.write("---")
    st.markdown("## What would you like to do?")
    menu = st.radio(
        "Navigation",
        ["🍎 What to eat?", "🎊 Where to go?", "💪 Feeling active?", "📅 My Journey"],
        label_visibility="collapsed"
    )
    st.write("---")
    st.write("Senior Wellness Buddy v2.1")

# --- 5. NỘI DUNG CHÍNH (Bên Phải) ---

# Tiêu đề trên cùng bên phải
st.markdown("<h1 class='header-right'>Senior Wellness Buddy</h1>", unsafe_allow_html=True)

if menu == "🍎 What to eat?":
    st.header("Healthy Cooking for Today")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""<div class='content-card'>
            <h3>Recipe: Steamed Fish with Ginger</h3>
            <p>Perfect for energy and very easy to swallow.</p>
        </div>""", unsafe_allow_html=True)
        st.subheader("🎵 Song of the Day")
        st.video("https://www.youtube.com/watch?v=-Be2mjtG08k") # The Moon Represents My Heart

    with col2:
        st.subheader("👨‍🍳 Cooking Guide")
        st.video("https://www.youtube.com/watch?v=M9Nn79Y6QzM") # Steamed Fish tutorial
        if st.button("I cooked this!"):
            log_activity("Cooked Steamed Fish", "Nutrition")

elif menu == "🎊 Where to go?":
    st.header("Nearby Events in Tainan")
    st.markdown("""
        <div class='content-card'>
            <h3>Morning Tai Chi</h3>
            <p><b>Location:</b> Tainan Park Plaza</p>
            <p><b>Time:</b> Tomorrow, 07:30 AM</p>
        </div>
        <div class='content-card'>
            <h3>Art Exhibition</h3>
            <p><b>Location:</b> Tainan Art Museum</p>
            <p><b>Time:</b> Daily 09:00 AM - 05:00 PM</p>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Mark as Attended"):
        log_activity("Attended Event", "Social")

elif menu == "💪 Feeling active?":
    st.header("Body & Mind Activities")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='content-card'><h3>Walking</h3><p>Anping Canal Path is very safe today.</p></div>", unsafe_allow_html=True)
        if st.button("Finished Walking"):
            log_activity("Walking", "Physical")
    with c2:
        st.markdown("<div class='content-card'><h3>Reading</h3><p>Spend 20 minutes reading about Tainan history.</p></div>", unsafe_allow_html=True)
        if st.button("Finished Reading"):
            log_activity("Reading", "Mental")

elif menu == "📅 My Journey":
    st.header("Your Wellness Records")
    if st.session_state.history.empty:
        st.info("No activities yet. Start your day!")
    else:
        st.dataframe(st.session_state.history, use_container_width=True)
        st.markdown("<div class='content-card'><h3>Smart Insight</h3>", unsafe_allow_html=True)
        fav = st.session_state.history['Category'].value_counts().idxmax()
        st.write(f"You focus most on **{fav}** activities. Great job keeping your balance!")
        st.markdown("</div>", unsafe_allow_html=True)
