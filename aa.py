#1 문자 메세지 길이 판별 클래스, 문자메세지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오.
class Mms:
    def __init__(self,mms):
        self.mms=mms

    def price(self):
        if len(self.mms)>=20:
            print('문자 요금은 100원 입니다.')
            result=100
        elif len(self.mms)<20 :
            print('문자 요금은 50원 입니다.')
            result=50
        return result
my_mms=Mms('555555')
my_mms.price()

#2 문자메세지의 길이에 따라 부과되는 요금은, 클래스를 생성할때 속성 정보로 갖게된다. 또한, 요금이 부과될 문자 메세지의 길이를 정할 수 있도록 설장하시오.
#3 이때, 사용자로부터 문자메세지를 입력받아서 문자 요금을 반환하는 코드를 작성하시오.