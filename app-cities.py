import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('World Major Cities')

df = pd.read_csv('worldcities.csv')
population_filter = st.slider('minimal population', 0, 40, 10) # min, max, default

capital_filter = st.sidebar.multiselect('capital filter', df.capital.unique(), df.capital.unique()) #default is all the options

form = st.sidebar.form('country-form')
country_filter = form.text_input('Enter Country Name:', 'ALL')
form.form_submit_button('Apply')

df = df[df.population>population_filter] # population filter

df = df[df.capital.isin(capital_filter)] # capital filter

if country_filter != 'ALL': # country filter
    df = df[df.country==country_filter]

st.map(df)
st.write(df[['city', 'country', 'population']])

pop_sum = df.groupby('country').sum()['population']
fig, ax = plt.subplots(figsize=(20, 5))
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)