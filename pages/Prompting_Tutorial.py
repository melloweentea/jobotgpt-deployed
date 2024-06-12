import streamlit as st 
from st_paywall_mod.aggregate_auth import add_auth


st.set_page_config(page_title="Prompting Tutorial", page_icon="💬")
st.title("💬 Prompting Tutorial")

if st.session_state.user_subscribed == False:
    st.write("You are not subscribed and are unable to access this resource. Please login with Google or pay the subscription fee using Stripe.")
    
# st.video()
add_auth(required=True)

st.write(f"You are currently subscribed to {st.session_state.tier}, enjoy the provided content.")

if st.session_state.tier == "tier 1":
    st.write("Tier 1 content will be available soon")
elif st.session_state.tier == "tier 2":
    st.write("Tier 2 content will be available soon")
elif st.session_state.tier == "tier 3":
    st.write("Tier 3 content will be available soon")
