import streamlit as st 
import pandas as pd
import plotly.express as px
from streamlit_extras.let_it_rain import rain
from streamlit_extras.stodo import to_do
import duckworld_funcs as dw
import os
import random


st.set_page_config(
   page_title="DuckWorld Price Monitoring",
   page_icon="🦆",
   layout="wide",
   initial_sidebar_state="collapsed",
)

st.title('🦆Duck World Dynamic Pricing!!🦆')

cola, colb = st.columns([3, 1])
with cola:
    st.write("""DuckWorld uses controversial dynamic pricing to rip off consumers.""")
    st.write("Use this handy chart to compare duck feed prices and ensure you get a great deal!""")

with colb:
    ducks = st.button("Click for ducks")

if ducks:
    dw.raining_ducks()


df = dw.fetch_data_to_dataframe()

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


st.divider()

col3, col4 = st.columns(2)

with col3:
    st.write("Your perfect DuckWorld Day Out to do list")
    dw.to_do_list()

with col4:
    random_image_path = dw.get_random_image()
    st.image(random_image_path, caption='Live View from Duck World', use_column_width=True)

