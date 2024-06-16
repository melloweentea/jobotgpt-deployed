import streamlit as st
import stripe 
from pymongo import MongoClient
from .google_auth import get_logged_in_user_email, show_login_button
from .stripe_auth import is_active_subscriber, redirect_button, get_api_key
from .buymeacoffee_auth import get_bmac_payers

payment_provider = st.secrets.get("payment_provider", "stripe")

connection_string = st.secrets["MONGO_AUTH"]
client = MongoClient(connection_string)

def add_auth(
    required: bool = True,
    login_button_text: str = "Login with Google",
    login_button_color: str = "#FD504D",
    login_sidebar: bool = True,

):
    if required:
        require_auth(
            login_button_text=login_button_text,
            login_sidebar=login_sidebar,
            login_button_color=login_button_color,
        )
    else:
        optional_auth(
            login_button_text=login_button_text,
            login_sidebar=login_sidebar,
            login_button_color=login_button_color,
        )

def require_auth(
    login_button_text: str = "Login with Google",
    login_button_color: str = "#FD504D",
    login_sidebar: bool = True,
):
    user_email = get_logged_in_user_email()

    if not user_email:
        show_login_button(
            text=login_button_text, color=login_button_color, sidebar=login_sidebar
        )
        login_popup()
        
        if st.sidebar.button("ไทย/ENG"):
            if st.session_state.language == "thai":
                st.session_state.language = "english"
            else:
                st.session_state.language = "thai"
                
        st.stop()
    
    if payment_provider == "stripe":
        is_subscriber = user_email and is_active_subscriber(user_email)
    elif payment_provider == "bmac":
        is_subscriber = user_email and user_email in get_bmac_payers()
    else:
        raise ValueError("payment_provider must be 'stripe' or 'bmac'")
    
    if st.secrets.testing_mode == True:
        link_1 = st.secrets["stripe_link_test"]
        link_2 = st.secrets["stripe_link_test_2"]
        link_3 = st.secrets["stripe_link_test_3"]
    else:
        link_1 = st.secrets["stripe_link"]
        link_2 = st.secrets["stripe_link_2"]
        link_3 = st.secrets["stripe_link_3"]
    @st.experimental_dialog("Subscribe!")
    
    def subscribe_popup():
        col1, col2, col3 = st.columns([1/3, 1/3, 1/3])
        with col1:
            redirect_button(
                text="Tier 1 JobotGPT (Standard) ⭐️",
                customer_email=user_email,
                payment_link=link_1,
                sidebar=False,
                payment_provider=payment_provider,
            )
            st.write("4,560฿ / 6 เดือน")
        with col2:
            redirect_button(
                text="Tier 2 JobotGPT Pro (Bestseller) ⭐️⭐️",
                customer_email=user_email,
                payment_link=link_2,
                sidebar=False,
                payment_provider=payment_provider,
            )
            st.write("7,890฿ / 1 ปี")
        with col3:
            redirect_button(
                text="Tier 3 JobotGPT Elite (Best Value) ⭐️⭐️⭐️",
                customer_email=user_email,
                payment_link=link_3,
                sidebar=False,
                payment_provider=payment_provider,
            )
            st.write("14,560฿ / 2 ปี")
        st.write("")
    
    if not is_subscriber:
        subscribe_popup()
        redirect_button(
            text="Subscribe to tier 1",
            customer_email=user_email,
            payment_link=link_1,
            sidebar=True,
            payment_provider=payment_provider,
        )
        redirect_button(
            text="Subscribe to tier 2 ⭐️",
            customer_email=user_email,
            payment_link=link_2,
            sidebar=True,
            payment_provider=payment_provider,
        )
        redirect_button(
            text="Subscribe to tier 3",
            customer_email=user_email,
            payment_link=link_3,
            sidebar=True,
            payment_provider=payment_provider,
        )
        st.session_state.user_subscribed = False
        
        if st.sidebar.button("ไทย/ENG"):
            if st.session_state.language == "thai":
                st.session_state.language = "english"
            else:
                st.session_state.language = "thai"
                
        st.stop()
    elif is_subscriber:
        st.session_state.user_subscribed = True
        
        if st.session_state.subscriptions.data[0].plan.amount == 456000:
            st.session_state.tier = "tier 1"
            redirect_button(
                text="Subscribe to tier 2 ⭐️",
                customer_email=user_email,
                payment_link=link_2,
                sidebar=True,
                payment_provider=payment_provider,
            )
            redirect_button(
                text="Subscribe to tier 3",
                customer_email=user_email,
                payment_link=link_3,
                sidebar=True,
                payment_provider=payment_provider,
            )
        elif st.session_state.subscriptions.data[0].plan.amount == 789000:
            st.session_state.tier = "tier 2"
            redirect_button(
                text="Subscribe to tier 3",
                customer_email=user_email,
                payment_link=link_3,
                sidebar=True,
                payment_provider=payment_provider,
            )
        elif st.session_state.subscriptions.data[0].plan.amount == 1456000 or st.session_state.subscriptions.data[0].plan.amount == 59900:
            st.session_state.tier = "tier 3"
        
        #add user to database
        collection = client.jobotgpt.users
        docs = collection.find({"Email": st.session_state.email})
        count = 0
        for doc in docs:
            count += 1
        if count == 0:
            collection.insert_one({"Email": st.session_state.email, "Tier": st.session_state.tier, "Currency": st.session_state.subscriptions.data[0].currency})
        
        if st.sidebar.button("Cancel subscription", type="primary"):
            stripe.api_key = get_api_key()
            stripe.Subscription.cancel(st.session_state.subscriptions.data[0].id)
            

    if st.sidebar.button("Logout", type="primary"):
        del st.session_state.email
        del st.session_state.user_subscribed
        st.rerun()
    
    if st.sidebar.button("ไทย/ENG"):
        if st.session_state.language == "thai":
            st.session_state.language = "english"
        elif st.session_state.language == "english":
            st.session_state.language = "thai"

@st.experimental_dialog("Login with Google")
def login_popup():
    col1, col2, col3 = st.columns([0.3, 0.4, 0.3])
    with col2:
        show_login_button(text="Login with Google", color="#FD504D", sidebar=False)
    st.write("")

def optional_auth(
    login_button_text: str = "Login with Google",
    login_button_color: str = "#FD504D",
    login_sidebar: bool = True,
):
    user_email = get_logged_in_user_email()
    if payment_provider == "stripe":
        is_subscriber = user_email and is_active_subscriber(user_email)
    elif payment_provider == "bmac":
        is_subscriber = user_email and user_email in get_bmac_payers()
    else:
        raise ValueError("payment_provider must be 'stripe' or 'bmac'")

    if not user_email:
        show_login_button(
            text=login_button_text, color=login_button_color, sidebar=login_sidebar
        )
        st.session_state.email = ""
        st.sidebar.markdown("")

    if not is_subscriber:
        redirect_button(
            text="Subscribe now!", customer_email="", payment_provider=payment_provider
        )
        st.sidebar.markdown("")
        st.session_state.user_subscribed = False

    elif is_subscriber:
        st.session_state.user_subscribed = True

    if st.session_state.email != "":
        if st.sidebar.button("Logout", type="primary"):
            del st.session_state.email
            del st.session_state.user_subscribed
            st.rerun()
