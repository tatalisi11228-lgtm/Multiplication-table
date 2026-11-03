# تمرین ۰۲ — داستان خنده‌دار (Mad Libs)
#
# صورت تمرین:
#   یک داستان کوتاه می‌نویسی که چند جای آن خالی است. از کاربر می‌پرسی
#   چه کلمه‌ای در هر جای خالی بگذارد، و بعد داستان کامل را چاپ می‌کنی.
#
# نمونهٔ اجرا (خروجی تو باید شبیه این باشد):
#   Enter a name: Ali
#   Enter an adjective: sleepy
#   Enter a verb: jump
#   Enter a place: school
#
#   Ali was very sleepy one morning.
#   Suddenly, Ali decided to jump all the way to school.
#   Everyone at school was amazed!
#
# ابزارهایی که لازم داری:
#   input("...")   گرفتن یک کلمه از کاربر
#   print(...)     چاپ کردن
#   f"..."         گذاشتن کلمه‌ها داخل متن
#
# تفاوت مهم با تمرین ۰۱:
#   در تمرین ۰۱ مجبور بودی با float() متن را به عدد تبدیل کنی.
#   اینجا نه! چون می‌خواهیم خودِ «کلمه» را داخل جمله بگذاریم.
#   پس سؤال درست این است: کِی باید تبدیل کنی و کِی نه؟
#
# چالش اضافه (اختیاری):
#   یک کلمهٔ پنجم هم بگیر (مثلاً یک رنگ) و آن را دو بار در داستان به کار ببر.

# کد خودت را از این‌جا بنویس
name = input("Enter a name:")
adjective = input("Enter an adjective:")
verb = input("Enter a verb:")
place = input("Enter a place:")

print(f"{name} was very {adjective} one morning.\nSuddenly, {name} decided to {verb} all the way to {place}.\nEveryone at {place} was amazed!")
