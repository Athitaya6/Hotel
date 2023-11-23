import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Athitaya Datascience Project",
    page_icon= ":bar_chart:",
)
st.markdown(
   f"""
   <h1 style= 'text-align: center;'>การทำนายผลพฤติกรรมการจองโรงแรมของลูกค้า 🌍 🏨</h1>
   """,
   unsafe_allow_html=True
)

st.subheader("3.ทฤษฎีที่เกี่ยวข้อง")
st.write(" 1. เหมืองข้อมูล (data Mining) เป็นเทคนิคในการวิเคราะห์ข้อมูลอย่างหนึ่ง เป็นการค้นหาสิ่งที่มีประโยชน์จากฐานข้อมูลที่มีขนาดใหญ่ เช่น ข้อมูลการซื้อขายสินค้าในซุปเปอร์มาร์เก็ตต่าง ๆ โดยข้อมูลเหล่านี้จะเก็บจากรายการสินค้าที่ลูกค้าซื้อในแต่ละครั้ง โดยเมื่อทำการวิเคราะห์ข้อมูลด้วยเทคนิค Data Mining แล้วจะได้สิ่งที่เป็นประโยชน์")
st.write(" 2. วิธีการเพื่อนบ้านใกล้ที่สุด (K-Nearest Neighbor Algorithm : Knn) เป็นวิธีที่ใช้ในการจัดแบ่งคลาสโดยเทคนิคนี้จะตัดสินใจว่า คลาสใดที่จะแทนเงื่อนไขหรือกรณีใหม่ๆ ได้บ้าง โดยการตรวจสอบจำนวนบางจำนวน ในขั้นตอนวิธีการเพื่อนบ้านใกล้ที่สุด ของกรณีหรือเงื่อนไขที่เหมือนกันหรือใกล้เคียงกันมากที่สุด โดยจะหาผลรวม (Count Up) ของจำนวนเงื่อนไข หรือกรณีต่างๆ สำหรับแต่ละคลาส และกำหนดเงื่อนไขใหม่ๆ ให้คลาสที่เหมือนกันกับคลาสที่ใกล้เคียงกันมากที่สุด")
st.write(" 3. ต้นไม้การตัดสินใจ (decision tree) เป็นเครื่องมือที่ช่วยให้วิเคราะห์เหตุการณ์ หรือสถานการณ์เพื่อการตัดสินใจได้อย่างเป็นระบบและรวดเร็ว ต้นไม้การตัดสินใจมีลักษณะเป็นกราฟรูปต้นไม้ ซึ่งแสดงที่ตั้งต้นที่มีรากและแขนงต่างๆแตกออกมาจากต้นไม้ไปในทิศทางเดียว จนกระทั่งนำไปสู่ข้อสรุปสำหรับการตัดสินใจได้ ต้นไม้การตัดสินใจมีประโยชน์ในการสรุปการตัดสินใจที่มีความซับซ้อนให้ง่ายต่อความเข้าใจ ปัจจุบันต้นไม้การตัดสินใจเป็นที่นิยมใช้ในงานหลายอย่าง เช่น การสร้างเครื่องที่เรียนรู้ได้เอง การสร้างระบบผู้เชี่ยวชาญ ฯลฯ")
st.write(" 4. โครงข่ายประสาทเทียม (Artificial Neural Networks) คือ การสร้างคอมพิวเตอร์ที่มีแบบจำลองที่จำลองวิธีการทำงานของสมองมนุษย์ หรือเป็นการทำให้คอมพิวเตอร์รู้จักการคิดและการจดจำ หรือจะใช้โครงข่ายประสาทเทียมในการทำให้คอมพิวเตอร์รู้จักและเข้าใจภาษามนุษย์ หรือเรียกอีกอย่าว่า AI")
st.write(" 5. การแปลงรูปแบบข้อมูล (Data Transformation) เป็นส่วนหนึ่งของขั้นตอนการเตรียมข้อมูล(Data preparation)  ซึ่งเป็นการปรับเปลี่ยนรูปแบบของข้อมูลให้อยู่ในรูปแบบที่พร้อมนำไปใช้ในการประมวลผลหรือการวิเคราะห์ต่อไป มีหลายเทคนิควิธี เช่น Min-Max Normalization, Mean  Normalization, Z-score  Normalization")


st.balloons()