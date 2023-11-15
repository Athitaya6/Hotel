import streamlit as st 

st.title('พฤติกรรมการจองโรงแรมของลูกค้า')
st.header('นางสาวอฑิตยา กะการดี')
st.subheader('สาขาวิทยาการข้อมูล')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
#with col1:
    #st.image('./pic/k1.jpg')
#with col2:
    #st.image('./pic/iris.jpg')
    

html_1="""
<div style="background-color:#63D767;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การจองโรงแรม</h5></center>
</div>
"""    
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('data/CleanHotel.csv')
st.write(dt.head(10))

dt1 = dt['no adults'].sum()
dt2 = dt['no children'].sum()
dt3 = dt['weekend ss'].sum()
dt4 = dt['week mf'].sum()
dt5 = dt['meal plan'].sum()
dt6 = dt['car parking'].sum()
dt7 = dt['leadtime'].sum()
dt8 = dt['arrival year'].sum()
dt9 = dt['arrival month'].sum()
dt10 = dt['arrival date'].sum()
dt11 = dt['market segment'].sum()
dt12 = dt['repeated guest'].sum()
dt13 = dt['cancellations'].sum()
dt14 = dt['bookings not canceled'].sum()
dt15 = dt['avg price'].sum()
dt16 = dt['special requests'].sum()
dt17 = dt['booking_status'].sum()

dx = [dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8, dt9, dt10, dt11, dt12, dt13, dt14, dt15, dt16, dt17]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4", "dt5", "dt6", "dt7", "dt8", "dt9", "dt10", "dt11", "dt12", "dt13", "dt14", "dt15", "dt16", "dt17"])

if st.button("show bar chart"):
   st.bar_chart(dx2)
   st.button("Not show bar chart")
else :
   st.button("Not show bar chart")
   
   
html_2 = """
<div style="background-color:#6CE9E8;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายพฤติกรรมการจองโรงแรม</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

ptlen = st.slider("จำนวนผู้ใหญ่ no adults",0,10)
ptwd = st.slider("จำนวนเด็ก no children",0,10)

splen = st.number_input("กรุณาเลือกข้อมูล sepal.length")
spwd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

if st.button("ทำนายผล"):
    #ทำนาย
    #dt = pd.read_csv("./data/iris.csv") 
    X = dt.drop('variety', axis=1)
    y = dt.variety 
    st.button("ไม่ทำนายผล")

    DTT_model = DecisionTreeClassifier (criterion='gini')
    DTT_model.fit(X, y)

#ข้อมูลสำหรับทดลองจำแนกข้อมูล
    x_input = np.array([[ptlen, ptwd, splen, spwd]])

#เอา input ไปทดสอบ
    st.write(Knn_model.predict(x_input))
    out=Knn_model.predict(x_input)

    if out[0]=="Setosa":    
        st.image("./pic/iris1.jpg")
        st.header("Setosa")
    elif out[0]=="Versicolor":
        st.image("./pic/iris2.jpg")
        st.header("Versicolor")
    else:
        st.image("./pic/iris3.jpg") 
        st.header("Versicolor") 
    st.button("ไม่ทำนาย")
else:
    st.button("ไม่ทำนาย")