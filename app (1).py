import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from fpdf import FPDF
import datetime

# ---------- FIREBASE SETUP ----------
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase-key.json")  # Upload this file to your repo root
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Business Connect Hub", page_icon="💼", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background-color: #fffaf0;
}
h1, h2, h3 {
    color: #b8860b;
}
.sidebar .sidebar-content {
    background-color: #fff8dc;
}
.stButton>button {
    background-color: #FFD700;
    color: black;
    border-radius: 10px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #ffcc00;
    color: white;
}
.post-box {
    background-color: #fff8dc;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.comment {
    background-color: #fff;
    border-left: 3px solid #b8860b;
    padding: 5px 10px;
    margin-top: 5px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# ---------- AUTH SYSTEM ----------
def register_user():
    st.subheader("📝 Register")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        db.collection("users").add({"name": name, "email": email, "password": password})
        st.success("Account created successfully! You can now log in.")
        st.session_state.page = "login"

def login_user():
    st.subheader("🔐 Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        users = db.collection("users").where("email", "==", email).where("password", "==", password).stream()
        if any(users):
            st.session_state.logged_in = True
            st.session_state.email = email
            st.success("Login successful ✅")
        else:
            st.error("Invalid credentials ❌")
    st.write("Don’t have an account?")
    if st.button("Create one"):
        st.session_state.page = "register"

# ---------- BUSINESS PROFILE ----------
def business_profile():
    st.title("💼 Business Profile Generator")
    company = st.text_input("Company Name")
    industry = st.selectbox("Industry", ["Technology", "Fashion", "Agriculture", "Finance", "Other"])
    description = st.text_area("Business Description")
    goal = st.text_input("Business Goal")
    contact = st.text_input("Contact Info")

    if st.button("Generate Profile"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Business Profile for {company}", ln=True, align="C")
        pdf.cell(200, 10, txt=f"Industry: {industry}", ln=True)
        pdf.multi_cell(0, 10, txt=f"Description: {description}")
        pdf.cell(200, 10, txt=f"Goal: {goal}", ln=True)
        pdf.cell(200, 10, txt=f"Contact: {contact}", ln=True)
        pdf.output("profile.pdf")

        with open("profile.pdf", "rb") as f:
            st.download_button("📄 Download Profile PDF", f, file_name="business_profile.pdf")

# ---------- COMMUNITY FEED ----------
def community_feed():
    st.title("🌍 Business Community Feed")

    post_content = st.text_area("Share something with the community...")
    if st.button("Post"):
        if post_content:
            db.collection("posts").add({
                "email": st.session_state.email,
                "content": post_content,
                "timestamp": datetime.datetime.now(),
                "likes": 0,
                "comments": []
            })
            st.success("Posted successfully!")

    st.markdown("---")

    posts = db.collection("posts").order_by("timestamp", direction=firestore.Query.DESCENDING).stream()
    for post in posts:
        data = post.to_dict()
        st.markdown(f"<div class='post-box'><b>{data['email']}</b><br>{data['content']}</div>", unsafe_allow_html=True)

        if st.button(f"👍 Like ({data['likes']})", key=post.id):
            db.collection("posts").document(post.id).update({"likes": data['likes'] + 1})

        comment = st.text_input("💬 Add a comment", key=f"comment_{post.id}")
        if st.button("Send", key=f"send_{post.id}"):
            new_comment = {"text": comment, "user": st.session_state.email}
            db.collection("posts").document(post.id).update({
                "comments": firestore.ArrayUnion([new_comment])
            })
        if "comments" in data:
            for c in data["comments"]:
                st.markdown(f"<div class='comment'><b>{c['user']}:</b> {c['text']}</div>", unsafe_allow_html=True)

# ---------- NAVIGATION ----------
if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st. sidebar.title("📱 Navigation")
if st.session_state.logged_in:
    choice = st.sidebar.radio("Go to", ["Profile Generator", "Community"])
    if choice == "Profile Generator":
        business_profile()
    elif choice == "Community":
        community_feed()
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
else:
    if st.session_state.page == "login":
        login_user()
    elif st.session_state.page == "register":
        register_user()
