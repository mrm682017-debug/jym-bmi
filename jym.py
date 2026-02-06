import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import time

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Pro Gym Suite", page_icon="🏋️‍♂️", layout="wide")

# Session State for Data (Records ko save rakhne ke liye)
if 'gym_members' not in st.session_state:
    st.session_state.gym_members = []
if 'water' not in st.session_state:
    st.session_state.water = 0

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .exercise-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 25px;
        text-align: center;
        border: 1px solid #eee;
    }
    .stButton>button { width: 100%; border-radius: 10px; font-weight: bold; background-color: #007bff; color: white; }
    img { border-radius: 12px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DASHBOARD ---
st.sidebar.title("📑 GYM DASHBOARD")
menu = st.sidebar.radio("Main Menu", ["Lec 1: Fitness Tools", "Lec 2: Gym Manager (Admin)", "📚 Full Exercise Dictionary"])

# --- SECTION 1: LEC 1 (HEALTH TOOLS & VISUAL BMI) ---
if menu == "Lec 1: Fitness Tools":
    st.title("📊 Health Tools")
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
        st.subheader("BMI Calculator")
        w = st.number_input("Weight (kg)", value=70.0)
        h = st.number_input("Height (cm)", value=170.0)
        calc_bmi = st.button("Calculate BMI")
        
        st.divider()
        st.subheader("Water Intake")
        if st.button("Add Glass 🥛"): st.session_state.water += 1
        st.progress(min(st.session_state.water/10, 1.0))
        st.write(f"Logged: {st.session_state.water} / 10 Glasses")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if calc_bmi:
            bmi = w / ((h/100)**2)
            # Visual Gauge Meter (Jo aapne manga tha)
            fig = go.Figure(go.Indicator(
                mode = "gauge+number", value = bmi,
                title = {'text': f"BMI Score: {bmi:.1f}"},
                gauge = {
                    'axis': {'range': [15, 40]},
                    'bar': {'color': "black"},
                    'steps': [
                        {'range': [15, 18.5], 'color': "#FFCC00"}, 
                        {'range': [18.5, 25], 'color': "#008000"}, 
                        {'range': [25, 30], 'color': "#FFFF00"},   
                        {'range': [30, 40], 'color': "#FF0000"}    
                    ]}))
            st.plotly_chart(fig, use_container_width=True)

# --- SECTION 2: LEC 2 (GYM MANAGER - ADMIN PANEL) ---
elif menu == "Lec 2: Gym Manager (Admin)":
    st.title("👥 Gym Management (Admin)")
    st.write("Record members' fee and workout status (Monday to Sunday).")

    with st.expander("➕ Add Member Record (Fee & Day)", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            m_name = st.text_input("Member Name:")
            m_fee = st.selectbox("Fee Status", ["Paid ✅", "Pending ❌"])
        with c2:
            m_day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
            
            # Sunday Off Logic
            if m_day == "Sunday":
                st.warning("Sunday is Gym OFF Day! 😴")
                m_workout = "OFF"
            else:
                m_workout = st.radio("Workout Activity:", ["Touched/Done 💪", "Absent ❌"], horizontal=True)

        if st.button("Save Record"):
            if m_name:
                st.session_state.gym_members.append({
                    "Date": datetime.now().strftime("%Y-%m-%d"),
                    "Name": m_name, "Fee": m_fee, "Day": m_day, "Status": m_workout
                })
                st.success(f"{m_name} ka record update ho gaya!")
            else:
                st.error("Please enter a name.")

    if st.session_state.gym_members:
        st.subheader("📋 Gym Ledger / Fee List")
        df = pd.DataFrame(st.session_state.gym_members)
        st.table(df) # Table showing all added members
        if st.button("Clear All Data"):
            st.session_state.gym_members = []
            st.rerun()

# --- SECTION 3: FULL EXERCISE DICTIONARY ---
elif menu == "📚 Full Exercise Dictionary":
    st.title("📖 Complete Gym Exercise Dictionary")
    muscle = st.selectbox("Select Muscle Group", ["Chest", "Back", "Shoulders", "Legs", "Arms", "Abs & Core"])
    
    col_a, col_b = st.columns(2)

    if muscle == "Chest":
        with col_a:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/b/b3/Bench_press_starting_position.png")
            st.subheader("Bench Press")
            st.write("Proper form: Lower bar to mid-chest. Focus on power.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/e/e4/Dumbbell_Fly.png")
            st.subheader("Dumbbell Flys")
            st.write("Focus on the stretch at the bottom.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Back":
        with col_a:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/d/d7/Lat_pulldown_machine_01.jpg")
            st.subheader("Lat Pulldown")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/b/b2/Cable_Row.png")
            st.subheader("Seated Row")
            st.markdown('</div>', unsafe_allow_html=True)