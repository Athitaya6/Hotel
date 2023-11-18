import json
import time
import requests
import streamlit as st

st.set_page_config(
    page_title="Athitaya Datascience Project",
    page_icon= ":bar_chart:",
)
st.sidebar.success("เลือกรายการด้านบน.")

st.header("พฤติกรรมการจองโรงแรมของลูกค้า! 🌍  🏨 ")
st.subheader("1.หลักการและเหตุผล")
st.write("ปัจจุบันการท่องเที่ยวเป็นตัวขับเคลื่อนเศรษฐกิจของโลกและของประเทศเป็นอันดับ1 ถึงแม้จะมีสถานการณ์ COVID-19 แต่ในปี2565 ทั่วโลกมีแนวโน้มที่พร้อมกับการเตรียมประกาศให้ COVID-19 กลายเป็นโรคประจำถิ่น ทำให้นานาประเทศรวมทั้งประเทศไทยประกาศปลดล็อก และผ่อนคลายมาตรการต่าง ๆ ตามเงื่อนไขของแต่ละประเทศ พร้อมกับเปิดรับนักท่องเที่ยวเข้าประเทศแบบไม่มีเงื่อนไข ทำให้ผู้คนต่างวางแผนออกเดินทางท่องเที่ยวเป็นจำนวนมาก บรรยากาศการเดินทางท่องเที่ยวเริ่มกลับมาคึกคักอีกครั้ง จึงทำให้นักท่องเที่ยวต้องการหาที่พักค้างคืน ธุรกิจที่พักแรมในปัจจุบัน จึงมีความหลากหลายทั้งในด้านรูปแบบและด้านการบริการที่นักท่องเที่ยวสามารถเลือกใช้บริการตามความต้องการ เช่น โรงแรม โมเต็ล เกสต์เฮาส์ อพาร์ตเม้นท์ รีสอร์ท โฮมสเตย์บังกะโล เป็นต้น")

st.subheader("2.วัตถุประสงค์")
st.write("1.เพื่อใช้เทคนิคเหมืองข้อมูลในการแปลงชุดข้อมูลการจองโรงแรมให้อยู่ในรูปแบบที่เหมาะสมกับเทคนิคที่นำมาใช้ใช้จำแนกประเภทข้อมูล")
st.write("2.เพื่อเปรียบเทียบประสิทธิภาพของการจำแนกประเภทการจองโรงแรมของชุดข้อมูลการแปลงข้อมูลในรูปแบบต่างๆ")
st.write("3.เพื่อใช้ประสิทธิภาพที่ดีที่สุดสำหรับนำไปพัฒนาเป็นระบบต้นแบบสำหรับสนับสนุนการตัดสินใจเลือกจองอสังหาริมทรัพย์บนเว็บ")
st.balloons()