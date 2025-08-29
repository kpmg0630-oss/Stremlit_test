import streamlit as st
import pandas as pd
import numpy as np

st.title('Data Display elements')
st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/data')

# 1. Metric (단일 지표 카드)
st.header('1.Metric')
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# 2. 여러 개의 metric 카드 (한 줄)
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


# 3. delta 색상 옵션
st.metric(label="Gas price", value=4, delta=-0.5, delta_color="inverse")
st.metric(label="Active developers", value=123, delta=123, delta_color="off")


# 4. Grid 형태의 metric 카드
a, b = st.columns(2)
c, d = st.columns(2)

a.metric("Temperature", "30°F", "-9°F", border=True)
b.metric("Wind", "4 mph", "2 mph", border=True)

c.metric("Humidity", "77%", "5%", border=True)
d.metric("Pressure", "30.34 inHg", "-2 inHg", border=True)


# 4_1. Grid 형태의 metric 카드 - 내 실습
st.header('2. 주요지표')
a, b, c = st.columns(3)

a.metric("미국", "1388.30", "2.80", border=True)
b.metric("중국", "194.85", "0.26", border=True)
c.metric("국제 금", "3471.00", "-3.30", border=True)



# Dataframe 조회
st.header('3. Dataframe 조회하기')
titanic = pd.read_csv('t2.csv')
st.dataframe(titanic.head(10))
# 인터렉티브 테이블 (스크롤, 정렬, 다운로드, 검색 가능)


# Pandas Styler 활용 예시
# 난수 데이터 프레임 생성 (10행 * 20열)
df = pd.DataFrame(np.random.randn(10, 20), 
columns=("col %d" % i for i in range(20)))
# 각 열의 최대값을 강조 표시 (hinglight_max)
st.dataframe(df.style.highlight_max(axis=0)) 
