# Collection type * 시험 전부 다 외워.. 리스트튜플 딕트세트 묶어서 외워, 딕트세트는 자료형에 순서가 없이.? 딕트는 키로, 세트는 값으로 꺼냄 근데 값이 중복이면 어케 꺼내요?하니까 세트는 중복값을 제거해줌 (딕트세트는 복주머니) 그래서 딕트세트는 인덱스없음
#*34다외워
#  - 여러 값을 저장하고 싶은 경우 사용
#  - 리스트(List), 튜플(Tuple), 딕셔너리(Dictionary), 세트(Set)
# 리스트와 튜플은 순서가 있고 딕셔너리, 세트는 순서가 없음
# 값을 여러개 담음 그래서 꾸러미가 필요함

# * 순서가 있는 자료형 = 시퀀스 자료형: List, Tuple
# * 순서가 없는 자료형: Dict, Set

# 1. 리스트(List) : 예시 기차
#  - 시퀀스 자료형(순서가 있는 자료형이라 그래서 index 사용 가능)
#  - index 사용(슬라이싱 가능)
#  - [] 사용
#  - 정렬 가능
#  - mutable(생성 후 값 변경 가능) 값을 만든 다음에 변경할 수 있음, 하지만 튜플은 값을 못 바꿈 그래서 튜플은 다시 만들어야 함
#  - packing과 unpacking 가능
#  - 멤버함수 존재(append(), insert(), ...)
#  - 문자열을 리스트로 표현
str = "abc"  # ["a", "b", "c"]
a = [1, 2, 3] # packing
b, c, d = [1, 2, 3] #unpacking

# Quiz: aa와 bb의 값을 서로 교환
aa = 5
bb = 3

# JAVA, C
temp = aa
aa = bb
bb = temp

# python
aa, bb = bb, aa

# 리스트 생성
list_a = [1, 2, 3]
list_b = []                    # 빈 리스트 생성 가능
list_c = [1, "a", 3.14, True]  # 다양한 자료형을 담을 수 있음

# append()
list_a.append(4)   # 맨 마지막에 추가 [1, 2, 3, 4]
# insert()
list_a.insert(1, 5) # 2번 인덱스에 5번 값 추가 [1, 5, 2, 3, 4]

# extend()
a = [1, 2, 3]
b = [2, 3, 4]
a.extend(b) # a에 b를 합치기 [1, 2, 3, 2, 3, 4]
a.append(b) # [1, 2, 3, [2, 3, 4]]
print(a)
# a+b == a.extend(b) 와 동일

# remove(값)   : 값으로 삭제
list_a.remove(2)
# pop(인덱스)  : 인덱스로 삭제     
temp = list_a.pop(0)  # 0번인덱스의 값을 temp 담고, 삭제하세요.

# index()  : 해당 값의 인덱스 출력
list_a.index(2)  # 2라는 값의 인덱스 번호
# <list_a.index(2)> # 에러나는 이유: list_a = [1, 2, 3]이지만 list_a.remove(2)를 하면 실제 값 2가 삭제된 상태여서 list_a.index(2)를 하면 2 값의 인덱스 번호를 알려달라고 하기 때문에 error가 생김
a.index(2) # 2라는 값의 인덱스 출력

# sort()    : 원본값을 정렬               : 지양
# sorted()  : 복제본을 정렬(원본값은 유지)  : 지향
a = [95, 1, 3, 27, 5]
a = sorted(a)                # 오름차순
a = sorted(a, reverse=True)  # 내림차순


# Tip: 데이터 분석or 인공지능 데이터 활용
#      -> 원본 데이터는 유지, 복제 사용


# 2. 튜플(Tuple) *못 바꿈
#  - 시퀀스 자료형
#  - index 사용(슬라이싱 가능)
#  - () 사용, () 생략 가능
#  - immutable(생성 후 값 변경 불가능)
#  - packing과 unpacking 가능
a = [1, 2, 3]  #리스트
b = (1, 2, 3)  #튜플
c = 1, 2, 3    #튜플
d = (5)        #튜플
e = 5          #정수 int
f = 5,         #튜플

# 3. 딕셔너리(Dictionary) ex: 복주머니
#  - 순서가 없음(Non-시퀀스)
#  - 인덱스 없음
#  - {} 사용
#  - {key:value} 데이터 구조 사용
#  - value는 중복 가능
#  - value는 key로만 접근 가능
a = {
    "Korea": "Seoul",
    "Canada": "Ottwa",
    "USA": 3.14
}

# dict 항목 추가 및 변경
#  - 기존에 key가 존재하지 않으면 update(수정)
#  - 기존에 key가 존재하지 않으면 insert(삽입)
a["Japan"] = "Tokyo"  # insert
a["Japan"] = "Kyoto"  # update

# dict 항목 삭제(key를 사용)
#  - del 키워드
#  - pop 함수 이용
del a["Japan"]  # 사용 금지
a.pop("Janan")

# dict 병합
# - update()
a = {"a":1, "b":2}
b = {"a":2, "c":5}
a.update(b)
print(a)  # a:2 b:2 c:5

# clear()
#  - 딕셔너리의 모든 값을 초기화
a.clear()

# in()
#  - dict안데 key가 존재하는지 확인
print("Japan" in a)

# Value Access
print(a["Japan"])  # "Japan" key 없으면 오류
print(a.get("Japan"))  #"Japan" key 없으면 None 반환 (지향)

# 모든 key, value 접근
#  - keys()   : Key만 추출
#  - values() : Value만 추출
#  - items()  : Key+Value 추출(튜플 타입)
print(list(a.keys()))
print(list(a.values()))
print(list(a.items()))

# 4. 세트(Set)
#  - 순서 없음, 인덱스 없음
#  - {} 사용
#  - 수학의 집합
#  - *중복값을 허용하지 않음* - 중복값을 제거하고 싶을 때 빼고는 안 씀
set_a = {1, 2, 3, 2, 2, 2, 2}  # Set {1, 2, 3}
aa = {}  # 딕셔너리

list_c = [1, 2, 3, 2, 3, 4, 5]  # 리스트
set(list_c)  # 세트(중복값 제거) {1, 2, 3, 4, 5}
list(ser(list_c))  # [1, 2, 3, 4, 5] *외워

# 중복값 사용 예시
list_c = [1,2,3,2,3,4,5] # 리스트타입
set(list_c) # set타입, list를 set타입을 변환하면 중복값이 사람짐
list(set(list_c)) # [1,2,3,4,5] 원본이 list형태였으면 다시 list형태로 바꿔야 함