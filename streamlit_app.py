# ghost_bank_app.py
# Full app implementation 
import streamlit as st
import json
import os
import random
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from cryptography.fernet import Fernet

# ----------------------------- INIT -----------------------------

def load_data():
    if os.path.exists("user_data.json"):
        with open("user_data.json", "r") as file:
            return json.load(file)
    else:
        return {
            "name": "Ghost Seeker",
            "balance": 500,
            "debt": 0,
            "savings": 0,
            "investments": 0,
            "spending_history": [],
            "vault_locked": True,
            "time_capsules": [],
            "challenges_completed": []
        }

def save_data(data):
    with open("user_data.json", "w") as file:
        json.dump(data, file)

user_data = load_data()

# ----------------------------- STYLES -----------------------------

st.markdown("""
    <style>
    body, .reportview-container, .main {{
        background-color: #0a0a0a;
        color: #33FFB2;
        font-family: 'Courier New', monospace;
    }}
    .stButton>button {{
        background-color: #111111;
        color: #33FFB2;
        border-radius: 10px;
        padding: 10px;
    }}
    </style>
""", unsafe_allow_html=True)

# ----------------------------- FUNCTIONS -----------------------------

# 1. Black Mirror Budget AI
def budget_ai():
    st.subheader("Black Mirror Budget AI")
    total_spent = sum([x['amount'] for x in user_data['spending_history']])
    days = len(set([x['date'] for x in user_data['spending_history']])) or 1
    avg_spending = total_spent / days
    warning_msg = ""

    if avg_spending > 80:
        warning_msg = "You’re on track to be overdrawn in 3 days. Reduce night spending."
    if warning_msg:
        st.error(warning_msg)

# 2. ShadowMarket Scanner (mocked data)
def shadow_market():
    st.subheader("ShadowMarket Scanner")
    tracked_items = {"Milk": 1.20, "Eggs": 2.10, "Bread": 1.50}
    local_prices = {"Milk": 1.35, "Eggs": 2.00, "Bread": 1.75}  # Mocked
    for item in tracked_items:
        delta = local_prices[item] - tracked_items[item]
        if delta > 0:
            st.warning(f"{item} price up {round((delta/tracked_items[item])*100)}%. Alternatives available.")

# 3. Timeline Collapse Mode
def timeline_mode():
    st.subheader("Timeline Collapse Mode")
    choices = ["Eat Out Daily", "Cook at Home", "Invest Spare Change", "Ignore Savings"]
    timeline = {}
    for choice in choices:
        if choice == "Eat Out Daily":
            timeline[choice] = -1000
        elif choice == "Cook at Home":
            timeline[choice] = 800
        elif choice == "Invest Spare Change":
            timeline[choice] = 1500
        elif choice == "Ignore Savings":
            timeline[choice] = -600

    choice = st.selectbox("Choose a path to reveal fate:", choices)
    st.write(f"6-month Projection: {'Gain' if timeline[choice] > 0 else 'Loss'} of £{abs(timeline[choice])}")

# 4. Redacted Risk Analysis
def risk_analysis():
    st.subheader("Redacted Risk Analysis")
    decision = st.text_input("Enter a financial decision:")
    if decision:
        score = random.randint(0, 99)
        st.code(f"R-{score:02d}: Risk classified.")
        if st.button("Override Warning"):
            st.warning("Proceed at your own risk. Trail logged.")

# 5. Ghost Mode
def ghost_mode():
    st.subheader("Ghost Mode")
    if st.button("Burn the Trail"):
        os.remove("user_data.json")
        st.success("All session history deleted.")

# 6. Time Capsules
def time_capsules():
    st.subheader("Time Capsules")
    if st.button("Bury a Thought Capsule"):
        capsule = st.text_area("What's on your mind?")
        user_data['time_capsules'].append({"msg": capsule, "time": str(datetime.datetime.now())})
        st.success("Sealed away. Will reveal when you return.")

# 7. Finance Glitch Generator
def finance_glitch():
    st.subheader("Finance Glitch Generator")
    if st.button("Simulate System Glitch"):
        glitch_value = random.randint(-200, 500)
        user_data['balance'] += glitch_value
        st.info(f"System error: £{glitch_value} {'added' if glitch_value >=0 else 'removed'} from account.")

# ----------------------------- UI -----------------------------

st.title("🧊 Ghost Bank")
st.caption("""Where money meets mystery.
A terminal into the financial shadows.
""")

menu = st.sidebar.selectbox("Enter a Chamber:", [
    "Dashboard", "Black Mirror Budget AI", "ShadowMarket Scanner", "Timeline Collapse Mode",
    "Redacted Risk Analysis", "Ghost Mode", "Time Capsules", "Finance Glitch Generator"
])

if menu == "Dashboard":
    st.header("Welcome, Ghost Seeker")
    st.metric("Balance", f"£{user_data['balance']}")
    st.metric("Debt", f"£{user_data['debt']}")
    st.metric("Savings", f"£{user_data['savings']}")

elif menu == "Black Mirror Budget AI":
    budget_ai()
elif menu == "ShadowMarket Scanner":
    shadow_market()
elif menu == "Timeline Collapse Mode":
    timeline_mode()
elif menu == "Redacted Risk Analysis":
    risk_analysis()
elif menu == "Ghost Mode":
    ghost_mode()
elif menu == "Time Capsules":
    time_capsules()
elif menu == "Finance Glitch Generator":
    finance_glitch()

save_data(user_data)
