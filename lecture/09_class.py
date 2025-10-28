# Class
# - 객체: 실세계에 존재하는 것을 속성과 동작으로 표현하는 것
# - 속성: 변수
# - 동작: 함수

# 우체부 -> 객체로 표현
# Class: 우체부
#  ㄴ 변수1: 배달할 물품
#  ㄴ 변수2: 주소
#  ㄴ 함수1: 배달한다()
#  ㄴ 함수2: 회수한다()
#  ㄴ 함수3: 이동한다()

# web, app -> Java -> Spring
# AI, 데이터 분석 -> python

# 1.Class: 객체의 설계 도면     : 힐스테이트 아파트 도면
# 2.객체생성: 인스턴스 생성!    : 힐스테이트 수완 짓기
#   ㄴ 생성자 함수() -> 모든 Class에는 반드시 1개 이상의 생성자 함수 보유
#   ㄴ 생성자 함수를 선언하지 않는 경우 자동으로 Default 생성자() 생성
# 3.객체사용: 인스턴스 사용!   : 입주
# *동일한 Class로 생성된 인스턴스들은 서로 다른 객체 인식

# 1. Class 
class Test:
    # 생성자 함수
    # JAVA(This) == Python(self)
    # python은 클래스에 포함된 모든 함수들의 첫번째 매개변수로 self
    def __init__(self):
        print("Hello Class")  
  
    # 일반함수  
    def print_name(self, name: str):
        print(f"Hello {name}")

#객체 생성
# Test() -> 생성자 함수
# test -> 인스턴스
test = Test()

# 3.객체 사용
test.print_name("홍길동")