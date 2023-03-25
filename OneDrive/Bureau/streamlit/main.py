import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

header = st.container()
dataset = st.container()
features = st.container()
modeltraining = st.container()

with header :
	st.title('Welcome to my ansome data science project')
	st.text('In this project i look the boursiers mackets')

with dataset:
	st.header('data_finance')
	bitcoin = pd.read_csv('data/data_finance.csv', index_col='Date', parse_dates=True)
	st.write(bitcoin.head())
	st.subheader('bourses')
	st.bar_chart(bitcoin['Open'])
	st.bar_chart(bitcoin)
	st.subheader(' entrer en bourses')

	st.line_chart(bitcoin)
	st.area_chart(bitcoin)
	st.line_chart(bitcoin['Close']['2021'], width=0, height=1000)


	#bitcoin_data = st.dataframe(bitcoin, width=None, height=None, use_container_width=False)
	#st.line_chart()
#with features:
	#st.header('the features i created')


#with modeltraining:
	#st.header('time to train the model')
	#st.text('here you get to choose the hyperparameters of the model and see how the performance of model ')