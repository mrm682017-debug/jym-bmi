import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="Ultimate Health Suite", page_icon="🛡️", layout="wide")

# Session State Initialization
if 'total_calories' not in st.session_state:
    st.session_state.total_calories = 0
    st.session_state.total_protein = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []

st.title("🛡️ Ultimate Health & Fitness Suite")
st.markdown("Aapka personal assistant jo BMI, Gym Fee aur Workout sab manage karega.")

# Sidebar for User Data
st.sidebar.header("👤 Your Profile")
age = st.sidebar.number_input("Age:", value=25)
gender = st.sidebar.radio("Gender:", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg):", value=70.0)
height = st.sidebar.number_input("Height (cm):", value=170.0)
goal = st.sidebar.selectbox("Goal:", ["Lose Weight", "Gain Muscle", "Maintain"])

# --- NEW TABS SYSTEM (Organized by Lectures) ---
tab1, tab2, tab3 = st.tabs(["📊 Lec 1: BMI & Diet", "🏋️ Lec 2: Gym Dashboard", "🏃 Lec 3: Workout Plans"])

# --- TAB 1: LEC 1 (BMI & DIET) ---
with tab1:
    st.header("Body Composition & Diet")
    # BMI Calculation
    bmi = weight / ((height/100) ** 2)
    
    # BMR Calculation
    if gender == "Male": bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else: bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Your BMI", f"{bmi:.2f}")
        if bmi < 18.5: st.warning("Underweight")
        elif 18.5 <= bmi < 25: st.success("Normal Weight")
        else: st.error("Overweight")
        
    with c2:
        st.metric("Your BMR (Base Calories)", f"{int(bmr)} kcal")

    st.divider()

    # Water & Food Section (Existing)
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
            cals = food_db[item]
            st.session_state.total_calories += cals
            st.success(f"{item} added!")
        st.metric("Total Calories", f"{st.session_state.total_calories} kcal")

# --- TAB 2: LEC 2 (GYM DASHBOARD) ---
with tab2:
    st.header("🏋️ Gym Management Dashboard")
    
    # Gym Fee Tracker
    st.subheader("💰 Gym Fee Status")
    col_fee1, col_fee2 = st.columns(2)
    with col_fee1:
        fee_date = st.date_input("Last Fee Paid Date", datetime.now())
    with col_fee2:
        status = st.selectbox("Payment Status", ["Paid", "Pending"])
    
    if status == "Paid":
        st.success(f"Aapki fee {fee_date} ko jama ho chuki hai.")
    else:
        st.error("Meharbani karke apni gym fee jama karwayein.")

    st.divider()

    # Attendance Tracker
    st.subheader("📅 Gym Attendance")
    attendance = st.multiselect("Is hafte aap kin dino gym gaye?", 
                               ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    st.info(f"Aap is hafte **{len(attendance)}** din gym gaye hain.")

# --- TAB 3: LEC 3 (WORKOUT PLANS) ---
with tab3:
    st.header("Exercise Suggestions")
    if goal == "Lose Weight":
        st.info("🔥 Focus: Cardio & Fat Burn")
        st.write("- 30 mins Running\n- 15 mins Jumping Jacks")
    elif goal == "Gain Muscle":
        st.info("💪 Focus: Strength Training")
        st.write("- Pushups: 3x15\n- Squats: 3x20")
    else:
        st.info("🧘 Focus: Flexibility")
        st.write("- Yoga for 20 mins\n- Brisk Walking")

# Reset Button
if st.sidebar.button("Reset Daily Progress", type="primary"):
    st.session_state.total_calories = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []
    st.rerun()import streamlit as st
import pandas as pd
from datetime import datetime

# Page Config
st.set_page_config(page_title="Ultimate Health Suite", page_icon="🛡️", layout="wide")

# Session State Initialization
if 'total_calories' not in st.session_state:
    st.session_state.total_calories = 0
    st.session_state.total_protein = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []

st.title("🛡️ Ultimate Health & Fitness Suite")
st.markdown("Aapka personal assistant jo BMI, Gym Fee aur Workout sab manage karega.")

# Sidebar for User Data
st.sidebar.header("👤 Your Profile")
age = st.sidebar.number_input("Age:", value=25)
gender = st.sidebar.radio("Gender:", ["Male", "Female"])
weight = st.sidebar.number_input("Weight (kg):", value=70.0)
height = st.sidebar.number_input("Height (cm):", value=170.0)
goal = st.sidebar.selectbox("Goal:", ["Lose Weight", "Gain Muscle", "Maintain"])

# --- NEW TABS SYSTEM (Organized by Lectures) ---
tab1, tab2, tab3 = st.tabs(["📊 Lec 1: BMI & Diet", "🏋️ Lec 2: Gym Dashboard", "🏃 Lec 3: Workout Plans"])

# --- TAB 1: LEC 1 (BMI & DIET) ---
with tab1:
    st.header("Body Composition & Diet")
    # BMI Calculation
    bmi = weight / ((height/100) ** 2)
    
    # BMR Calculation
    if gender == "Male": bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else: bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric("Your BMI", f"{bmi:.2f}")
        if bmi < 18.5: st.warning("Underweight")
        elif 18.5 <= bmi < 25: st.success("Normal Weight")
        else: st.error("Overweight")
        
    with c2:
        st.metric("Your BMR (Base Calories)", f"{int(bmr)} kcal")

    st.divider()

    # Water & Food Section (Existing)
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
            cals = food_db[item]
            st.session_state.total_calories += cals
            st.success(f"{item} added!")
        st.metric("Total Calories", f"{st.session_state.total_calories} kcal")

# --- TAB 2: LEC 2 (GYM DASHBOARD) ---
with tab2:
    st.header("🏋️ Gym Management Dashboard")
    
    # Gym Fee Tracker
    st.subheader("💰 Gym Fee Status")
    col_fee1, col_fee2 = st.columns(2)
    with col_fee1:
        fee_date = st.date_input("Last Fee Paid Date", datetime.now())
    with col_fee2:
        status = st.selectbox("Payment Status", ["Paid", "Pending"])
    
    if status == "Paid":
        st.success(f"Aapki fee {fee_date} ko jama ho chuki hai.")
    else:
        st.error("Meharbani karke apni gym fee jama karwayein.")

    st.divider()

    # Attendance Tracker
    st.subheader("📅 Gym Attendance")
    attendance = st.multiselect("Is hafte aap kin dino gym gaye?", 
                               ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    st.info(f"Aap is hafte **{len(attendance)}** din gym gaye hain.")

# --- TAB 3: LEC 3 (WORKOUT PLANS) ---
with tab3:
    st.header("Exercise Suggestions")
    if goal == "Lose Weight":
        st.info("🔥 Focus: Cardio & Fat Burn")
        st.write("- 30 mins Running\n- 15 mins Jumping Jacks")
    elif goal == "Gain Muscle":
        st.info("💪 Focus: Strength Training")
        st.write("- Pushups: 3x15\n- Squats: 3x20")
    else:
        st.info("🧘 Focus: Flexibility")
        st.write("- Yoga for 20 mins\n- Brisk Walking")

# Reset Button
if st.sidebar.button("Reset Daily Progress", type="primary"):
    st.session_state.total_calories = 0
    st.session_state.water_glasses = 0
    st.session_state.history = []
