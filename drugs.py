
class Drug:

    def __init__(self,name,id,price,quantity):
        self.name= name
        self.id= id
        self.price=price
        self.quantity=quantity

drug1=Drug("Panadol", 12, 100, 5)
drug2=Drug("Amoxil", 15, 50, 20)
drug3=Drug("Quinin", 15, 200, 150)

print(drug1.name)
print(drug2.price)
print(drug3.__dict__)

        