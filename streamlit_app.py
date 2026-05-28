import streamlit as st

# 1. 앱 제목 및 설명 (출력)
st.title("🏆 이번 주 주인공은 3등! 프로그램")
st.write("여러 명의 이름과 점수를 입력하면, 당당하게 3등을 차지한 사람을 찾아줍니다!")
st.caption("조건: 최소 3명 이상의 점수를 입력해야 정확한 결과가 나옵니다.")

st.divider()

# 2. 사용자 입력 받기 (입력)
# 스트림릿에서는 text_area를 통해 여러 줄을 한 번에 입력받을 수 있습니다.
st.subheader("📝 이름과 점수 입력하기")
user_input = st.text_area(
    "형식: 이름 점수 (한 줄에 한 명씩 입력하고 엔터를 눌러주세요)",
    value="🌟예시🌟\n철수 95\n영희 88\n민수 100\n수지 72\n길동 91",
    height=200,
)

# 결과를 저장할 딕셔너리
score_dict = {}

# 3. 데이터 처리 (반복문 및 조건문)
if st.button("📊 3등 결과 확인하기"):
    # 입력된 텍스트를 줄 바꿈 기준으로 분리 (반복문 활용)
    lines = user_input.strip().split("\n")

    for line in lines:
        if not line.strip() or "🌟" in line:  # 빈 줄이거나 예시 텍스트면 건너뛰기
            continue

        try:
            # 공백을 기준으로 이름과 점수 분리
            name, score_str = line.split()
            score = int(score_str)  # 점수를 정수형으로 변환
            score_dict[name] = score
        except ValueError:
            st.error(
                f"⚠️ '{line}' 입력 형식이 잘못되었습니다. '이름 점수' 형태로 입력해주세요."
            )
            st.stop()

    # 4. 3등 찾기 알고리즘 (조건문 및 정렬)
    # 입력된 데이터의 수가 3명 이상인지 확인 (조건문)
    if len(score_dict) < 3:
        st.warning(
            f"현재 입력된 인원은 {len(score_dict)}명입니다. 3등을 찾으려면 최소 3명 이상 입력해주세요!"
        )
    else:
        # 점수를 기준으로 내림차순(높은 순) 정렬
        # sorted_scores는 (이름, 점수) 형태의 튜플들이 담긴 리스트가 됩니다.
        sorted_scores = sorted(
            score_dict.items(), key=lambda x: x[1], reverse=True
        )

        # 파이썬 인덱스는 0부터 시작하므로, 3등은 인덱스 2번입니다.
        third_place = sorted_scores[2]
        third_name = third_place[0]
        third_score = third_place[1]

        # 5. 최종 결과 출력 (출력)
        st.success("🎉 결과를 확인하세요!")

        # 메인 결과 박스
        st.metric(label="🥉 3위 달성자", value=f"{third_name}님", delta=f"{third_score}점")

        # 전체 순위 보기 (반복문 활용)
        with st.expander("👀 전체 순위 보기"):
            rank = 1
            for name, score in sorted_scores:
                st.write(f"**{rank}등** : {name} ({score}점)")
                rank += 1