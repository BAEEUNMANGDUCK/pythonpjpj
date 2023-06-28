import another_module
from prettytable import PrettyTable
# print(another_module.another_variable)
"""
절차 지향 프로그래밍: 위에서 아래로, 필요할 때 함수 호출, 복잡도 증가

객체지향 프로그래밍: 생산성 향상을 위해 등장, 각각을 모듈화하여 '재사용'에 용이함.
ex) 레스토랑 운영시 각 역할의 사람을 고용하는 것.(셰프, 웨이터, 청소부, 매니저)

객체지향이라 불리는 이유? 실생활의 객체를 모델로 하므로, 객체란 현실에 존재하거나 생각할 수 있는 것을 말함.

객체 : 속성(property, 상태) 과 행위(method, behavior)으로 이루어져 있음.
"""

# from turtle import Turtle, Screen
#
# # Turtle 클래스의 timmy 객체 생성
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('coral')
#
# timmy.forward(100)
# # Screen 클래스의 객체 생성 후, 메서드 호출
# my_screen = Screen()
# my_screen.exitonclick()

# prettytable 활용

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = "l"
print(table)

"""
객체 지향 프로그래밍의 장점: 추상화?
커피 머신 OOP로 다시 만들기 
"""


