import streamlit as st 
import psycopg2
import pandas as pd
from psycopg2 import sql, OperationalError
import plotly.express as px
from streamlit_extras.let_it_rain import rain

st.set_page_config(
   page_title="DuckWorld Price Monitoring",
   page_icon="🦆",
   layout="wide",
   initial_sidebar_state="collapsed",
)

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

st.title('🦆Duck World Dynamic Pricing!!🦆')

cola, colb = st.columns([3, 1])

with cola:

    st.write("""DuckWorld uses controversial dynamic pricing to rip off consumers.""")
    st.write("Use this handy chart to compare duck feed prices and ensure you get a great deal!""")

with colb:
    ducks = st.button("Click for ducks")

if ducks:
    raining_ducks()


df = fetch_data_to_dataframe()

## Clean the dataframe
df['datetime'] = pd.to_datetime(df['pricedate'].astype(str) + ' ' + df['pricetime'].astype(str))
df.set_index('datetime', inplace=True)
df.drop(columns=['pricedate', 'pricetime'], inplace=True)


avg_price = df['price'].mean()
min_price = df['price'].min()
max_price = df['price'].max()

col1, col2 = st.columns([3, 1])


with col1:
    fig = px.line(df, x=df.index, y='price', title='DuckWorld Feed Prices £ over time', labels={'x': 'Date & Time', 'price': 'Price'})
    st.plotly_chart(fig)


with col2:
    st.write("## Statistics")
    st.write(f"**Average Price:** £{avg_price:.2f}")
    st.write(f"**Min Price:** £{min_price:.2f}")
    st.write(f"**Max Price:** £{max_price:.2f}")


st.write("This is an unofficial duckworld price monitoring tool. We're not liable for any decision you make using it, nor any mistakes. Consult with a professional before buying a stake in duck feed.")