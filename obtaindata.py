import requests 
from datetime import datetime, timedelta 
import psycopg2
import os 
from dotenv import load_dotenv

load_dotenv()

def insert_data(current_date, current_time, price ):
    connection = psycopg2.connect(
      dbname="pagila",
      user= os.getenv('sql_user'),
      password=os.getenv('sql_password'),
      host=os.getenv('host'),
      port="5432"
        )
    cursor = connection.cursor()
    insert_statement = (f"""
            INSERT INTO main.duckworld (pricedate, pricetime, price)
            values ('{current_date}', '{current_time}', {price});            
        """)      
    cursor.execute(insert_statement)
    connection.commit()
    cursor.close()
    connection.close()

duckworld = os.getenv('duckworld')
response = requests.get(duckworld).json()

price = response['price']
current_date = (timedelta(hours=1) + datetime.now()).date().strftime("%Y-%m-%d")
current_time = (timedelta(hours=1) + datetime.now()).time().strftime("%H:%M:%S")

# Sometimes the price is None when DuckWorld is shut
if price not None:
    insert_data(current_date, current_time, price)
