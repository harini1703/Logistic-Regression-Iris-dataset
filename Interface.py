import pickle
import streamlit as st


pickle_in=open('flowers .pkl','rb')
forecast=pickle.load(pickle_in)

a=st.number_input('Enter the Sepal Length' )
b=st.number_input('Enter the Sepal Width'  )
c=st.number_input('Enter the Petal length' )
d=st.number_input('Enter the Petal width' )

result=''
if st.button("Predict"):
     result=forecast.predict([[a,b,c,d]]).squeeze()
     if result==0:
          st.success("Setosa")
     elif result==1:
          st.success("Versicolor")
     else:
          st.success("Virginica")
   
   
