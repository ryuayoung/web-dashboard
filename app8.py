import streamlit as st
from app_home import run_home_app
from app_eda import run_eda_app
from app_ml import run_ml_app

def main() :
    st.title('파일 분리 앱')

    menu = ['Home', 'EDA', 'ML']
    
    choice = st.sidebar.selectbox('메뉴 선택', menu )

    if choice == menu[0] :
        
        run_home_app() # Ctrl + click 시 해당 함수로 이동할 수 있다

    elif choice == menu[1] :

        run_eda_app()
        
    elif choice == menu[2] :
        
        run_ml_app()

if __name__ == '__main__' :
    main()