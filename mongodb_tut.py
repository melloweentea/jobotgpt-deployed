import streamlit as st 
from pymongo import MongoClient
import os 
import pprint

connection_string = st.secrets["MONGO_AUTH"]
client = MongoClient(connection_string)

dbs = client.list_database_names()
jobot_db = client.jobotgpt 
collections = jobot_db.list_collection_names()

#inserting document
def insert_doc(test_doc: dict):
    collection = client.jobotgpt.usage 
    collection.insert_one(test_doc)
    
doc = {"Time": "2024-06-02 20:00:30", "Email": "naratsarun.tha@gmail.com", "Total_Tokens": 990, "Total_Cost": 0.000504}
insert_doc(doc)