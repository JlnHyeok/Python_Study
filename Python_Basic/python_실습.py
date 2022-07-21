class Quiz:
    answer = ['경기도','강원도','충청남도','충청북도','전라남도','전라북도',
              '경상남도','경상북도','제주특별자치도'] # 클래스 변수
    @classmethod
    def challange(cls): # 클래스 메서드 정의
        if not cls.answer: # answer 리스트에 값이 없다는 뜻은 모두 맞췄다는 뜻.
            print('모든 도를 맞췄습니다. 성공입니다.')
            return # 함수 종료
        do = input('정답은? >>> ')
        if do not in cls.answer: # 대답이 answer 리스트에 없는 값이라면
            raise Exception('틀렸습니다')
        for i, answer_do in enumerate(cls.answer):
            if do == answer_do: # 정답과 대답이 같다면
                print('정답입니다.')
                cls.answer.pop(i)   # i번째 값을 꺼내어서 삭제
                break
        cls.challange()

try:
    print('우리나라의 9개 모든 도를 맞히는 퀴즈입니다. 하나씩 대답하세요.')
    Quiz.challange()    # 클래스 메서드 호출
except Exception as e:
    print(e)    # 예외 메시지 출력
