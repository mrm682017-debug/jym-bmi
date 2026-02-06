import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Pro Gym Dictionary", page_icon="🏋️‍♂️", layout="wide")

# Custom CSS for App-like Card Layout
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
    h1, h2 { color: #1f1f1f; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DASHBOARD ---
st.sidebar.title("📑 GYM DASHBOARD")
menu = st.sidebar.radio("Main Menu", ["Lec 1: Fitness Tools", "Lec 2: Gym Manager", "📚 Full Exercise Dictionary"])

# --- SECTION 1: LEC 1 (HEALTH TOOLS) ---
if menu == "Lec 1: Fitness Tools":
    st.title("📊 Health Tools")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
        st.subheader("BMI Calculator")
        w = st.number_input("Weight (kg)", value=70.0)
        h = st.number_input("Height (cm)", value=170.0)
        if st.button("Calculate BMI"):
            bmi = w / ((h/100)**2)
            st.metric("Score", f"{bmi:.1f}")
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
        st.subheader("Water Intake")
        if 'water' not in st.session_state: st.session_state.water = 0
        if st.button("Add Glass"): st.session_state.water += 1
        st.progress(min(st.session_state.water/10, 1.0))
        st.write(f"Logged: {st.session_state.water} / 10")
        st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 2: LEC 2 (GYM MANAGER) ---
elif menu == "Lec 2: Gym Manager":
    st.title("💳 Management")
    st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
    st.subheader("Member Status")
    f_status = st.selectbox("Fee Status", ["Paid", "Pending"])
    if f_status == "Paid": st.success("Membership Active")
    else: st.error("Membership Expired")
    att = st.multiselect("Attendance Tracker", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- SECTION 3: FULL EXERCISE DICTIONARY (IMAGE CARDS) ---
elif menu == "📚 Full Exercise Dictionary":
    st.title("📖 Complete Gym Exercise Dictionary")
    muscle = st.selectbox("Select Muscle Group", ["Chest", "Back", "Shoulders", "Legs", "Arms (Biceps/Triceps)", "Abs & Core"])
    
    col1, col2 = st.columns(2)

    if muscle == "Chest":
        with col1:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/360/Male/l/360_1.jpg")
            st.subheader("Bench Press")
            st.write("Target: Chest Mass. Proper form: Lower bar to mid-chest.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/380/Male/l/380_1.jpg")
            st.subheader("Dumbbell Flys")
            st.write("Target: Chest Stretch. Keep elbows slightly bent.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Back":
        with col1:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/10/Male/l/10_1.jpg")
            st.subheader("Lat Pulldowns")
            st.write("Target: Back Width. Pull down to upper chest.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/28/Male/l/28_1.jpg")
            st.subheader("Seated Cable Rows")
            st.write("Target: Back Thickness. Squeeze shoulder blades.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Shoulders":
        with col1:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/48/Male/l/48_1.jpg")
            st.subheader("Shoulder Press")
            st.write("Target: Overall Shoulder. Keep core tight.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/373/Male/l/373_1.jpg")
            st.subheader("Lateral Raises")
            st.write("Target: Side Shoulder. Don't swing the weights.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Arms (Biceps/Triceps)":
        with col1:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/138/Male/l/138_1.jpg")
            st.subheader("Bicep Curls")
            st.write("Target: Biceps. Full range of motion.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/345/Male/l/345_1.jpg")
            st.subheader("Triceps Pushdown")
            st.write("Target: Triceps. Keep elbows tucked in.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Legs":
        with col1:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/43/Male/l/43_1.jpg")
            st.subheader("Barbell Squats")
            st.write("Target: Quads & Glutes. The king of leg exercises.")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
            st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/53/Male/l/53_1.jpg")
            st.subheader("Leg Press")
            st.write("Target: Legs. Control the weight on the way down.")
            st.markdown('</div>', unsafe_allow_html=True)

    elif muscle == "Abs & Core":
        st.markdown('<div class="exercise-card">', unsafe_allow_html=True)
        st.image("https://www.bodybuilding.com/exercises/exerciseImages/sequences/148/Male/l/148_1.jpg")
        st.subheader("Crunches")
        st.write("Target: Abs. Squeeze your core on every rep.")
        st.markdown('</div>', unsafe_allow_html=True)