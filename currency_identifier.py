import streamlit as st
from langchain_helper import generate_currency_and_places_of_interest

st.title('Currency Identifier')

country = st.sidebar.selectbox("Pick a Country", ("US", "UK", "France", "Japan", "China", "Italy", "Holland",
                                        "Germany", "Russia", "Spain", "Thailand", "Singapore"))

if country:
    response = generate_currency_and_places_of_interest(country)
    st.header(response["currency"])
    places_of_interest = response["Places_of_interest"].split(",")
    st.write("***Places of Interest***")
    for place in places_of_interest:
        st.write(" - ", place)

