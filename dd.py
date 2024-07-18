# class Building:
#     def __init__(self,loc, y, p, a):
#         self.location = loc
#         self.year = y
#         self.price = p
#         self.area = a
#
#     def print_info(self):
#         print(self.location,self.year,self.price,self.area)
#
# b_info=Building("강남","2000","1억","ㅇㅅㅇ")
# b_info.print_info(

class 정보:
    def __init__(self,이름, 나이, 연락처 ):
        self.이름 = 이름
        self.나이 = 나이
        self.연락처 = 연락처
    def print_info(self):
        print('이름은',self.이름,'이며, 나이는',self.나이,'그리고 연락처는',self.연락처, '입니다')
my_info=정보('박도현',27,'010-0000-0000')
my_info.print_info()
