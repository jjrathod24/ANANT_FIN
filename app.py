import streamlit as st
from pathlib import Path

st.set_page_config(page_title="MF Advisor Pro", page_icon="📈", layout="wide")

# ── Hide Streamlit default UI ──
st.markdown("""<style>
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding: 0 !important;}
</style>""", unsafe_allow_html=True)

# ── Login ──
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.markdown("""
    <style>
    .login-box {
        max-width: 380px; margin: 8vh auto; padding: 2.5rem;
        border: 1px solid #ddd; border-radius: 12px;
        background: white; box-shadow: 0 2px 16px rgba(0,0,0,0.08);
    }
    .login-title { font-size: 22px; font-weight: 600; color: #0C447C; margin-bottom: 4px; }
    .login-sub   { font-size: 13px; color: #888; margin-bottom: 1.5rem; }
    </style>
    <div class="login-box">
      <div class="login-title">📈 MF Advisor Pro</div>
      <div class="login-sub">Please login to continue</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("login"):
        user = st.text_input("Username")
        pwd  = st.text_input("Password", type="password")
        btn  = st.form_submit_button("Login", use_container_width=True)

    if btn:
        if user == st.secrets["USERNAME"] and pwd == st.secrets["PASSWORD"]:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid username or password.")

# ── Main App ──
else:
    html = Path("calculator.html").read_text(encoding="utf-8")
    st.components.v1.html(html, height=900, scrolling=True)

    if st.sidebar.button("🔒 Logout"):
        st.session_state.logged_in = False
        st.rerun()
