Senior Wellness Buddy - Project Requirements
1. Project Overview
Senior Wellness Buddy is an assistive application designed to enhance the quality of life for elderly individuals in Tainan. The app provides personalized daily recommendations for nutrition, physical activity, and social engagement, while tracking user behavior to refine future suggestions.

2. Functional Requirements
FR1: Seasonal Nutrition Suggestions
Weather Integration: The system shall fetch real-time weather data (Temperature/Condition) for Tainan.
Dynamic Recipes: The system shall suggest recipes based on the current weather (e.g., cooling foods for >30°C, warming foods for cold/rainy days).
FR2: Public Event Discovery
Localized Events: The system shall display local community events (Cultural exhibitions, morning exercise groups, health seminars).
Senior-Friendly Filters: Events must be filtered by proximity (Tainan area) and appropriateness for elderly users (accessible, daytime hours).
FR3: Light Physical Activity Mapping
Safe Walking Paths: The system shall suggest low-traffic walking routes and public parks (e.g., Tainan Park, Anping Canal).
Environmental Alerts: Suggestions should include reminders for hydration and sun protection based on UV/Temperature levels.
FR4: Automated Reminders
Hydration & Movement: The system shall provide periodic notifications to encourage water intake and light stretching.
FR5: Activity Calendar & Analytics (Core Research Feature)
Activity Logging: Users can record completed activities (e.g., "I cooked this," "I attended this event").
User Preference Analysis: The system shall analyze the frequency of activity categories to identify user interests (Nutrition vs. Social vs. Physical).
Adaptive Recommendation Engine: Future suggestions will be weighted based on historical engagement stored in the calendar.
3. Non-Functional Requirements (UX/UI Standards)
Typography: Minimum font size of 18pt for body text; 24pt+ for headings.
Visual Clarity: High color contrast (WCAG AA standard) to accommodate age-related vision changes.
Accessibility: Large touch targets (minimum 44x44 pixels) for buttons to assist users with reduced motor precision.
Simplicity: Minimalist navigation with a flat hierarchy (Tabs instead of nested menus).
4. Technical Stack
Language: Python 3.x
Framework: Streamlit (Web-based Interface)
Data Handling: Pandas (for Calendar logging and analytics)
Environment: Developed in VS Code
5. Future Roadmap
Integration with Tainan City Government Open Data API.
Voice-activated commands for hands-free interaction.
Integration with Google Maps API for real-time navigation to events.
