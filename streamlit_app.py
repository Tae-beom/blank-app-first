import streamlit as st

# 페이지 제목
st.title("🎈 Streamlit 요소 예시 페이지")  # 페이지의 제목을 설정합니다.

# 텍스트 출력
st.header("📄 텍스트 출력")  # 섹션 헤더를 추가합니다.
st.write("이것은 일반 텍스트입니다.")  # 일반 텍스트를 출력합니다.
st.markdown("**이것은 마크다운 텍스트입니다.**")  # 마크다운 형식의 텍스트를 출력합니다.

# 입력 요소
st.header("🖊️ 입력 요소")  # 입력 섹션 헤더를 추가합니다.
text_input = st.text_input("텍스트 입력창:", "기본값")  # 텍스트 입력창을 추가합니다.
number_input = st.number_input("숫자 입력창:", min_value=0, max_value=100, value=50)  # 숫자 입력창을 추가합니다.
date_input = st.date_input("날짜 선택창:")  # 날짜 선택창을 추가합니다.
time_input = st.time_input("시간 선택창:")  # 시간 선택창을 추가합니다.

# 버튼 및 선택 요소
st.header("🔘 버튼 및 선택 요소")  # 버튼 섹션 헤더를 추가합니다.
if st.button("클릭 버튼"):  # 버튼을 추가하고 클릭 이벤트를 처리합니다.
    st.write("버튼이 클릭되었습니다!")
checkbox = st.checkbox("체크박스")  # 체크박스를 추가합니다.
if checkbox:
    st.write("체크박스가 선택되었습니다.")
radio = st.radio("라디오 버튼:", ["옵션 1", "옵션 2", "옵션 3"])  # 라디오 버튼을 추가합니다.
st.write(f"선택된 옵션: {radio}")
selectbox = st.selectbox("드롭다운 선택:", ["옵션 A", "옵션 B", "옵션 C"])  # 드롭다운 선택창을 추가합니다.
st.write(f"선택된 옵션: {selectbox}")
multiselect = st.multiselect("다중 선택:", ["옵션 X", "옵션 Y", "옵션 Z"])  # 다중 선택창을 추가합니다.
st.write(f"선택된 옵션: {multiselect}")

# 슬라이더
st.header("🎚️ 슬라이더")  # 슬라이더 섹션 헤더를 추가합니다.
slider = st.slider("슬라이더:", min_value=0, max_value=100, value=50)  # 슬라이더를 추가합니다.
st.write(f"슬라이더 값: {slider}")

# 파일 업로드
st.header("📁 파일 업로드")  # 파일 업로드 섹션 헤더를 추가합니다.
uploaded_file = st.file_uploader("파일 업로드:", type=["txt", "csv", "png", "jpg"])  # 파일 업로드 창을 추가합니다.
if uploaded_file:
    st.write(f"업로드된 파일 이름: {uploaded_file.name}")

# 데이터 시각화
st.header("📊 데이터 시각화")  # 데이터 시각화 섹션 헤더를 추가합니다.
import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])  # 랜덤 데이터 생성
st.line_chart(data)  # 라인 차트를 추가합니다.
st.bar_chart(data)  # 바 차트를 추가합니다.

# 이미지 출력
st.header("🖼️ 이미지 출력")  # 이미지 출력 섹션 헤더를 추가합니다.
st.image("https://via.placeholder.com/150", caption="예시 이미지")  # URL을 통해 이미지를 출력합니다.

# 비디오 출력
st.header("🎥 비디오 출력")  # 비디오 출력 섹션 헤더를 추가합니다.
st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # YouTube 비디오를 출력합니다.

# 오디오 출력
st.header("🔊 오디오 출력")  # 오디오 출력 섹션 헤더를 추가합니다.
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 오디오 파일을 출력합니다.

# 데이터 테이블
st.header("📋 데이터 테이블")  # 데이터 테이블 섹션 헤더를 추가합니다.
st.table(data)  # 정적 데이터 테이블을 출력합니다.
st.dataframe(data)  # 동적 데이터 테이블을 출력합니다.

# 코드 출력
st.header("💻 코드 출력")  # 코드 출력 섹션 헤더를 추가합니다.
st.code("print('Hello, Streamlit!')", language="python")  # 코드 블록을 출력합니다.

# 상태 표시
st.header("⏳ 상태 표시")  # 상태 표시 섹션 헤더를 추가합니다.
with st.spinner("로딩 중..."):
    import time
    time.sleep(2)
st.success("로딩 완료!")  # 성공 메시지를 출력합니다.
st.error("에러 메시지!")  # 에러 메시지를 출력합니다.
st.warning("경고 메시지!")  # 경고 메시지를 출력합니다.
st.info("정보 메시지!")  # 정보 메시지를 출력합니다.