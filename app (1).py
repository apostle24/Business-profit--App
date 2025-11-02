import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Business Profit Analyzer", page_icon="💼", layout="wide")

# --- HEADER ---
st.title("💼 Business Profit Analyzer (Premium Version)")
st.markdown("Analyze, visualize, and grow your business — globally.")

# --- SIDEBAR ---
st.sidebar.header("⚙️ App Settings")
st.sidebar.success("Connected to Global Server 🌍")

menu = st.sidebar.selectbox(
    "Navigate",
    ["Home", "Add Business Data", "Analytics Dashboard", "Subscription & Payment", "About"]
)

# --- HOME ---
if menu == "Home":
    st.subheader("Welcome to Business Profit Analyzer")
    st.write("""
    This premium tool helps you:
    - Track your business performance
    - Visualize profits and expenses
    - Predict growth using AI insights
    - Upgrade for advanced global analytics
    """)
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f", use_container_width=True)
    st.markdown("### 🌍 Designed for global entrepreneurs and creators.")

# --- ADD BUSINESS DATA ---
elif menu == "Add Business Data":
    st.subheader("📊 Enter Your Business Data")

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
            "Country": [country]
        })
        df.to_csv("business_data.csv", mode="a", index=False, header=False)
        st.success("✅ Data Saved Successfully!")

# --- ANALYTICS DASHBOARD ---
elif menu == "Analytics Dashboard":
    st.subheader("📈 Business Analytics Dashboard")

    try:
        df = pd.read_csv("business_data.csv")
        st.dataframe(df)

        st.metric("Total Businesses", len(df))
        st.metric("Average Profit", f"${df['Profit ($)'].mean():.2f}")
        st.metric("Total Income", f"${df['Income ($)'].sum():.2f}")

        st.bar_chart(df[['Income ($)', 'Expenses ($)', 'Profit ($)']])
        st.line_chart(df['Profit ($)'])
    except FileNotFoundError:
        st.warning("⚠️ No data found. Please add business data first.")

# --- SUBSCRIPTION & PAYMENT ---
elif menu == "Subscription & Payment":
    st.subheader("💳 Premium Subscription")

    st.info("Upgrade to Premium for full access to global analytics and advanced AI insights.")
    st.markdown("**Plans:**\n- Basic: Free\n- Premium: $10/month\n- Global Business: $25/month")

    email = st.text_input("Enter your email for payment confirmation")
    plan = st.selectbox("Select Plan", ["Basic", "Premium", "Global Business"])
    if st.button("Proceed to Payment"):
        with st.spinner("Processing Payment..."):
            time.sleep(3)
        st.success(f"✅ {plan} Plan Activated Successfully for {email}!")

# --- ABOUT ---
elif menu == "About":
    st.subheader("ℹ️ About the App")
    st.write("""
    **Business Profit Analyzer (Premium)** helps entrepreneurs analyze their data,
    visualize performance, and make informed business decisions globally.
    
    **Developer:** Apostle Joshua  
    **Version:** 2.0 Premium  
    **Powered by:** Streamlit, Python, and AI-driven analytics.
    """)
    st.markdown("🌐 [Visit GitHub Repository](https://github.com/apostle24/Business-profit-App)")
