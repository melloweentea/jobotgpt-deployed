import streamlit as st 
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma, FAISS
from langchain_community.document_loaders.merge import MergedDataLoader
from langchain_community.document_loaders import SpiderLoader, PyPDFLoader, WebBaseLoader, DirectoryLoader, CSVLoader
from langchain_community.vectorstores.utils import filter_complex_metadata
from langchain_community.callbacks import get_openai_callback
from langchain_community.utilities import GoogleSearchAPIWrapper
from langchain_core.tools import Tool
from dotenv import load_dotenv
import os
from st_paywall_mod.aggregate_auth import add_auth
from time import strftime, localtime
from pymongo import MongoClient
from gtts import gTTS
from langdetect import detect 
from io import BytesIO

#note: run using python -m streamlit run app.py instead 
#to resolve import of local package add path of folder to python.analysis.extraPaths cmd+, to search it in settings

connection_string = st.secrets["MONGO_AUTH"]
client = MongoClient(connection_string)

load_dotenv()
FAISS_PATH = "faiss_data"
CHROMA_PATH = "chroma_data"
DIR_PATH_TXT = "data/txt"
DIR_PATH_CSV = 'data/csv'

os.environ['OPENAI_API_KEY'] = st.secrets["API_KEY_JO"]
os.environ["GOOGLE_CSE_ID"] = st.secrets["GOOGLE_CSE_ID"]
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "user_subscribed" not in st.session_state:
    st.session_state.user_subscribed = False 

if "language" not in st.session_state:
    st.session_state.language = "thai"

st.set_page_config(page_title="JobotGPT", page_icon="🤖")

col1, mid, col2 = st.columns([1,2,20])
with col1:
    st.image("photo_2024-05-24_20-22-49.jpg", output_format="JPEG", width=100)
with col2:
    st.title("JobotGPT")

placeholder = st.empty()
if st.session_state.user_subscribed == False:
    with placeholder.container():
        if st.session_state.language == "english":
            st.write("You are not subscribed and are unable to access JobotGPT. Please login with Google or pay the subscription fee using Stripe.")
        else: 
            st.write("คุณยังไม่ได้สมัครสมาชิกและไม่สามารถเข้าถึง JobotGPT ได้ กรุณาเข้าสู่ระบบด้วย Google หรือชำระค่าสมัครสมาชิกผ่าน Stripe")

#hide footer made with streamlit 
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

add_auth(required=True)

if st.session_state.user_subscribed == True:
    placeholder.empty()
    if st.session_state.language == "english":
        st.write(f"You are subscribed! Welcome {st.session_state.email}")
    else:
        st.write(f"คุณได้สมัครสมาชิกเรียบร้อยแล้ว! ยินดีต้อนรับ {st.session_state.email}")

# st.write(st.session_state.subscriptions.data[0].id)
# st.write(st.session_state.subscriptions.data[0].currency)
# st.write(st.session_state)

#streamlit conversation 
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

#get response
def get_response(query, chat_history, context):
    template = """
    You are a helpful customer assistance bot, helping people with algorithmic trading. You should also be able to generate code.
    If you are given input in Thai, reply in Thai. If you are given input in English, reply in English. Do not include AIMessage in the message.
    Answer the following questions in detail using the following context and chat history:
    
    Context: {context}
    
    Chat history: {chat_history}
    
    User question: {user_question}
    """
    # prompt = ChatPromptTemplate.from_template(template)
    
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
    
    # print(template.format(context=context, chat_history=chat_history, user_question=query))  
    
    return llm.stream(template.format(context=context, chat_history=chat_history, user_question=query))

def stream_response(response):
    for chunk in response:
        yield chunk.content

def get_token_info_brute(query, chat_history, context):
    template = """
    You are a helpful customer assistance bot, helping people with algorithmic trading. You should also be able to generate code.
    If you are given input in Thai, reply in Thai. If you are given input in English, reply in English. Do not include AIMessage in the message.
    Answer the following questions in detail using the following context and chat history:
    
    Context: {context}
    
    Chat history: {chat_history}
    
    User question: {user_question}
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125")
    
    with get_openai_callback() as cb:
        result = llm.invoke(template.format(context=context, chat_history=chat_history, user_question=query))
        return cb.total_cost, cb.total_tokens
        

def get_token_info_streaming(stream):
    aggregate = None
    for chunk in stream:
        aggregate = chunk if aggregate is None else aggregate + chunk
    return aggregate.usage_metadata

#inserting document
def insert_doc(test_doc: dict):
    collection = client.jobotgpt.usage 
    collection.insert_one(test_doc)

#google search 
def google_search(prompt):
    search = GoogleSearchAPIWrapper()
    tool = Tool(
        name="google_search", 
        description="Search Google for recent results related to the prompt.", 
        func=search.run,
    )
    return tool.run(prompt)
    
#user input
user_query = st.chat_input("Your question")
if user_query is not None and user_query != "":
    load_db = FAISS.load_local(FAISS_PATH, OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    context = load_db.max_marginal_relevance_search(user_query, k=3)
    context_text = "\n\n---\n\n".join([doc.page_content for doc in context])
    
    st.session_state.chat_history.append(HumanMessage(user_query))
    
    with st.chat_message("Human"):
        st.markdown(user_query)
        
    with st.chat_message("AI"):
        ai_response = st.write_stream(stream_response(get_response(user_query, st.session_state.chat_history, context_text)))
        # st.write(google_search(user_query))
        mp3 = BytesIO()
        tts = gTTS(ai_response, lang=detect(ai_response))
        tts.write_to_fp(mp3)
        st.audio(mp3)
            
    st.session_state.chat_history.append(AIMessage(ai_response))
    
    #recording info in google sheets 
    # conn = st.connection("gsheets", type=GSheetsConnection)
    # df = conn.read(worksheet="Sheet1", usecols=[0,1,2,3])
    # df_cleaned = df.dropna()
    # df_new = pd.DataFrame(usage_data, index=[0])
    # df_concat = pd.concat([df_cleaned, df_new])
    # conn.update(worksheet="Sheet1", data=df_concat)
    # st.dataframe(df_concat)
    
    total_cost, total_tokens = get_token_info_brute(user_query, st.session_state.chat_history, context_text)
    usage_data = {"Time": strftime("%Y-%m-%d %H:%M:%S", localtime()), 
                  "Tier": st.session_state.tier, 
                  "Email":st.session_state.email, 
                  "Total_Tokens": total_tokens * 2, 
                  "Total_Cost": total_cost * 2, 
                  "Currency": st.session_state.subscriptions.data[0].currency}
    insert_doc(usage_data)
    


    

