import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 제목
st.title("📈 CSV 파일 데이터 시각화")

# 파일 업로드 섹션
st.header("📁 CSV 파일 업로드")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요", type=["csv"])  # CSV 파일 업로드 창

# 파일이 업로드되었는지 확인
if uploaded_file is not None:
    # CSV 파일 읽기
    try:
        data = pd.read_csv(uploaded_file)  # 업로드된 파일을 Pandas 데이터프레임으로 읽기
        st.success("파일 업로드 성공!")  # 성공 메시지 출력
        st.write("업로드된 데이터:")
        st.dataframe(data)  # 업로드된 데이터 표시

        # 데이터 시각화 섹션
        st.header("📊 데이터 시각화")
        
        # 데이터프레임의 첫 번째 열과 두 번째 열을 사용하여 시각화
        if len(data.columns) >= 2:  # 최소 두 개의 열이 있는지 확인
            x = data.iloc[:, 0]  # 첫 번째 열
            y = data.iloc[:, 1]  # 두 번째 열
            
            # Matplotlib 그래프 생성
            fig, ax = plt.subplots()
            ax.plot(x, y, marker='o', label="데이터 시각화")  # 데이터 시각화
            ax.set_title("CSV 데이터 시각화")  # 그래프 제목
            ax.set_xlabel("X축: " + data.columns[0])  # X축 레이블
            ax.set_ylabel("Y축: " + data.columns[1])  # Y축 레이블
            ax.legend()  # 범례 추가
            
            # Streamlit에 그래프 출력
            st.pyplot(fig)
        else:
            st.warning("시각화를 위해 최소 두 개의 열이 필요합니다.")
    except Exception as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
else:
    st.info("CSV 파일을 업로드하세요.")