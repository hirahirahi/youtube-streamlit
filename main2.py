import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 門')

st.write('Display Image')

# -----------------------------------
if st.checkbox('show image'):

    img = Image.open('C:/Users/hiramatu/Desktop/pythonwk/Test.jpg')
    #ブラウザの横幅に合わせるuse_column_width
    st.image(img, caption='aiueo',use_column_width='true')

# -----------------------------------
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1,11))
)
'あなたの好きな数字は、', option, 'です。'

# -----------------------------------
st.write('Interactive Widgets')
#text_areaは複数行入力
#option = st.text_input('あなたの趣味を教えて下さい。')
#'あなたの趣味は', option, 'です。'

# -----------------------------------
#condition = st.slider('あなたの今の調子は？',0,100,50)
#'コンディション', condition

# -----------------------------------
#condition2 = st.sidebar.slider('あなたの今の調子は？',0,100,50)
#'コンディション', condition2

# -----------------------------------
#option = st.sidebar.text_input('あなたの趣味を教えて下さい。')
#'あなたの趣味は', option, 'です。'
#
#condition3 = st.sidebar.slider('あなたの今の調子は？',0,100,50)
#'コンディション', condition3

# -----------------------------------
st.title('Streamlit 門')
st.write('Display Image')

st.write('Interactive Widgets')

left_column,right_column = st.columns(2)
button = left_column.button('⇒カラムに文字を表示')
if button:
    right_column.write('ここは⇒カラム')

# -----------------------------------
#left_column, right_column = st.column(2)
#button = left_column.buttoon('右絡むに文字を表示')
#if button:
#    right_column.write('ここは右カラム2')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせの回答1')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせの回答2')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせの回答3')




