# hours = int(input("Enter Your Hours:"))
# regPay = 20
# overPay = 30
# totalPay = 0
#
# if hours <= 40:
#     totalPay = (regPay * hours)
#     print("Your weeks pay is: $", totalPay)
# elif hours > 40:
#     xtime = hours - 40
#     totalPay = (regPay * hours)
#     bigPay = ((overPay * xtime) + totalPay)
#     print("Your weeks pay w/ overtime is: $", bigPay)

hours = int(input("Enter Your Hours:"))
rate = 20
overtimeRate = 30
pay = 0

if hours <= 40:
    pay = ( rate * hours)
    print("Your weekly pay is: $", pay)
elif hours == 32:
    pay = (overtimeRate * (hours - 40 ) + (rate * hours) )
    print("Your weeks pay w/ overtime is: $", pay)