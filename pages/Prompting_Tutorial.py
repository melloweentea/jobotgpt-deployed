import streamlit as st 
from st_paywall_mod.aggregate_auth import add_auth


st.set_page_config(page_title="Prompting Tutorial", page_icon="💬")
st.title("💬 Prompting Tutorial")

if st.session_state.user_subscribed == False:
    if st.session_state.language == "english":
        st.write("You are not subscribed and are unable to access this resource. Please login with Google or pay the subscription fee using Stripe.")
    else:
        st.write("คุณยังไม่ได้สมัครสมาชิกและไม่สามารถเข้าถึง JobotGPT ได้ กรุณาเข้าสู่ระบบด้วย Google หรือชำระค่าสมัครสมาชิกผ่าน Stripe")
        
# st.video()
add_auth(required=True)

if st.session_state.language == "english":
    st.write(f"You are currently subscribed to {st.session_state.tier}, enjoy the provided content.")
elif st.session_state.language == "thai":
    st.write(f"คุณได้สมัครสมาชิกในระดับ {st.session_state.tier} แล้ว สามารถดูเนื้อหาที่มีให้")

if st.session_state.language == "english":
    if st.session_state.tier == "tier 1":
        st.write("Tier 1 content will be available soon")
    elif st.session_state.tier == "tier 2":
        st.write("Tier 2 content will be available soon")
    elif st.session_state.tier == "tier 3":
        st.write("Tier 3 content will be available soon")
elif st.session_state.language == "thai":
    if st.session_state.tier == "tier 1":
        st.write("เนื้อหา Tier 1 จะพร้อมให้บริการเร็วๆ นี้")
    elif st.session_state.tier == "tier 2":
        st.write("เนื้อหา Tier 2 จะพร้อมให้บริการเร็วๆ นี้")
    elif st.session_state.tier == "tier 3":
        st.write("เนื้อหา Tier 3 จะพร้อมให้บริการเร็วๆ นี้")
