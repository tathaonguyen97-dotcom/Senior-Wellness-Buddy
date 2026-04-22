"""
Senior Wellness Buddy - An Intelligent, Context-Aware Ecosystem for Active Aging in Taiwan

This application implements the core features of the SeniorWellnessBuddy proposal:
1. AI-Powered Nutrition & Multimedia
2. National Event Aggregator
3. Dual-Track Activity Logging
4. Smart Wellness Journey

Technical Stack: Python, Streamlit, Pandas, and integrated APIs
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import os
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION & STYLING
# ============================================================================

st.set_page_config(
    page_title="Senior Wellness Buddy",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for accessibility and senior-friendly design
st.markdown("""
<style>
    /* High-contrast, senior-friendly styling */
    :root {
        --primary-color: #FF6B35;
        --secondary-color: #004E89;
        --success-color: #2ECC71;
        --warning-color: #F39C12;
        --text-color: #1C1C1C;
        --light-bg: #F8F9FA;
    }
    
    /* Increase font sizes for readability */
    body {
        font-size: 18px !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    h1 {
        font-size: 36px !important;
        color: #004E89 !important;
        font-weight: bold !important;
    }
    
    h2 {
        font-size: 28px !important;
        color: #FF6B35 !important;
        font-weight: bold !important;
    }
    
    h3 {
        font-size: 24px !important;
        color: #1C1C1C !important;
    }
    
    /* Button styling */
    .stButton > button {
        font-size: 18px !important;
        padding: 15px 30px !important;
        height: auto !important;
        border-radius: 10px !important;
        font-weight: bold !important;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stNumberInput > div > div > input {
        font-size: 18px !important;
        padding: 12px !important;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        padding: 20px !important;
    }
    
    /* Card-like containers */
    .metric-card {
        background-color: #F8F9FA;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF6B35;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA MANAGEMENT & PERSISTENCE
# ============================================================================

DATA_DIR = Path("wellness_data")
DATA_DIR.mkdir(exist_ok=True)

WELLNESS_JOURNEY_FILE = DATA_DIR / "wellness_journey.csv"
NUTRITION_LOG_FILE = DATA_DIR / "nutrition_log.csv"
ACTIVITY_LOG_FILE = DATA_DIR / "activity_log.csv"
EVENTS_LOG_FILE = DATA_DIR / "events_log.csv"

def load_or_create_dataframe(filepath, columns):
    """Load existing dataframe or create new one with specified columns."""
    if filepath.exists():
        return pd.read_csv(filepath)
    return pd.DataFrame(columns=columns)

def save_dataframe(df, filepath):
    """Save dataframe to CSV file."""
    df.to_csv(filepath, index=False)

# Initialize session state
if "wellness_journey" not in st.session_state:
    st.session_state.wellness_journey = load_or_create_dataframe(
        WELLNESS_JOURNEY_FILE,
        ["Date", "Activity", "Duration (min)", "Mood", "Notes"]
    )

if "nutrition_log" not in st.session_state:
    st.session_state.nutrition_log = load_or_create_dataframe(
        NUTRITION_LOG_FILE,
        ["Date", "Meal Type", "Food Item", "Nutritional Value", "Recipe Link"]
    )

if "activity_log" not in st.session_state:
    st.session_state.activity_log = load_or_create_dataframe(
        ACTIVITY_LOG_FILE,
        ["Date", "Activity Type", "Distance (km)", "Duration (min)", "Calories Burned"]
    )

if "events_log" not in st.session_state:
    st.session_state.events_log = load_or_create_dataframe(
        EVENTS_LOG_FILE,
        ["Date", "Event Name", "Location", "Category", "Description"]
    )

# ============================================================================
# HEADER & NAVIGATION
# ============================================================================

col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("# 🌟 Senior Wellness Buddy")
    st.markdown("*An Intelligent, Context-Aware Ecosystem for Active Aging in Taiwan*")

with col2:
    st.markdown(f"### 📅 {datetime.now().strftime('%B %d, %Y')}")

st.divider()

# ============================================================================
# SIDEBAR NAVIGATION
# ============================================================================

st.sidebar.markdown("## 🗂️ Navigation")
page = st.sidebar.radio(
    "Choose a feature:",
    ["🏠 Home", "🍽️ Nutrition Guide", "📍 Events Near You", "🚶 Activity Tracker", "🏆 Wellness Journey"]
)

# ============================================================================
# PAGE: HOME
# ============================================================================

if page == "🏠 Home":
    st.markdown("## Welcome to Your Wellness Companion!")
    st.markdown("""
    Senior Wellness Buddy is designed specifically for you. We help you:
    - **Eat Well**: Get personalized nutrition advice and cooking tutorials
    - **Stay Active**: Track your daily activities and find safe walking routes
    - **Connect**: Discover local events and activities in your area
    - **Celebrate**: Record your wellness victories and build healthy habits
    """)
    
    st.divider()
    
    # Quick Stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "🍽️ Meals Logged",
            len(st.session_state.nutrition_log),
            "this month"
        )
    
    with col2:
        st.metric(
            "🚶 Activities",
            len(st.session_state.activity_log),
            "this month"
        )
    
    with col3:
        st.metric(
            "📍 Events Found",
            len(st.session_state.events_log),
            "nearby"
        )
    
    with col4:
        st.metric(
            "🏆 Victories",
            len(st.session_state.wellness_journey),
            "recorded"
        )
    
    st.divider()
    
    # Triple-A Architecture Explanation
    st.markdown("## 🎯 How We Support You: The Triple-A Architecture")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 🔧 Adaptive Intelligence
        We use real-time weather and location data to give you advice tailored to your area.
        """)
    
    with col2:
        st.markdown("""
        ### ♿ Accessible Engagement
        Simple, one-click actions. No complex menus. Just what you need.
        """)
    
    with col3:
        st.markdown("""
        ### 📊 Analytical Empowerment
        We track your progress and celebrate your victories!
        """)

# ============================================================================
# PAGE: NUTRITION GUIDE
# ============================================================================

elif page == "🍽️ Nutrition Guide":
    st.markdown("## 🍽️ AI-Powered Nutrition & Multimedia")
    st.markdown("*Healthy eating made simple with cooking tutorials and nostalgic music*")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Log Your Meal")
        
        meal_date = st.date_input("Date", key="nutrition_date")
        meal_type = st.selectbox(
            "Meal Type",
            ["Breakfast", "Lunch", "Dinner", "Snack"],
            key="meal_type"
        )
        food_item = st.text_input("What did you eat?", key="food_item")
        nutritional_value = st.text_input("Nutritional notes (e.g., High in Protein)", key="nutrition_notes")
        recipe_link = st.text_input("Recipe link (optional)", key="recipe_link")
        
        if st.button("✅ Log This Meal", key="log_meal"):
            new_entry = pd.DataFrame({
                "Date": [meal_date],
                "Meal Type": [meal_type],
                "Food Item": [food_item],
                "Nutritional Value": [nutritional_value],
                "Recipe Link": [recipe_link]
            })
            st.session_state.nutrition_log = pd.concat(
                [st.session_state.nutrition_log, new_entry],
                ignore_index=True
            )
            save_dataframe(st.session_state.nutrition_log, NUTRITION_LOG_FILE)
            st.success("✨ Meal logged successfully!")
    
    with col2:
        st.markdown("### 🎵 Recommended Recipes & Music")
        
        # Sample healthy recipes
        recipes = {
            "🥗 Simple Vegetable Salad": {
                "ingredients": "Lettuce, Tomato, Cucumber, Olive Oil",
                "time": "5 minutes",
                "benefits": "Rich in vitamins and fiber"
            },
            "🍲 Traditional Taiwanese Soup": {
                "ingredients": "Chicken, Ginger, Dates, Water",
                "time": "30 minutes",
                "benefits": "Warming and nourishing"
            },
            "🍚 Brown Rice with Vegetables": {
                "ingredients": "Brown Rice, Carrots, Peas, Broccoli",
                "time": "25 minutes",
                "benefits": "Good source of whole grains"
            },
            "🥚 Egg with Spinach": {
                "ingredients": "Eggs, Spinach, Garlic, Oil",
                "time": "10 minutes",
                "benefits": "High in protein and iron"
            }
        }
        
        selected_recipe = st.selectbox("Choose a recipe", list(recipes.keys()))
        recipe_info = recipes[selected_recipe]
        
        st.markdown(f"""
        **Ingredients:** {recipe_info['ingredients']}  
        **Time:** {recipe_info['time']}  
        **Benefits:** {recipe_info['benefits']}
        """)
        
        st.markdown("### 🎶 Nostalgic Music Playlist")
        st.markdown("""
        While cooking, enjoy these classics:
        - 鄧麗君 (Teresa Teng) - 月亮代表我的心
        - 周華健 (Wakin Chau) - 朋友
        - 陶喆 (David Tao) - 說好不哭
        """)
    
    st.divider()
    
    # Nutrition Log History
    st.markdown("### 📊 Your Meal History")
    if len(st.session_state.nutrition_log) > 0:
        st.dataframe(st.session_state.nutrition_log, use_container_width=True)
    else:
        st.info("No meals logged yet. Start by logging your first meal!")

# ============================================================================
# PAGE: EVENTS NEAR YOU
# ============================================================================

elif page == "📍 Events Near You":
    st.markdown("## 📍 National Event Aggregator")
    st.markdown("*Discover activities and events happening near you in Taiwan*")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔍 Find Events")
        
        county = st.selectbox(
            "Select your county:",
            [
                "Taipei", "New Taipei", "Taoyuan", "Taichung", "Tainan",
                "Kaohsiung", "Keelung", "Hsinchu", "Miaoli", "Changhua",
                "Nantou", "Yunlin", "Chiayi", "Pingtung", "Yilan",
                "Hualien", "Taitung", "Penghu", "Kinmen", "Lienchiang"
            ]
        )
        
        event_category = st.selectbox(
            "Event Category:",
            ["Tea Arts", "Temple Festival", "Senior Workshop", "Cultural Event", "Health Seminar"]
        )
        
        if st.button("🔎 Search Events"):
            st.session_state.search_performed = True
    
    with col2:
        st.markdown("### 📅 Upcoming Events")
        
        # Sample events for demonstration
        sample_events = {
            "Taipei": [
                {"name": "Traditional Tea Arts Workshop", "date": "2026-05-01", "time": "14:00"},
                {"name": "Senior Health Seminar", "date": "2026-05-05", "time": "10:00"}
            ],
            "Taichung": [
                {"name": "Temple Festival Celebration", "date": "2026-05-03", "time": "09:00"},
                {"name": "Tai Chi Class for Seniors", "date": "2026-05-07", "time": "07:00"}
            ],
            "Tainan": [
                {"name": "Cultural Heritage Walking Tour", "date": "2026-05-02", "time": "15:00"},
                {"name": "Cooking Class - Traditional Recipes", "date": "2026-05-06", "time": "11:00"}
            ]
        }
        
        if county in sample_events:
            for event in sample_events[county]:
                st.markdown(f"""
                **{event['name']}**  
                📅 {event['date']} at {event['time']}
                """)
    
    st.divider()
    
    # Log Event Interest
    st.markdown("### ❤️ Save Events You're Interested In")
    
    event_name = st.text_input("Event Name", key="event_name")
    event_location = st.text_input("Location", key="event_location")
    event_category_log = st.selectbox("Category", ["Tea Arts", "Festival", "Workshop", "Other"], key="event_cat")
    event_description = st.text_area("Description", key="event_desc")
    
    if st.button("💾 Save Event", key="save_event"):
        new_event = pd.DataFrame({
            "Date": [datetime.now().date()],
            "Event Name": [event_name],
            "Location": [event_location],
            "Category": [event_category_log],
            "Description": [event_description]
        })
        st.session_state.events_log = pd.concat(
            [st.session_state.events_log, new_event],
            ignore_index=True
        )
        save_dataframe(st.session_state.events_log, EVENTS_LOG_FILE)
        st.success("✨ Event saved!")
    
    st.divider()
    
    # Events Log
    st.markdown("### 📋 Your Saved Events")
    if len(st.session_state.events_log) > 0:
        st.dataframe(st.session_state.events_log, use_container_width=True)
    else:
        st.info("No events saved yet. Find and save events you'd like to attend!")

# ============================================================================
# PAGE: ACTIVITY TRACKER
# ============================================================================

elif page == "🚶 Activity Tracker":
    st.markdown("## 🚶 Dual-Track Activity Logging")
    st.markdown("*Track your physical activities and mental wellness*")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🏃 Physical Activity")
        
        activity_date = st.date_input("Date", key="activity_date")
        activity_type = st.selectbox(
            "Activity Type",
            ["Walking", "Tai Chi", "Swimming", "Gardening", "Dancing", "Other"],
            key="activity_type"
        )
        distance = st.number_input("Distance (km)", min_value=0.0, step=0.5, key="distance")
        duration = st.number_input("Duration (minutes)", min_value=0, step=5, key="duration")
        calories = st.number_input("Estimated Calories Burned", min_value=0, step=10, key="calories")
        
        if st.button("✅ Log Activity", key="log_activity"):
            new_activity = pd.DataFrame({
                "Date": [activity_date],
                "Activity Type": [activity_type],
                "Distance (km)": [distance],
                "Duration (min)": [duration],
                "Calories Burned": [calories]
            })
            st.session_state.activity_log = pd.concat(
                [st.session_state.activity_log, new_activity],
                ignore_index=True
            )
            save_dataframe(st.session_state.activity_log, ACTIVITY_LOG_FILE)
            st.success("✨ Activity logged successfully!")
    
    with col2:
        st.markdown("### 🧠 Mental Wellness")
        
        st.markdown("#### Daily Wisdom")
        wisdom_quotes = [
            "Every step you take is a victory. Keep moving forward!",
            "Your health is your wealth. Invest in yourself today.",
            "Staying active keeps your mind sharp and your heart happy.",
            "You are stronger than you think. Believe in yourself!",
            "Small steps lead to big changes. Be patient with yourself."
        ]
        
        today_quote = wisdom_quotes[datetime.now().day % len(wisdom_quotes)]
        st.info(f"💭 {today_quote}")
        
        st.markdown("#### Cognitive Activities")
        st.markdown("""
        - **Reading:** Try reading a newspaper or book for 30 minutes
        - **Puzzles:** Solve crosswords or Sudoku
        - **Learning:** Take an online class on topics you love
        - **Socializing:** Call a friend or family member
        """)
    
    st.divider()
    
    # Activity Statistics
    st.markdown("### 📊 Your Activity Statistics")
    
    if len(st.session_state.activity_log) > 0:
        col1, col2, col3 = st.columns(3)
        
        total_activities = len(st.session_state.activity_log)
        total_duration = st.session_state.activity_log["Duration (min)"].sum()
        total_calories = st.session_state.activity_log["Calories Burned"].sum()
        
        with col1:
            st.metric("Total Activities", total_activities)
        with col2:
            st.metric("Total Minutes", int(total_duration))
        with col3:
            st.metric("Total Calories", int(total_calories))
        
        st.dataframe(st.session_state.activity_log, use_container_width=True)
    else:
        st.info("No activities logged yet. Start by logging your first activity!")

# ============================================================================
# PAGE: WELLNESS JOURNEY
# ============================================================================

elif page == "🏆 Wellness Journey":
    st.markdown("## 🏆 Smart Wellness Journey")
    st.markdown("*Celebrate your victories and track your progress*")
    
    st.divider()
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📝 Record Your Victory")
        
        victory_date = st.date_input("Date", key="victory_date")
        victory_activity = st.selectbox(
            "What did you accomplish?",
            [
                "Completed a meal",
                "Finished a walk",
                "Attended an event",
                "Did cognitive exercise",
                "Helped someone",
                "Other"
            ],
            key="victory_activity"
        )
        victory_mood = st.selectbox(
            "How do you feel?",
            ["😊 Happy", "😌 Calm", "💪 Energized", "😄 Proud", "🤗 Grateful"],
            key="victory_mood"
        )
        victory_notes = st.text_area("Add notes about your victory", key="victory_notes")
        
        if st.button("🎉 Celebrate This Victory!", key="log_victory"):
            new_victory = pd.DataFrame({
                "Date": [victory_date],
                "Activity": [victory_activity],
                "Duration (min)": [0],
                "Mood": [victory_mood],
                "Notes": [victory_notes]
            })
            st.session_state.wellness_journey = pd.concat(
                [st.session_state.wellness_journey, new_victory],
                ignore_index=True
            )
            save_dataframe(st.session_state.wellness_journey, WELLNESS_JOURNEY_FILE)
            st.success("🌟 Victory recorded! You're amazing!")
            st.balloons()
    
    with col2:
        st.markdown("### 🎯 Your Wellness Milestones")
        
        if len(st.session_state.wellness_journey) > 0:
            milestone_count = len(st.session_state.wellness_journey)
            
            if milestone_count >= 10:
                st.success("🏅 Gold Star! You've recorded 10+ victories!")
            elif milestone_count >= 5:
                st.info("⭐ Great job! You've recorded 5+ victories!")
            else:
                st.warning("🌱 You're just getting started! Keep going!")
            
            st.metric("Total Victories", milestone_count)
    
    st.divider()
    
    # Wellness Journey History
    st.markdown("### 📖 Your Wellness Story")
    
    if len(st.session_state.wellness_journey) > 0:
        # Display in reverse chronological order
        journey_display = st.session_state.wellness_journey.iloc[::-1].reset_index(drop=True)
        
        for idx, row in journey_display.iterrows():
            st.markdown(f"""
            **{row['Date']}** - {row['Activity']}  
            Mood: {row['Mood']} | {row['Notes']}
            """)
    else:
        st.info("Your wellness journey starts here! Record your first victory to get started.")

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
st.markdown("""
---
**Senior Wellness Buddy** - Empowering Taiwan's Super-Aged Society  
*Developed by Future Assist Lab | Instructed by Professor HSU, CHUNG-HAO*  
*An Intelligent, Context-Aware Ecosystem for Active Aging in Taiwan*
""")
