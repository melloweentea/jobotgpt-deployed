import streamlit as st 
from st_paywall_mod.aggregate_auth import add_auth
from streamlit_pdf_reader import pdf_reader
import base64


st.set_page_config(page_title="Prompting Tutorial", page_icon="💬")
st.title("💬 Prompting Tutorial")

if "language" not in st.session_state:
    st.session_state.language = "thai"

if st.session_state.user_subscribed == False:
    if st.session_state.language == "english":
        st.write("You are not subscribed and are unable to access this resource. Please login with Google or pay the subscription fee using Stripe.")
    else:
        st.write("คุณยังไม่ได้สมัครสมาชิกและไม่สามารถเข้าถึง JobotGPT ได้ กรุณาเข้าสู่ระบบด้วย Google หรือชำระค่าสมัครสมาชิกผ่าน Stripe")
        
add_auth(required=True)

if st.session_state.language == "english":
    st.write(f"You are currently subscribed to {st.session_state.tier}, enjoy the provided content.")
elif st.session_state.language == "thai":
    st.write(f"คุณได้สมัครสมาชิกในระดับ {st.session_state.tier} แล้ว สามารถดูเนื้อหาที่มีให้")

if st.session_state.tier == "tier 1":
    pdf_reader("prompt_tutorial/tier_1.pdf")
elif st.session_state.tier == "tier 2":
    pdf_reader("prompt_tutorial/tier_2.pdf")
elif st.session_state.tier == "tier 3":
    pdf_reader("prompt_tutorial/tier_3.pdf")

