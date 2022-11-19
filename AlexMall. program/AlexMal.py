# This program is to store the amount of times alex is 'negative' in chemistry alone.

Day_Entry=input("Enter amount of times Alex was 'negative' in Lesson: \n")
#Date=input("Enter date of the lesson: (DD/MM/YY)\n")
f=open("AlexEnteries.txt", "a")
f.write(Day_Entry)
f.write('\n')
f.close()
# Finding the total amount
Total=0
Myfile='AlexEnteries.txt'
f=open("AlexEnteries.txt", "r")
with open(Myfile) as f:
    for n in f:
        #n=n.split()
        Total=Total+int(n)
print("Current total:",Total)
f.close()