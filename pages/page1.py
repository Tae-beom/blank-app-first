import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import font_manager
import numpy as np

# 한글 폰트 설정 (NanumGothic-Regular.ttf 파일 사용)
font_path = "./fonts/NanumGothic-Regular.ttf"  # 폰트 파일 경로
font = font_manager.FontProperties(fname=font_path)
rc('font', family=font.get_name())  # 폰트 설정

# 페이지 제목
st.title("📊 Matplotlib 데이터 시각화 예시")

# 데이터 생성
x = np.linspace(0, 10, 100)
y = np.sin(x)

# 그래프 생성
fig, ax = plt.subplots()
ax.plot(x, y, label="사인 곡선")
ax.set_title("Matplotlib 그래프 예시", fontproperties=font)  # 그래프 제목에 한글 표시
ax.set_xlabel("X축", fontproperties=font)  # X축 레이블에 한글 표시
ax.set_ylabel("Y축", fontproperties=font)  # Y축 레이블에 한글 표시
ax.legend(prop=font)  # 범례에 한글 표시

# Streamlit에 그래프 출력
st.pyplot(fig)