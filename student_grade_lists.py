print("=" * 10 , "students scores" "=" * 10)
people = []
n = int(input("> How many students we have ?\n> "))
for i in range(n) :
    print(f"----student information {i + 1}----")
    name = input ("Enter name : ")
    score = float(input("Enter score : "))
    people.append ({"name" : name , "score" : score})

print("\n===== searching student=====")
search_name = input ("> Who are you searching for ? ")
found = False
for person in people :
    if person ["name"] == search_name :
        print (f"> Found\nstudent : {person["name"]} | score : {person["score"]}")
# تو خط قبلی هم باید اسم و نمره رو از توی لیست انتخاب کنیم اگه فقط متغییر رو بزاریم درسته که به ظاهر کار میکنه ولی یه خطای خاموشه
        found = True
# اینجا بریک نزاشتم که اگه چند تا اسم تکراری داشتیم همه رو چاپ کنه

if not found :
    print("This student is not available")
