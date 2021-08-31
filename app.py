import streamlit as st
import pickle
import pandas as pd
import os



st.set_page_config('Dress Recommendation System')
dress_dict=pd.read_csv("python1.csv")
simalri=pd.read_csv("final.csv")





 

st.title('Dress Recommendation System')
options = dress_dict['Dress_type']
index = st.selectbox("Which kind of dress you are looking for?", range(len(options)), format_func=lambda x: options[x])


def recommend(index):
  csr=[]
  for i in simalri.iloc[index]:
     csr.append(dress_dict.iloc[i])
  return csr



if st.button('Show Recommendation'):
	recommendation=recommend(index)
	recommendation=pd.DataFrame(recommendation)
	title_container = st.container()
	col1, col2 = st.columns([1, 2])

	with title_container:
          with col1:
                  st.text(" ")

          with col2:
            st.image(recommendation['Image'].values[0])
            st.markdown('<p style="text-align: -webkit-auto; font-weight:bold;">{}</p>'.format(recommendation['Dress_type'].values[0]),unsafe_allow_html=True)
            st.markdown('<p style="text-align:-webkit-auto;">{}</p>'.format(recommendation['Brand'].values[0]),unsafe_allow_html=True)
            st.markdown('<p style="text-align: -webkit-auto;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color:565959;">₹{}</span></p>'.format(recommendation['Disc_price'].values[0],recommendation['Actual_price'].values[0]), unsafe_allow_html=True)
	
	st.markdown('<p style="font-size: 1.2rem;">Products related to this item:</p>', unsafe_allow_html=True)


	count = 1
	for i in range(4):
	    for j in st.columns(3):

	        if count == 10:
	            break
	        with j:
	            st.image(recommendation['Image'].values[count])
	            st.markdown('<p style="text-align: center; font-weight:bold;">{}</p>'.format(recommendation['Dress_type'].values[count]),
	unsafe_allow_html=True)
	            st.markdown('<p style="text-align:center;">{}</p>'.format(recommendation['Brand'].values[count]),
	unsafe_allow_html=True)
	            st.markdown('<p style="text-align: center;"><span style="font-size: 18px;color: #B12704;">₹{}</span>&nbsp;<span style="color: grey; text-decoration: line-through; color:#565959;">₹{}</span></p>'.format(recommendation['Disc_price'].values[count],recommendation['Actual_price'].values[count]), unsafe_allow_html=True)
	            count += 1
