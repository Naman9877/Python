#paytm
# Object recharge attributes type prepaid or postpaid,mobile number,operator,Amount
print("Recharge or pay Mobile Bill ")
class Recharge:
    def __init__(self,type="Prepaid or Postpaid",mobile="+91 7696040355",operator="",amount=40):
        self.type = type
        self.mobile = mobile
        self.operator = operator
        self.amount = amount
    def show(self):
        print("~~~~~~~~~~~~~~~~~~~")
        print("TYPE OF MOBILE NO IS:",self.type)
        print("MOBILE NO. is:", self.mobile)
        print("Operator is:", self.operator)
        print("AMOUNT IS:",self.amount)
        print("~~~~~~~~~~~~~~~~~~")
recharge1 = Recharge()
recharge2 = Recharge("Prepaid","+91 9542162549","Jio",239)
recharge1.show()
recharge2.show()