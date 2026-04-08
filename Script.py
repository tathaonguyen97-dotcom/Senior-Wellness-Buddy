import streamlit as st
import pandas as pd
from datetime import datetime

# --- CẤU HÌNH GIAO DIỆN NÂNG CAO ---
st.set_page_config(page_title="Senior Wellness Buddy", layout="wide")

# CSS để thay đổi hoàn toàn bố cục
st.markdown("""
    <style>
    /* Tổng thể font chữ to và rõ */
    html, body, [class*="st-"] {
        font-size: 20px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Ẩn Header mặc định của Streamlit */
    header {visibility: hidden;}
    
    /* Sidebar tùy chỉnh */
    [data-testid="stSidebar"] {
        background-color: #2D6A4F;
        min-width: 350px !important;
    }
    
    /* Tiêu đề góc phải trên cùng */
    .top-right-title {
        position: absolute;
        top: -50px;
        right: 0px;
        color: #1B4332;
        font-size: 45px !important;
        font-weight: 800;
        z-index: 999;
    }

    /* Thẻ nội dung (Content Cards) */
    .content-card {
        background: white;
        padding: 30px;
        border-radius: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border-top: 8px solid #52B788;
        margin-bottom: 25px;
    }

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
        transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_name_allowed=True)

# --- DỮ LIỆU GIẢ LẬP (MOCK DATA) ---
today_date = datetime.now().strftime("%A, %d %B %Y")
weather_info = "📍 Tainan | 🌡️ 31°C Sunny | 🍃 AQI: 42 (Good)"

# --- SIDEBAR (BÊN TRÁI) ---
with st.sidebar:
    st.markdown(f"<p style='color: white; font-size: 18px;'>{today_date}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #D8F3DC; font-size: 20px; font-weight: bold;'>{weather_info}</p>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<h2 style='color: white;'>Menu</h2>", unsafe_allow_html=True)
    
    # Navigation bằng Radio button giả lập menu dọc
    menu = st.radio(
        "Choose an activity:",
        ["🍎 What to eat today?", "🎊 Where to go?", "💪 Feeling active?", "📅 My Journey"],
        index=0
    )
    st.write("---")
    st.markdown("<p style='color: #D8F3DC; font-size: 14px;'>© 2026 Senior Wellness Buddy Project</p>", unsafe_allow_html=True)

# --- NỘI DUNG CHÍNH (BÊN PHẢI) ---
# Tiêu đề góc phải trên cùng
st.markdown("<h1 class='top-right-title'>Senior Wellness Buddy</h1>", unsafe_allow_html=True)

if 'history' not in st.session_state:
    st.session_state.history = pd.DataFrame(columns=['Date', 'Activity', 'Category'])

def log_activity(name, category):
    new_entry = pd.DataFrame([[datetime.now().strftime("%Y-%m-%d"), name, category]], 
                             columns=['Date', 'Activity', 'Category'])
    st.session_state.history = pd.concat([st.session_state.history, new_entry], ignore_index=True)
    st.toast(f"Saved to your calendar: {name}!", icon="✅")

# LOGIC HIỂN THỊ THEO MENU
if menu == "🍎 What to eat today?":
    st.header("Daily Healthy Nutrition")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("""
            <div class='content-card'>
                <h3>Today's Recipe: Steamed Sea Bass with Ginger</h3>
                <p><b>Health Benefit:</b> High in Omega-3 for brain health and very easy to digest for seniors.</p>
                <p><b>Ingredients:</b> Sea bass, ginger slices, soy sauce, green onions.</p>
            </div>
        """, unsafe_allow_html=True)
        st.subheader("🎵 Relaxing Music for Cooking")
        # Video 1: Bài hát thư giãn (Ví dụ: Nhạc không lời hoặc nhạc cũ)
        st.video("https://www.youtube.com/watch?v=5as_V_D7Pew") 

    with col2:
        st.subheader("👨‍🍳 Step-by-Step Tutorial")
        # Video 2: Hướng dẫn nấu ăn thực tế (Ví dụ: Món cá hấp)
        st.video("https://www.youtube.com/watch?v=M9Nn79Y6QzM")
        if st.button("I cooked this healthy meal!"):
            log_activity("Cooked Steamed Sea Bass", "Nutrition")

elif menu == "🎊 Where to go?":
    st.header("Community Events in Tainan")
    events = [
        {"title": "Morning Tai Chi Workshop", "loc": "Tainan Park", "time": "07:30 AM", "desc": "Join local seniors for a refreshing session of Tai Chi."},
        {"title": "Tea Art Appreciation", "loc": "Chihkan Tower Culture Hall", "time": "02:00 PM", "desc": "Learn the history of Oolong tea and enjoy free tasting."}
    ]
    for e in events:
        st.markdown(f"""
            <div class='content-card'>
                <h3>{e['title']}</h3>
                <p>📍 <b>Location:</b> {e['loc']} | 🕒 <b>Time:</b> {e['time']}</p>
                <p>{e['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Mark attendance for {e['title']}"):
            log_activity(e['title'], "Social")

elif menu == "💪 Feeling active?":
    st.header("Body & Mind Activities")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
            <div class='content-card'>
                <h3>Outdoor Activity</h3>
                <p><b>Safe Walk:</b> Anping Canal Path.</p>
                <p>Enjoy the breeze and sunset. The path is flat and wheelchair accessible.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Completed my walk"):
            log_activity("Anping Canal Walk", "Physical")
    
    with c2:
        st.markdown("""
            <div class='content-card'>
                <h3>Mental Enrichment</h3>
                <p><b>Reading:</b> 'The Wonders of Tainan History'.</p>
                <p>Keeping the mind sharp is just as important as the body.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Finished reading session"):
            log_activity("Reading History", "Mental")

elif menu == "📅 My Journey":
    st.header("Your Personal Wellness Calendar")
    if st.session_state.history.empty:
        st.info("No activities recorded yet. Let's start with a walk or a meal!")
    else:
        st.table(st.session_state.history)
        
        # PHÂN TÍCH NHU CẦU (RESEARCH COMPONENT)
        st.markdown("""<div class='content-card'><h3>Smart Insight</h3>""", unsafe_allow_html=True)
        counts = st.session_state.history['Category'].value_counts()
        fav = counts.idxmax()
        st.write(f"Your activity log shows a strong preference for **{fav}**.")
        st.write("Based on this, we are preparing more similar suggestions for your next week!")
        st.markdown("</div>", unsafe_allow_html=True)
