import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Page Config (Sirf aik baar top par)
st.set_page_config(page_title="Ultimate Health Suite", page_icon="🛡️", layout="wide")

# 2. Session State Initialization
if 'total_calories' not in st.session_state:
    st.session_state.total_calories = 0
    st.session_state.total_protein = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []

st.title("🛡️ Ultimate Health & Fitness Suite")
st.markdown("Aapka personal assistant jo BMI, Gym Fee aur Workout sab manage karega.")

# 3. Sidebar for User Data
st.sidebar.header("👤 Your Profile")
age = st.sidebar.number_input("Age:", value=25)
gender = st.sidebar.radio("Gender:", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg):", value=70.0)
height = st.sidebar.number_input("Height (cm):", value=170.0)
goal = st.sidebar.selectbox("Goal:", ["Lose Weight", "Gain Muscle", "Maintain"])

# --- TABS SYSTEM ---
tab1, tab2, tab3 = st.tabs(["📊 Lec 1: BMI & Diet", "🏋️ Lec 2: Gym Dashboard", "🏃 Lec 3: Workout Plans"])

# --- TAB 1: LEC 1 (BMI & DIET) ---
with tab1:
    st.header("Body Composition & Diet")
    bmi = weight / ((height/100) ** 2)
    
    if gender == "Male": bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else: bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Your BMI", f"{bmi:.2f}")
        if bmi < 18.5: st.warning("Underweight")
        elif 18.5 <= bmi < 25: st.success("Normal Weight")
        else: st.error("Overweight")
        
    with c2:
        st.metric("Your BMR", f"{int(bmr)} kcal")

    st.divider()
    st.subheader("💧 Water & 🍱 Food Log")
    col_w, col_f = st.columns(2)
    with col_w:
        if st.button("🥤 Add Water Glass"):
            st.session_state.water_glasses += 1
        st.write(f"Glasses: {st.session_state.water_glasses} / 10")
        st.progress(min(st.session_state.water_glasses / 10, 1.0))
    
    with col_f:
        food_db = {"Roti": 120, "Rice": 200, "Chicken": 239, "Egg": 78, "Dal": 180}
        item = st.selectbox("Select Food:", list(food_db.keys()))
        if st.button("Add to Diary"):
            st.session_state.total_calories += food_db[item]
            st.success(f"{item} added!")
        st.metric("Total Calories", f"{st.session_state.total_calories} kcal")

# --- TAB 2: LEC 2 (GYM DASHBOARD) ---
with tab2:
    st.header("🏋️ Gym Management Dashboard")
    st.subheader("💰 Gym Fee Status")
    col_fee1, col_fee2 = st.columns(2)
    with col_fee1:
        fee_date = st.date_input("Last Fee Paid Date", datetime.now())
    with col_fee2:
        status = st.selectbox("Payment Status", ["Paid", "Pending"])
    
    if status == "Paid": st.success(f"Fees clear! Paid on: {fee_date}")
    else: st.error("Please clear your dues.")

    st.divider()
    st.subheader("📅 Gym Attendance")
    attendance = st.multiselect("Days present this week:", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    st.info(f"Attendance: {len(attendance)} days.")

# --- TAB 3: LEC 3 (WORKOUT PLANS) ---
with tab3:
    st.header("Exercise Suggestions")
    if goal == "Lose Weight":
        st.info("🔥 Cardio focus")
        st.write("- 30 mins Running")
    elif goal == "Gain Muscle":
        st.info("💪 Strength focus")
        st.write("- Pushups & Squats")
    else:
        st.info("🧘 Flexibility focus")
        st.write("- Yoga & Walking")

# --- RESET BUTTON ---
if st.sidebar.button("Reset Daily Progress", type="primary"):
    st.session_state.total_calories = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []
    st.rerun()