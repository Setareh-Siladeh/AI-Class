age = int(input("سن مشتری: "))
day = input("روز هفته: ")

if age < 5:
    price = 0
elif age <= 12:
    price = 50000
elif age >= 60:
    price = 60000
else:
    price = 100000

if day == "سه‌شنبه":
    price = price * 0.8

if price == 0:
    print("ورود رایگان!")
else:
    print("قیمت بلیط:", int(price), "تومان")