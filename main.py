Day_Entry=input("Enter amount of times Alex was 'negative' in Lesson: \n")
#Date=input("Enter date of the lesson: (DD/MM/YY)\n")
f=open("Alex.txt", "a")
f.write(Day_Entry)
f.write('\n')
f.close()
# Finding the total amount
Total=0
Myfile='Alex.txt'
f=open("Alex.txt", "r")
with open(Myfile) as f:
    for n in f:
        #n=n.split()
        Total=Total+int(n)
print("Current total:",Total)
f.close()