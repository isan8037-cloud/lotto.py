import random
import streamlit as st

# 웹 앱 제목 설정
st.title("로또 번호 생성기 🎰")
st.write("버튼을 눌러 행운의 로또 번호를 확인해보세요! (최대 5세트까지 생성됩니다)")

# 세션 상태를 이용해 생성된 로또 세트들을 기억하기
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []


# 로또 번호 구간별 색상을 반환해주는 함수 (한국 로또 공식 색상 기준)
def get_ball_color(number):
  if 1 <= number <= 10:
    return "#fbc400"  # 노란색
  elif 11 <= number <= 20:
    return "#69c8f2"  # 파란색
  elif 21 <= number <= 30:
    return "#ff7272"  # 빨간색
  elif 31 <= number <= 40:
    return "#aaaaaa"  # 회색
  else:
    return "#b0d840"  # 초록색


# '로또번호 생성' 버튼 클릭 시
if st.button("로또번호 생성"):
  # 1부터 45 사이의 숫자 중 중복 없이 6개 무작위 추출 및 오름차순 정렬
  numbers = sorted(random.sample(range(1, 46), 6))

  # 최대 5개 세트까지만 유지하도록 관리
  if len(st.session_state.lotto_history) >= 5:
    st.session_state.lotto_history.pop(
        0
    )  # 가장 오래된(첫 번째) 세트를 지우고 새 것 추가
  st.session_state.lotto_history.append(numbers)

# 기록 초기화 버튼 (선택 사항)
if st.button("기록 초기화"):
  st.session_state.lotto_history = []

# 현재 저장된 로또 번호 세트들을 화면에 예쁘게 출력
if st.session_state.lotto_history:
  st.write("### 📌 생성된 로또 번호 목록")

  # 최근에 생성된 번호가 위로 오도록 역순으로 출력
  for i, lotto_set in enumerate(reversed(st.session_state.lotto_history)):
    set_number = len(st.session_state.lotto_history) - i
    st.write(f"**세트 {set_number}**")

    # 공 모양으로 예쁘게 보여주기 위해 HTML/CSS 사용
    balls_html = '<div style="display: flex; gap: 10px; margin-bottom: 15px;">'
    for num in lotto_set:
      bg_color = get_ball_color(num)
      # 공 스타일 설정 (동그란 모양, 중앙 정렬, 그림자 효과)
      balls_html += f"""
            <div style='
                width: 40px; 
                height: 40px; 
                background-color: {bg_color}; 
                border-radius: 50%; 
                display: flex; 
                align-items: center; 
                justify-content: center; 
                color: black; 
                font-weight: bold; 
                font-size: 16px;
                box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
            '>
                {num}
            </div>
            """
    balls_html += "</div>"

    # HTML 렌더링
    st.markdown(balls_html, unsafe_allow_html=True)