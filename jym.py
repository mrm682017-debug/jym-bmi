import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime, timedelta

# Page Config
st.set_page_config(page_title="Elite Gym Library", page_icon="💪", layout="wide")

# Session State for Admin
if 'gym_members' not in st.session_state:
    st.session_state.gym_members = []

# --- SIDEBAR ---
menu = st.sidebar.radio("Main Menu", ["📊 Fitness Tools", "👥 Admin Manager", "📚 Full Exercise Dictionary"])

# --- SECTION 1: TOOLS ---
if menu == "📊 Fitness Tools":
    st.title("⚖️ BMI & Health")
    w = st.number_input("Weight (kg)", 40.0, 200.0, 70.0)
    h = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    if st.button("Calculate"):
        bmi = w / ((h/100)**2)
        st.metric("BMI", f"{bmi:.1f}")

# --- SECTION 2: ADMIN MANAGER (WITH FEE DAYS LEFT) ---
elif menu == "👥 Admin Manager":
    st.title("👥 Member Ledger & Fee Tracker")
    
    with st.form("admin"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Member Name")
            fee = st.selectbox("Fee Status", ["Paid ✅", "Pending ❌"])
        with col2:
            # Fee jis din jama ki
            pay_date = st.date_input("Fee Payment Date", datetime.now())
            day = st.selectbox("Today's Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        
        if st.form_submit_button("Save Member Record"):
            # Expiry date calculate ho rahi hai (30 din baad)
            expiry_date = pay_date + timedelta(days=30)
            st.session_state.gym_members.append({
                "Name": name,
                "Fee Status": fee,
                "Paid On": pay_date,
                "Expires On": expiry_date,
                "Day": day
            })
            st.success(f"{name} ka record save ho gaya!")

    # Table Display logic
    if st.session_state.gym_members:
        st.subheader("📋 Active Members Status")
        
        display_data = []
        today = datetime.now().date()

        for member in st.session_state.gym_members:
            # Din baaki calculate karna
            days_left = (member["Expires On"] - today).days
            
            status_msg = ""
            if days_left > 0:
                status_msg = f"{days_left} Din Baaki Hain"
            elif days_left == 0:
                status_msg = "Aaj Last Day Hai! ⚠️"
            else:
                status_msg = f"Expired ({abs(days_left)} din pehle) ❌"

            display_data.append({
                "Member Name": member["Name"],
                "Fee Status": member["Fee Status"],
                "Paid Date": member["Paid On"],
                "Expiry Date": member["Expires On"],
                "Remaining Time": status_msg
            })

        df = pd.DataFrame(display_data)
        st.dataframe(df, use_container_width=True)

# --- SECTION 3: EXERCISE DICTIONARY (Chest focus) ---
elif menu == "📚 Full Exercise Dictionary":
    st.title("📖 Complete Exercise Library")
    
    exercises_data = {
        "Chest (Hekal)": [
            {"name": "Flat Bench Press", "desc": "Overall chest mass."},
            {"name": "Incline Barbell Press", "desc": "Upper chest focus."},
            {"name": "Decline Barbell Press", "desc": "Lower chest focus."},
            {"name": "Dumbbell Flys", "desc": "Chest stretch and width."},
            {"name": "Cable Crossovers", "desc": "Inner chest definition."},
            {"name": "Chest Dips", "desc": "Lower chest power."},
            {"name": "Machine Press", "desc": "Targeted squeeze."},
            {"name": "Push-Ups", "desc": "Bodyweight power."}
        ],
        "Back": [{"name": "Lat Pulldown", "desc": "Width."}, {"name": "Seated Rows", "desc": "Thickness."}],
        "Arms": [{"name": "Bicep Curls", "desc": "Size."}, {"name": "Tricep Pushdown", "desc": "Shape."}]
    }

    selected_muscle = st.selectbox("Choose Muscle Group", list(exercises_data.keys()))
    ex_list = exercises_data[selected_muscle]
    
    for i in range(0, len(ex_list), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(ex_list):
                with cols[j]:
                    st.info(f"**{ex_list[i+j]['name']}**\n\n{ex_list[i+j]['desc']}")