#
# class AirPlain:
#     def __init__(self, departure, arrival):
#         self.departure = departure
#         self.arrival = arrival
#
#     def broadcast(self):
#         print(f"이 비행기의 출발지는 {self.departure}입니다. 도착지는 {self.arrival}입니다.")
#
# class CombatAirPlain(AirPlain):
#     #상속 부모의 속성을 전부 가지고 온다
#     def __init__(self, departure, arrival, missile):
#         super().__init__(departure, arrival)
#         self.missile = missile
#         #생성자를 오버라이드 했지만 생성자를 다시 불러오기 때문에 다시 정의해 주어야 한다.
#
#     def attack(self):
#         print("공격 기능을 수행합니다")
#
#
# a = AirPlain("서울", "부산")
# b = AirPlain("서울", "뉴욕")
# c = CombatAirPlain("서울", "제주", 1)
# c.attack()



class User():
    def __init__(self, name, ph_number, age):
        self.name = name
        self.ph_number = ph_number
        self.age = age

    def basicInfo(self):
        print(f"이름: {self.name} \n휴대폰: {self.ph_number} \n나이: {self.age}")


# 실행예시

man = User("홍길동", "010-1234-1234", 30)
man.basicInfo()

# 결과
# 이름: 홍길동
# 휴대폰: 010-1234-1234
# 나이: 30