import streamlit as st

# 이미지 / 동영상을 화면에 보여주기
# 라이브러리가 필요하다!
# 파이썬 이미지 라이브러리

from PIL import Image # pythin image 라이브러리의 약자!

def main() :
    
    img = Image.open('./02_st/data/image_03.jpg') # 메모리에 올리기!

    print(img)

    st.image( img )

    st.image( img, use_column_width= True )

    img_url = 'https://img.hankyung.com/photo/202306/01.33606768.1-1200x.jpg'

    st.image( img_url )

    video_file = open('./02_st/data/video1.mp4', 'rb') # 파일경로만 쓰면 안열려요! 'rb' 꼭 넣어줘야행

    st.video( video_file )

if __name__ == '__main__' :
    main()