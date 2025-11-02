import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Business Profit Analyzer", page_icon="💼", layout="wide")

# --- USER AUTH (SIMPLE VERSION) ---
# Temporary in-memory user storage
users = {"admin@gmail.com": {"password": "1234", "premium": True}}

def login_user(email, password):
    user = users.get(email)
    if user and user["password"] == password:
        return user
    return None

# --- LOGIN PAGE ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.session_state.premium = False

if not st.session_state.logged_in:
    st.title("🔐 Business Profit Analyzer Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = login_user(email, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.session_state.premium = user["premium"]
            st.success("✅ Login successful! Click 'Rerun' to enter app.")
            st.stop()
        else:
            st.error("❌ Invalid credentials.")
    st.info("Use demo login → Email: admin@gmail.com | Password: 1234")
    st.stop()

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("💼 Business Profit Analyzer")
menu = st.sidebar.radio("Navigate", ["Home", "Add Business Data", "Analytics Dashboard", "Subscription & Payment", "About"])
st.sidebar.write(f"👤 Logged in as: {st.session_state.user_email}")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.experimental_rerun()

# --- HOME PAGE ---
if menu == "Home":
    st.title("📊 Business Profit Analyzer (Premium)")
    st.write("""
    Welcome to the Premium Business Profit Analyzer App!
    - Add and analyze your business data.
    - Predict profits and growth.
    - Upgrade for unlimited access.
    """)

# --- ADD BUSINESS DATA ---
elif menu == "Add Business Data":
    st.subheader("📁 Enter Your Business Data")
    business_name = st.text_input("Business Name")
    income = st.number_input("Monthly Income ($)", min_value=0.0)
    expenses = st.number_input("Monthly Expenses ($)", min_value=0.0)
    staff_count = st.number_input("Number of Staff", min_value=0)
    country = st.text_input("Country")

    if st.button("Save Record"):
        df = pd.DataFrame({
            "Business Name": [business_name],
            "Income ($)": [income],
            "Expenses ($)": [expenses],
            "Profit ($)": [income - expenses],
            "Staff": [staff_count],
            "Country": [country],
            "User": [st.session_state.user_email]
        })
        df.to_csv("business_data.csv", mode="a", index=False, header=False)
        st.success("✅ Data saved successfully!")

# --- ANALYTICS DASHBOARD ---
elif menu == "Analytics Dashboard":
    st.subheader("📈 Business Analytics Dashboard")

    try:
        df = pd.read_csv("business_data.csv")
        df_user = df[df["User"] == st.session_state.user_email]
        if df_user.empty:
            st.warning("⚠️ You have no data yet.")
        else:
            st.dataframe(df_user)
            st.metric("Total Records", len(df_user))
            st.metric("Average Profit", f"${df_user['Profit ($)'].mean():.2f}")
            st.bar_chart(df_user[['Income ($)', 'Expenses ($)', 'Profit ($)']])
    except FileNotFoundError:
        st.warning("⚠️ No data file found yet. Add some business data first.")

# --- SUBSCRIPTION ---
elif menu == "Subscription & Payment":
    st.subheader("💳 Premium Subscription")
    if st.session_state.premium:
        st.success("✅ You already have Premium access.")
    else:
        st.info("Upgrade to Premium for full analytics and export features.")
        st.markdown("[👉 Buy Premium on Selar](https://selar.com/showlove/nbjoshua)")
        code = st.text_input("Enter Premium Code")
        if st.button("Activate Premium"):
            if code.strip().upper() == "PREMIUM2025":
                users[st.session_state.user_email]["premium"] = True
                st.session_state.premium = True
                st.success("✅ Premium Activated! Please refresh the app.")
            else:
                st.error("❌ Invalid Code. Please buy from Selar.")

# --- ABOUT ---
elif menu == "About":
    st.subheader("ℹ️ About This App")
    st.markdown("""
    **Business Profit Analyzer** helps entrepreneurs track profits, predict outcomes, and visualize performance.

    **Creator:** Apostle Joshua  
    **Instagram:** [@nbjoshua6](https://instagram.com/nbjoshua6)  
    **Website:** [faithconncthub.store](https://faithconncthub.store)  
    **Email:** nbjoshua8@gmail.com  
    **Phone:** +233556231984
    """)
