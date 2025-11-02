# app.py
import streamlit as st
from datetime import datetime
import pandas as pd
import io
import os
from fpdf import FPDF

# Try to import firebase admin — optional (for permanent DB)
use_firebase = False
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    use_firebase = True
except Exception:
    use_firebase = False

# ----------------- Style / Theme -----------------
gold = "#c79a3d"
dark = "#0f1724"
accent = gold
st.set_page_config(page_title="ProfitSense AI", page_icon="💼", layout="wide")

st.markdown(f"""
<style>
/* page background */
body {{ background-color: #fbfbfb; }}
h1, h2, h3, .streamlit-expanderHeader {{ color: {dark}; }}
.reportview-container .main .block-container{{ padding-top:1rem; padding-left:2rem; padding-right:2rem; }}
.stButton>button {{ background-color: {accent}; border-radius:10px; color: #fff; }}
.stDownloadButton>button {{ background-color: {accent}; border-radius:10px; color: #fff; }}
.sidebar .sidebar-content {{ background-color: #ffffff; }}
</style>
""", unsafe_allow_html=True)

# ----------------- Firebase initialization (optional) -----------------
db = None
if use_firebase:
    try:
        if not firebase_admin._apps:
            if os.path.exists("firebase_key.json"):
                cred = credentials.Certificate("firebase_key.json")
                firebase_admin.initialize_app(cred)
                db = firestore.client()
            else:
                # firebase module available but no key file uploaded
                db = None
        else:
            db = firestore.client()
    except Exception as e:
        db = None
        print("Firebase init error:", e)

# ----------------- Helpers -----------------
def save_user_firestore(email, name, password):
    if db:
        db.collection("users").document(email).set({
            "name": name,
            "email": email,
            "password": password,
            "premium": False,
            "created_at": datetime.utcnow()
        })
        return True
    return False

def get_user_firestore(email):
    if db:
        doc = db.collection("users").document(email).get()
        if doc.exists:
            return doc.to_dict()
    return None

def set_user_premium(email):
    if db:
        db.collection("users").document(email).update({"premium": True})
        return True
    return False

def save_prediction_firestore(user_email, inputs, result):
    if db:
        db.collection("predictions").add({
            "user": user_email,
            "inputs": inputs,
            "result": result,
            "timestamp": datetime.utcnow()
        })
        return True
    return False

def append_csv_local(filename, df):
    header = not os.path.exists(filename)
    df.to_csv(filename, mode="a", index=False, header=header)

def read_csv_local(filename):
    if os.path.exists(filename):
        return pd.read_csv(filename)
    return pd.DataFrame()

def create_pdf_binary(text: str):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in text.split("\n"):
        pdf.cell(0, 8, txt=line, ln=True)
    b = pdf.output(dest='S').encode('latin-1')  # return bytes
    return b

# ----------------- Session State -----------------
if "user" not in st.session_state:
    st.session_state.user = None  # dict with keys: email,name,premium
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- Top Banner / Landing -----------------
col1, col2 = st.columns([2,1])
with col1:
    st.image("https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1200&q=80", use_container_width=True)
    st.title("ProfitSense AI — Business Profit Predictor")
    st.markdown("**Predict profits, get actionable steps, and scale your business.**")
    st.markdown("---")
    st.markdown("**How it helps:**")
    st.write("""
    - Fast profit prediction based on spending and business inputs.  
    - Clear explanation and next-step suggestions.  
    - Save results, download reports, and upgrade for advanced analytics.
    """)
    st.markdown("---")
with col2:
    st.markdown("<div style='border-radius:8px;padding:12px;background:#fff;box-shadow:0 2px 6px rgba(0,0,0,0.06)'>"
                f"<h3 style='color:{dark}'>Get started</h3>"
                "<p>Register or login to save your results and access premium features.</p>"
                f"<p style='margin-top:8px'><a href='#' style='background:{accent};padding:8px 12px;border-radius:8px;color:#fff;text-decoration:none;'>Try Demo</a></p>"
                "</div>", unsafe_allow_html=True)

# ----------------- Sidebar (contact + quick links) -----------------
with st.sidebar:
    st.image("https://faithconncthub.store/wp-content/uploads/2024/12/logo.png", width=140)
    st.markdown(f"### ProfitSense AI")
    st.markdown("AI-powered business profit predictions")
    st.markdown("---")
    if st.session_state.logged_in:
        st.markdown(f"**Logged in:** {st.session_state.user.get('name')}  \n**Email:** {st.session_state.user.get('email')}")
        st.write("Premium:" , "✅" if st.session_state.user.get("premium") else "❌")
        if st.button("Logout"):
            st.session_state.user = None
            st.session_state.logged_in = False
            st.experimental_rerun()
    else:
        st.markdown("**Not logged in**")
    st.markdown("---")
    st.markdown("**Support & Contact**")
    st.write("📧 nbjoshua8@gmail.com")
    st.write("📱 +233 55 623 1984")
    st.markdown("[Instagram @nbjoshua6](https://instagram.com/nbjoshua6)")
    st.markdown("[Website](https://faithconncthub.store)")
    st.markdown("---")
    st.markdown(f"[Upgrade / Support on Selar](https://selar.com/showlove/nbjoshua)")

# ----------------- Navigation -----------------
page = st.sidebar.radio("Navigate", ["Home", "Register", "Login", "Predict", "History", "Premium", "About"])

# ----------------- Pages -----------------
# ----- Register -----
if page == "Register":
    st.header("Create an account")
    name = st.text_input("Full name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        if not email or not password or not name:
            st.error("Enter name, email and password")
        else:
            # check firestore
            if db:
                if get_user_firestore(email):
                    st.error("User already exists — try login.")
                else:
                    save_user_firestore(email, name, password)
                    st.success("Account created. Please login.")
            else:
                # local fallback: append to users.csv
                users_df = read_csv_local("users.csv")
                if not users_df.empty and email in users_df['email'].astype(str).tolist():
                    st.error("User exists. Login instead.")
                else:
                    new = pd.DataFrame([{"name":name,"email":email,"password":password,"premium":False,"created_at":datetime.utcnow()}])
                    append_csv_local("users.csv", new)
                    st.success("Account created (local). Please login.")

# ----- Login -----
elif page == "Login":
    st.header("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user_data = None
        if db:
            u = get_user_firestore(email)
            if u and u.get("password") == password:
                user_data = u
        else:
            users_df = read_csv_local("users.csv")
            if not users_df.empty:
                row = users_df[users_df['email'] == email]
                if not row.empty and row.iloc[0]['password'] == password:
                    user_data = row.iloc[0].to_dict()

        if user_data:
            st.session_state.user = {
                "name": user_data.get("name"),
                "email": user_data.get("email"),
                "premium": user_data.get("premium", False)
            }
            st.session_state.logged_in = True
            st.success("Login successful.")
            st.experimental_rerun()
        else:
            st.error("Invalid credentials or user not found.")

# ----- Home -----
elif page == "Home":
    st.header("Welcome to ProfitSense AI")
    st.video("https://www.youtube.com/watch?v=QH2-TGUlwu4", start_time=5)  # example; replace with your demo video
    st.markdown("### Quick demo")
    st.write("Enter a few business inputs on the Predict page to get a quick estimate.")

# ----- Predict -----
elif page == "Predict":
    st.header("Predict Business Profit")
    st.markdown("Enter your business inputs. Use the sliders and fields for better UX.")
    with st.form("predict_form"):
        biz_name = st.text_input("Business Name")
        industry = st.selectbox("Industry", ["E-commerce","Tech","Agriculture","Fashion","Other"])
        rd = st.number_input("R&D Spend (USD)", min_value=0.0, step=10.0, value=10000.0)
        admin = st.number_input("Administration Spend (USD)", min_value=0.0, step=10.0, value=5000.0)
        marketing = st.number_input("Marketing Spend (USD)", min_value=0.0, step=10.0, value=15000.0)
        submitted = st.form_submit_button("Run Prediction")

    if submitted:
        # Simple weighted formula as placeholder model (replace with your ML model)
        prediction_value = rd*0.45 + marketing*0.4 + admin*0.15
        result_text = ""
        if prediction_value > 30000:
            result_text = "High Success Potential 🚀"
        elif prediction_value > 15000:
            result_text = "Moderate Potential ⚡"
        else:
            result_text = "Needs Improvement 💡"

        st.success(f"Predicted Profit Score: {prediction_value:,.2f}")
        st.info(f"Result: {result_text}")
        st.markdown("#### Why this result?")
        st.write("- Marketing weight is high: invest in targeted campaigns.\n- R&D helps product quality.\n- Control admin costs to raise margins.")

        # Save result (Firestore or local)
        inputs = {"biz_name": biz_name, "industry": industry, "rd": rd, "admin": admin, "marketing": marketing}
        if st.session_state.logged_in:
            user_email = st.session_state.user.get("email")
            # save to firestore or local csv
            saved = False
            if db:
                try:
                    save_prediction_firestore(user_email, inputs, {"value": prediction_value, "label": result_text})
                    saved = True
                except Exception:
                    saved = False
            if not saved:
                df = pd.DataFrame([{
                    "user": user_email,
                    "biz_name": biz_name,
                    "industry": industry,
                    "rd": rd,
                    "admin": admin,
                    "marketing": marketing,
                    "prediction_value": prediction_value,
                    "result": result_text,
                    "timestamp": datetime.utcnow()
                }])
                append_csv_local("predictions.csv", df)
            st.success("✅ Result saved to your account.")
        else:
            st.warning("Login to save results to your account and access history.")

        # Download PDF
        pdf_text = f"Business: {biz_name}\nIndustry: {industry}\nPrediction Score: {prediction_value:,.2f}\nResult: {result_text}\n\nGenerated: {datetime.utcnow()}"
        pdf_bytes = create_pdf_binary(pdf_text)
        st.download_button("📥 Download Result (PDF)", data=pdf_bytes, file_name="profit_prediction.pdf", mime="application/pdf")

# ----- History -----
elif page == "History":
    st.header("Your Saved Predictions")
    if not st.session_state.logged_in:
        st.warning("Please login to view history.")
    else:
        user_email = st.session_state.user.get("email")
        if db:
            docs = db.collection("predictions").where("user","==",user_email).stream()
            rows = []
            for d in docs:
                doc = d.to_dict()
                rows.append({
                    "biz_name": doc.get("inputs",{}).get("biz_name"),
                    "industry": doc.get("inputs",{}).get("industry"),
                    "prediction_value": doc.get("result",{}).get("value"),
                    "result": doc.get("result",{}).get("label"),
                    "timestamp": doc.get("timestamp")
                })
            if rows:
                df = pd.DataFrame(rows)
                st.dataframe(df)
            else:
                st.info("No saved predictions yet.")
        else:
            df = read_csv_local("predictions.csv")
            if df.empty:
                st.info("No saved predictions yet (local storage).")
            else:
                df_user = df[df['user'] == user_email]
                if df_user.empty:
                    st.info("You have no saved predictions yet.")
                else:
                    st.dataframe(df_user)

# ----- Premium -----
elif page == "Premium":
    st.header("Premium Access")
    st.write("Premium gives you advanced analytics, CSV exports, and one-on-one consulting.")
    if st.session_state.logged_in and st.session_state.user.get("premium"):
        st.success("You have Premium access ✅")
        st.markdown("**Premium features:**")
        st.write("- CSV export of all predictions\n- Advanced charts and exportable reports\n- Priority consulting")
        # Export CSV for user
        if st.button("Export My Predictions (CSV)"):
            df = read_csv_local("predictions.csv")
            if not df.empty:
                df_user = df[df['user']==st.session_state.user.get("email")]
                if not df_user.empty:
                    csv = df_user.to_csv(index=False).encode('utf-8')
                    st.download_button("Download CSV", csv, file_name="my_predictions.csv", mime="text/csv")
                else:
                    st.info("No predictions to export.")
            else:
                st.info("No predictions saved yet.")
    else:
        st.info("Upgrade to Premium to unlock advanced features.")
        st.markdown("[👉 Buy Premium on Selar](https://selar.com/showlove/nbjoshua)")
        code = st.text_input("Enter premium code (if you have one)")
        if st.button("Activate"):
            if code.strip().upper() == "PREMIUM2025":
                if st.session_state.logged_in:
                    # Set premium locally and in firestore if available
                    st.session_state.user["premium"] = True
                    if db:
                        set_user_premium(st.session_state.user.get("email"))
                    # also update local users.csv if present
                    if os.path.exists("users.csv"):
                        users_df = pd.read_csv("users.csv")
                        users_df.loc[users_df['email'] == st.session_state.user.get("email"), 'premium'] = True
                        users_df.to_csv("users.csv", index=False)
                    st.success("Premium activated. Refresh app.")
                else:
                    st.warning("Please login first before activating.")

# ----- About -----
elif page == "About":
    st.header("About ProfitSense AI")
    st.write("""
    ProfitSense AI is built to help entrepreneurs and small businesses get quick, actionable profit predictions.
    Built by NB Joshua — contact: nbjoshua8@gmail.com
    """)
    st.image("https://images.unsplash.com/photo-1559526324-593bc073d938?w=1000&q=80", use_container_width=True)
    st.markdown("**Privacy**: We store only the information you provide. If you use Firebase, your data is saved securely. If not, data is saved locally to CSV in the app environment.")
