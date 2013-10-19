n=[["R/C","1","2","3"],["1"," "," "," "],["2"," "," "," "],["3"," "," "," "]]

def display():
	for x in n:
		for i in x:
			print(i,sep="|",end="\t")
		print('\n')

win1 = False
win2 = False
display()
u=1

user1 = input("Enter User1 name: ")
user2 = input("Enter User2 name: ")

while win1 != True or win2 !=True:
	if u%2==0:
		print(user2+"'s Turn")
	else:
		print(user1+"'s Turn")

	try:
		urow = int(input("Enter row no: "))
		ucol = int(input("Enter column no: "))
	except ValueError as e:
		print("Not a number. Try again")
		continue
	

	if urow > 3 or ucol > 3 or urow < 1 or ucol < 1:
		print("Invalid Position. Try again.\n")
		display()
		continue

	if n[urow][ucol] == "X" or n[urow][ucol] == "O":
		print("The position has already been marked. Please try another one","\n")
		display()
		continue

	if u%2 == 0:
		n[urow][ucol] = "O"
	else:
		n[urow][ucol] = "X"

	print("__________________________")

	display()
	u = u+1

	if n[1][1]=="X" and n[2][2]=="X" and n[3][3]=="X":
		win1 = True

	if n[1][3]=="X" and n[2][2]=="X" and n[3][1]=="X":
		win1 = True

	if n[1][1]=="O" and n[2][2]=="O" and n[3][3]=="O":
		win2 = True

	if n[1][3]=="O" and n[2][2]=="O" and n[3][1]=="O":
		win2 = True

	for k in range(1,4):
		if n[1][k]=="X" and n[2][k]=="X" and n[3][k]=="X":
			win1 = True
			break
		if n[1][k]=="O" and n[2][k]=="O" and n[3][k]=="O":
			win2 = True
			break

	for k in range(1,4):
		if n[k][1]=="X" and n[k][2]=="X" and n[k][3]=="X":
			win1 = True
			break
		if n[k][1]=="O" and n[k][2]=="O" and n[k][3]=="O":
			win2 = True
			break

	if win1:
		print("Congratulations!! %s has won!!") % (user1)
		break
	elif win2:
		print("Congratulations!! %s has won!!") % (user2)
		break
	elif u>=8:
		print("Game Draw!!")
		break
		
input()