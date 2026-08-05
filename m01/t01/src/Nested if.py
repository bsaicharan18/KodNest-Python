from ast import If
Marks=int(input())
Attendence=int(input())
Project_completion=input()
if(Marks >= 60 and Attendence>= 75):
    if(Project_completion =="yes"):
        print("Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
    