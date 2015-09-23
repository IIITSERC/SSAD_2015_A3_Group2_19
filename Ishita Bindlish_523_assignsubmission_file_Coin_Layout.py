import randomlayout
import random
B=[]

#class Set_Coins:
#	global B
#	count_coins=0
B=randomlayout.randomlayoutfunction()
def randomize_coins():
		count_coins=0
		row=list(B[28])
		row[1]='P'
		B[28]="".join(row)
		while count_coins<20:
			x=random.randint(4,28)
			y=random.randint(1,78)
			if (B[x][y]==' ' and (B[x+1][y]=='X' or (B[x+1][y]=='H' and B[x-1][y]==' ')) and B[x][y]!='C' and B[x][y]!='P' and B[x][y]!='D'):
				row=list(B[x])
				row[y]='C'
				B[x]="".join(row)
				count_coins=count_coins+1
		return B
#def main():
#B=randomlayout.randomlayoutfunction()
#c=Set_Coins()
#c.randomize_coins
#print type(B)


