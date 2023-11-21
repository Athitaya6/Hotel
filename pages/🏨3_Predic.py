import streamlit as st 

st.markdown(
   f"""
   <h1 style= 'text-align: center;'>ระบบวิเคราะห์พฤติกรรมการจองโรงแรมของลูกค้า</h1>
   """,
   unsafe_allow_html=True
)
  
st.markdown("----")

col1, col2 = st.columns(2)
col1.write("นางสาวอฑิตยา กะการดี")
col2.write("สาขาวิทยาการข้อมูล")
with col1:
    st.image('./image/Aa.jpg')
with col2:
    st.image('./image/ds.jpg')
    

html_1="""
<div style="background-color:#63D767;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การจองโรงแรม</h5></center>
</div>
"""    
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

dt=pd.read_csv('./data/Hotel.csv')
st.write(dt.head(10))

dt1 = dt['no adults'].sum()
dt2 = dt['no children'].sum()
dt3 = dt['weekend ss'].sum()
dt4 = dt['week mf'].sum()
dt5 = dt['car parking'].sum()
dt6 = dt['leadtime'].sum()
dt7 = dt['arrival month'].sum()
dt8 = dt['arrival date'].sum()
dt9 = dt['special requests'].sum()
dt10 = dt['booking_status'].sum()

dx = [dt1, dt2, dt3, dt4, dt5, dt6, dt7, dt8, dt9, dt10]
dx2 = pd.DataFrame(dx, index=["dt1", "dt2", "dt3", "dt4", "dt5", "dt6", "dt7", "dt8", "dt9", "dt10"])
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

hadults = st.slider("จำนวนผู้ใหญ่ no adults",0,10)
hchildren = st.slider("จำนวนเด็ก no children",0,10)
hweekend = st.slider("วันเสาร์-อาทิตย์ weekend ss",0,2)
hweek = st.slider("วันจันทร์-ศุกร์ week mf",0,5)
hcar = st.slider("car parking",0,1)

htime = st.number_input("จำนวนวันตั้งแต่จอง leadtime")
hmonth = st.number_input("เดือนที่จอง arrival month")
hdate = st.number_input("วันที่จอง arrival date")
hspecial = st.number_input("คำขอพิเศษ special requests")


from sklearn.tree import DecisionTreeClassifier
import numpy as np

if st.button("ทำนายผล"):
    #ทำนาย
    dt = pd.read_csv('./data/Hotel.csv') 
    X = dt.drop('booking_status', axis=1)
    y = dt.booking_status 
    st.button("ไม่ทำนายผล")

    DTT_model = DecisionTreeClassifier (criterion='gini')
    DTT_model.fit(X, y)
    #st.write(X.shape)
#ข้อมูลสำหรับทดลองจำแนกข้อมูล
    x_input = np.array([[hadults, hchildren, hweekend, hweek, hcar, htime, hmonth, hdate, hspecial]])
    #st.write(x_input)
#เอา input ไปทดสอบ
    st.write(DTT_model.predict(x_input))
    out=DTT_model.predict(x_input)

    if out[0]=="Not_Canceled":    
        st.image("./image/1.jpg")
        st.header("Not_Canceled")
    elif out[0]=="Canceled":
        st.image("./image/2.jpg")
        st.header("Canceled")
    else:
        st.image("./image/2.jpg") 
        st.header("Canceled") 
    st.button("ไม่ทำนาย")
else:
    st.button("ไม่ทำนาย")
    