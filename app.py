import streamlit as st
import random

def main():
    st.title("영단어 맞추기 게임")

    # Step 1: Select Dictionary
    st.header("Step 1: Select Dictionary")
    dictionary = st.radio("어떤 사전을 사용하시겠습니까?", ['수능2000 Day 19', '수능2000 Day 20'])

    # Step 2: Select Mode
    st.header("Step 2: Select Mode")
    mode = st.radio("어떤 모드를 선택하시겠습니까?", ['영단어 스펠링', '한국어 단어'])

    # Step 3: Play Game
    st.header("Step 3: Play Game")

    word_lists = {
        '수능2000 Day 19': {'vital': ['필수적인', '중요한'], 'incident': ['일어난 일', '사건', '일어나기 쉬운'],
                           'session': ['시간', '기간', '회의', '대학의 학기'], 'obvious': ['명백한', '분명한'],
                           'moderate': ['온건한', '적당한'], 'budget': ['예산', '예산안'], 'graze': ['풀을 뜯다', '방목하다'],
                           'fragile': ['부서지기 쉬운'], 'myth': ['신화'], 'fur': ['부드러운 털', '모피'],
                           'indifferent': ['무관심한'], 'strain': ['잡아당기다', '긴장시키다', '긴장', '압박'],
                           'ingredient': ['재료', '성분'], 'dismiss': ['해고하다', '해산시키다'],
                           'geometry': ['기하학'], 'glacier': ['빙하'], 'urge': ['촉구하다', '강요하다'],
                           'celebrity': ['명성', '유명 인사'], 'antique': ['옛날의', '고대의', '골동품'],
                           'profit': ['이익', '이윤', '이익을 얻다'], 'sphere': ['구체', '구'],
                           'inherit': ['상속하다', '물려받다'], 'disgrace': ['불명예', '수치'], 'crawl': ['기어가다', '서행하다', '기어가기', '서행'],
                           'scratch': ['긁다', '할퀴다', '긁은 자국', '찰과상'], 'diabetes': ['당뇨병'],
                           'congestion': ['밀집', '혼잡'], 'constitute': ['구성하다', '제정하다', '설립하다'],
                           'flow': ['흐르다', '흐름'], 'investigate': ['조사하다', '수사하다'], 'barter': ['물물 교환하다', '물물교환', '교역품'],
                           'circular': ['원의', '순환의'], 'chilly': ['쌀쌀한', '냉담한'], 'ancestor': ['조상', '선조'],
                           'fierce': ['사나운', '맹렬한'], 'vague': ['막연한', '모호한', '흐릿한'], 'rough': ['거친', '난폭한', '대강의'],
                           'content': ['만족하는', '내용(물)', '목차'], 'obstacle': ['장애물', '방해가 되는 것'],
                           'editorial': ['사설', '논설', '편집자의']},
        '수능2000 Day 20': {'tissue': ['조직'], 'refresh': ['상쾌하게 하다', '새롭게 하다'],
                           'present': ['제출하다', '나타내다', '현재의', '선물'], 'form': ['형성하다', '형태'],
                           'lord': ['군주'], 'substitute': ['대체하다', '대체물', '대리자'], 'scan': ['정밀검사하다', '유심히 쳐다보다'],
                           'pottery': ['도자기'], 'layer': ['층', '겹'], 'rise': ['오르다', '일어나다', '오름', '상승'],
                           'radiant': ['빛나는', '아주 밝은'], 'exclaim': ['(감탄하며)외치다'], 'polish': ['닦다', '윤 내다', '문장 등을 다듬다'],
                           'flavor': ['맛', '맛을 내다'], 'imprint': ['(도장 등을)찍다', '감명시키다', '찍은 자국', '인상'],
                           'heritage': ['유산', '세습 재산'], 'strive': ['노력하다', '애쓰다', '투쟁하다'],
                           'property': ['재산'], 'majesty': ['위엄', '장엄', '왕'], 'portray': ['묘사하다', '설명하다', '초상을 그리다'],
                           'subscribe': ['정기구독하다'], 'shrug': ['(어깨를)으쓱하다'], 'wage': ['급료'], 'asset': ['자산', '자질'],
                           'intimate': ['친밀한'], 'merit': ['장점', '공로', '~할 만하다'], 'launch': ['발사하다', '(새로운 일을)시작하다', '발사'],
                           'conference': ['회담', '회의'], 'reception': ['환영회', '접수'], 'administer': ['관리하다', '운영하다', '통치하다'],
                           'vicious': ['사악한', '악의 있는'], 'cherish': ['소중히 하다'], 'accuse': ['고발하다', '비난하다'],
                           'eternal': ['영원한'], 'shrink': ['축소하다', '수축하다'], 'overwhelm': ['압도하다', '당황하게 하다'],
                           'transmit': ['전달하다'], 'copper': ['구리', '구리의', '구릿빛의'], 'orbit': ['궤도', '궤도를 그리며 돌다'],
                           'colleague': ['동료']}
    }

    word_dict = word_lists[dictionary]

    strikes = 0
    outs = 0
    used_words = set()

    for word, meanings in word_dict.items():
        if outs == 3 or len(used_words) == len(word_dict):
            break

        if word in used_words:
            continue

        used_words.add(word)

        if mode == '한국어 단어':
            st.write(f"영단어: {word}")
            user_input = st.text_input("한국어를 입력하세요:", key=f"{word}_input", value="")
            if user_input:
                if user_input in meanings:
                    strikes += 1
                    st.success('맞췄습니다!')
                else:
                    outs += 1
                    st.error(f'땡! 정답은 {meanings} 중 하나입니다.')
        elif mode == '영단어 스펠링':
            st.write(f"뜻: {meanings}")
            user_input = st.text_input("영단어를 입력하세요:", key=f"{word}_input", value="")
            if user_input:
                if user_input == word:
                    strikes += 1
                    st.success('맞췄습니다!')
                else:
                    outs += 1
                    st.error(f'땡! 정답은 {word}입니다.')

    st.write(f'맞춘 개수: {strikes}, 틀린 개수: {outs}')

if __name__ == '__main__':
    main()