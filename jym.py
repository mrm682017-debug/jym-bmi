import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Elite Gym Manager", page_icon="🏋️‍♂️", layout="wide")

# Session State for Data
if 'gym_members' not in st.session_state:
    st.session_state.gym_members = []

# --- Aapka Wohi Zabardast Design (Custom CSS) ---
st.markdown("""
    <style>
    .main-box { background-color: #ffffff; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.1); border: 1px solid #eee; margin-bottom: 20px; }
    .exercise-card { background-color: #f9f9f9; padding: 15px; border-radius: 12px; text-align: center; border: 1px solid #e0e0e0; margin-bottom: 20px; min-height: 150px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; background-color: #007bff; color: white; }
    .remaining-days { color: #d9534f; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🛡️ ADMIN DASHBOARD")
menu = st.sidebar.radio("Navigation", [
    "📊 Lec 1: Visual BMI & Progress", 
    "👥 Lec 2: Member Records (Fee Tracking)", 
    "📚 Lec 3: Exercise Dictionary"
])

# --- SECTION 1: VISUAL BMI (Wapis Agaya!) ---
if menu == "📊 Lec 1: Visual BMI & Progress":
    st.title("⚖️ Visual BMI Calculator")
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        h = st.number_input("Height (cm):", 50, 250, 175)
        w = st.number_input("Weight (kg):", 10, 300, 75)
        calculate = st.button("Calculate BMI ▶️")
        st.markdown('</div>', unsafe_allow_html=True)

    if calculate:
        bmi = w / ((h/100)**2)
        with col2:
            fig = go.Figure(go.Indicator(
                mode = "gauge+number", value = bmi,
                title = {'text': "BMI Fitness Scale"},
                gauge = {'axis': {'range': [15, 40]}, 'bar': {'color': "black"},
                    'steps': [
                        {'range': [15, 18.5], 'color': "#FFCC00"}, # Underweight
                        {'range': [18.5, 25], 'color': "#008000"}, # Normal
                        {'range': [25, 30], 'color': "#FFFF00"},   # Overweight
                        {'range': [30, 40], 'color': "#FF0000"}    # Obese
                    ]}))
            st.plotly_chart(fig, use_container_width=True)

# --- SECTION 2: ADMIN RECORDS (With Fee Countdown) ---
elif menu == "👥 Lec 2: Member Records (Fee Tracking)":
    st.title("👥 Member Fee Management")
    st.write("Is member ki fee kitne din mein khatam hogi?")

    with st.expander("➕ Add Member Entry", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            m_name = st.text_input("Member Name:")
            m_fee = st.selectbox("Fee Status:", ["Paid ✅", "Pending ❌"])
        with c2:
            pay_date = st.date_input("Payment Date:", datetime.now())
            m_day = st.selectbox("Workout Day:", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

        if st.button("Submit Record"):
            if m_name:
                expiry = pay_date + timedelta(days=30)
                st.session_state.gym_members.append({
                    "Name": m_name, "Fee": m_fee, "Date": pay_date, "Expiry": expiry, "Day": m_day
                })
                st.success(f"{m_name} ka record save ho gaya!")

    if st.session_state.gym_members:
        st.subheader("📋 Member Ledger (Auto Countdown)")
        final_list = []
        today = datetime.now().date()
        
        for m in st.session_state.gym_members:
            days_left = (m["Expiry"] - today).days
            status = f"{days_left} Din Baaki" if days_left > 0 else "Expired ❌"
            
            final_list.append({
                "Name": m["Name"], "Status": m["Fee"], "Paid On": m["Date"], "Days Left": status, "Day": m["Day"]
            })
        
        st.table(pd.DataFrame(final_list))

# --- SECTION 3: MEGA EXERCISE DICTIONARY (Chest Specialists) ---
elif menu == "📚 Lec 3: Exercise Dictionary":
    st.title("📖 Complete Gym Library")
    muscle = st.selectbox("Select Muscle Group:", ["Chest", "Back", "Legs", "Arms", "Shoulders"])
    
    # Large Database
    exercises = {
        "Chest": [
            {"n": "Flat Bench Press", "d": "Overall mass."}, {"n": "Incline Press", "d": "Upper chest."},
            {"n": "Decline Press", "d": "Lower chest."}, {"n": "Dumbbell Flys", "d": "Chest stretch."},
            {"n": "Cable Crossovers", "d": "Inner chest."}, {"n": "Chest Dips", "d": "Lower power."},
            {"n": "Push-Ups", "d": "Bodyweight."}, {"n": "Pec Deck", "d": "Isolation."}
        ],
        "Back": [
            {"n": "Deadlifts", "d": "Power."}, {"n": "Lat Pulldowns", "d": "Width."},
            {"n": "Rows", "d": "Thickness."}, {"n": "Pull-Ups", "d": "Overall."}
        ]
    }

    ex_list = exercises.get(muscle, [])
    for i in range(0, len(ex_list), 2):
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f'<div class="exercise-card"><h4>🔥 {ex_list[i]["n"]}</h4><p>{ex_list[i]["d"]}</p></div>', unsafe_allow_html=True)
        if i+1 < len(ex_list):
            with col_b:
                st.markdown(f'<div class="exercise-card"><h4>🔥 {ex_list[i+1]["n"]}</h4><p>{ex_list[i+1]["d"]}</p></div>', unsafe_allow_html=True)