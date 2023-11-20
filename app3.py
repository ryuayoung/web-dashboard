import streamlit as st
import pandas as pd

# 판다스의 데이터 프레임을, 웹 화면으로 보여주는 방법

def main() :
    st.title('아이리스 꽃 데이터') # st. ~ 웹화면 표시

    df = pd.read_csv('./02_st/data/iris.csv') # ./ 현재 폴더라는 뜻

    st.dataframe( df ) # 웹 브라우저에 데이터프레임을 보여주는 함수~

    number_of_species = df['species'].nunique()

    st.text( '아이리스 꽃의 종류는 총 ' + str(number_of_species) + '가지 입니다.' )

if __name__ == '__main__' :
    main()