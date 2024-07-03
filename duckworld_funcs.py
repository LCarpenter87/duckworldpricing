import streamlit as st 
import psycopg2
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stodo import to_do
import pandas as pd 
from psycopg2 import sql
import os
import random
from datetime import datetime, time

def display_time_based_warning():
    current_time = datetime.now().time()
    morning_end = time(6, 0)    
    evening_start = time(22, 0) 
    
    if (current_time >= evening_start or current_time <= morning_end):
        st.warning('Duck World is currently CLOSED', icon="⚠️")


def raining_ducks():
    rain(
        emoji="🦆",
        font_size=70,
        falling_speed=2,
        animation_length=5,
    )

@st.cache_data
def fetch_data_to_dataframe():
    connection = psycopg2.connect(
            dbname="pagila",
            user=st.secrets['sql_user'],
            password=st.secrets['sql_password'],
            host=st.secrets['host'],
            port=5432
        )
    cursor = connection.cursor()
    select_query = sql.SQL("SELECT * FROM main.duckworld")
    cursor.execute(select_query)
    data = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    cursor.close()
    connection.close()

    return pd.DataFrame(data, columns=colnames)

def to_do_list():
    to_do(
            [(st.write, "🎟️ Buy a ticket")],
            "tickets",
        )
    to_do(
            [(st.write, "🦆 Visit the ducks")],
            "ducks",
        )
    to_do(
            [(st.write, "🍦 Buy ice cream")],
            "work",
        )
    
def get_random_image():
    files = os.listdir("assets")
    jpeg_files = [file for file in files if file.endswith('.jpg') or file.endswith('.jpeg')]
    random_image = random.choice(jpeg_files)    
    return os.path.join("assets", random_image)