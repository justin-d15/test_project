# x = input("x= ")
# y = bool(x)
# if y == False:
#     print("you have not entered anything")
# else:
#     print(f"x={x}")
def greet():
    print("hi there:)")
    print("NOT>:)")


temp = input("temperture=")
try:
    temp = int(temp)
    if temp == 100:
        print("hi,BBQ")
    elif temp < 20:
        print("冻死了屁的了！")
        greet()
    elif temp > 30:
        print("热死了屁的了！")

except:
    print("pls input number not word")
