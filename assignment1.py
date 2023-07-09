message ="""
WELCOME TO ZOMATO

Snacks Bar
Chinese, Fast Food, Pizza, Burger
Ludhiana Junction, Ludhiana

ZOMATO OFFERS
Get 50% OFF up to ₹100
Valid on total value of items worth ₹159 or more.
WELCOME50


Get 30% OFF up to ₹75 and ₹25 Paytm cashback using Paytm
Valid on total value of items worth ₹299 or more.
ZOMPAYTM


Get 30% OFF up to ₹90 using Simpl
Valid on total value of items worth ₹199 or more
SIMPLPARTY


Get 30% OFF up to ₹155 using SBI Credit Cards
Valid on total value of items worth ₹399 or more
SBITREATS

"""
print(message)
amount= int(input("Enter Total amount : "))
promo_code=input("Enter the promo code:")

if promo_code == "WELCOME50":
    if amount >= 159:
        print("Promo Code Applied")

        discount=0.50*amount

        if discount >=100:
            discount=100
        amount_to_pay=amount-discount
        print("Please Pay :  \u20b9",amount_to_pay)
    else:
        print("Amount is lesser for promo code")
        print("Amount to pay is: \u20b9",amount)
elif promo_code == "ZOMPAYTM":
    if amount >=299:
        print("Promo Code Applied")
        discount=0.30*amount
        if discount >=75:
            discount=75
        amount_to_pay=amount-discount
        print("Please Pay: \u20b9",amount_to_pay)
        print("Paytm Cashback is :\u20b9 25")
    else:
        print("Amount is lesser for promo code")
        print("Amount to pay is: \u20b9",amount)
elif promo_code == "SIMPLPARTY":
    if amount >=199:
        print("Promo Code Applied")
        discount=0.30*amount
        if discount >=90:
            discount=90
        amount_to_pay=amount-discount
        print("Amount to pay is: \u20b9",amount_to_pay)
    else:
        print("Amount is lesser for promo code")
        print("Amount to pay is: \u20b9",amount)
elif promo_code == "SBITREATS":
    if amount >=399:
        print("Promo Code Applied For SBI Credit Card")
        discount=0.30*amount
        if discount >=155:
            discount=155
        amount_to_pay=amount-discount
        print("Amount to pay is: \u20b9",amount_to_pay)
    else:
        print("Amount is lesser for promo code")
        print("Amount to pay is: \u20b9 using sbi credit card", amount)
print("\n")
print("THANK YOU FOR YOUR ORDER  but we have great offers for you Please see it ")
print("\n")


if (amount>=159 and amount<199):
    print("you can apply 2 promocodes WELCOME50 and SIMPLPARTY ")
    print("\n")
    print("WELCOME50 will give you more discount ")

elif  (amount>=199 and amount<299):
    print("you can apply 3 promocodes ZOMPAYTM and WELCOME50 and SIMPLPARTY ")
    print("SUGGESTION --> WELCOME50 will give you more discount")
elif (amount<=299 and amount<399):
   print("you can apply 3 promocodes ZOMPAYTM and WELCOME50 and SIMPLPARTY and ")
   print("ZOMPAYTM and WELCOME50 will give you equal  discount")
   print("You Can apply any one of them")
else:
    print("You can apply 4 promocodes ZOMPAYTM and WELCOME50 and SIMPLPARTY and SBITREATS")
    print("SBITREATS will give you more discount")