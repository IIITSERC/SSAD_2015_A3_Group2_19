import randomlayout
import Coin_Layout
import time
import os,sys,random
from threading import Thread

#Class with the extra information on the Board

class Board:
	def __init__(self,level):
		self.__level=level
	def layout(self,p):
		for i in Coin_Layout.B:
			print i
		score = p.return_player_score()
		coins = p.return_player_coins()
		lives = p.return_player_lives()
		print "LEVEL = "+str(self.__level)
		print "SCORE = "+str(score)
		print "COINS COLLECTED = "+str(coins)
		print "LIVES = "+str(lives)
	def return_player_level(self):
		return self.__level

#Class containing the common features of Donkey and Player

class Element:
	def __init__(self,board_row,board_column):
		self.board_row=board_row
		self.board_column=board_column
	def return_x_pos(self):
		return self.board_row
	def return_y_pos(self):
		return self.board_column
	def move_left(self,c,temp):
		l=list(Coin_Layout.B[self.board_row])
		l[self.board_column]=temp
		temp=l[self.board_column-1]
		l[self.board_column-1]=c
		Coin_Layout.B[self.board_row]="".join(l)
		self.board_column-=1
		if c == 'D':
			return temp
	def move_right(self,c,temp):
		l=list(Coin_Layout.B[self.board_row])
		l[self.board_column]=temp
		temp=l[self.board_column+1]
		l[self.board_column+1]=c
		Coin_Layout.B[self.board_row]="".join(l)
		self.board_column+=1
		if c == 'D':
			return temp

#Class defining the abilities of the Player
	
class Player(Element):
	def __init__(self,lives,score,board_row,board_column,coins):
		self.__lives=lives
		self.__score=score
		self.board_row=board_row
		self.board_column=board_column
		self.__coins=coins
	def move_up(self,temp):
		l1=list(Coin_Layout.B[self.board_row-1])
		l2=list(Coin_Layout.B[self.board_row])
		if l1[self.board_column]!='':
			l1[self.board_column]='P' 
			l2[self.board_column]=temp
		Coin_Layout.B[self.board_row-1]="".join(l1)
		Coin_Layout.B[self.board_row]="".join(l2)
		self.board_row-=1
	def move_down(self,temp,c):
		l1=list(Coin_Layout.B[self.board_row+1])
		l2=list(Coin_Layout.B[self.board_row])
		l2[self.board_column]=temp
		temp=l1[self.board_column]
		l1[self.board_column]=c
		Coin_Layout.B[self.board_row+1]="".join(l1)
		Coin_Layout.B[self.board_row]="".join(l2)
		self.board_row+=1

	def jump(self,direc,temp):
		if direc == "left":
			flag=0
	       		l1=[]
	 		l1.append(Coin_Layout.B[self.board_row][self.board_column-3])
 			l1.append(Coin_Layout.B[self.board_row-1][self.board_column-3])	 
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column-2])
			l1.append(Coin_Layout.B[self.board_row-2][self.board_column-2])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column-2])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column-1])
		        l1.append(Coin_Layout.B[self.board_row][self.board_column-1])
			l1.append(temp)
			if Coin_Layout.B[self.board_row+1][self.board_column-4] == 'X' or Coin_Layout.B[self.board_row+1][self.board_column-4] == 'H': 
				flag = 1
			self.move_left('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_left('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_left('P',l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_left('P',l1.pop())
			if flag == 0:
				l1=[]
				l1=list(Coin_Layout.B[self.board_row])
				l1[self.board_column] = ' '
				Coin_Layout.B[self.board_row] = "".join(l1)
				if Coin_Layout.B[self.board_row+4][self.board_column] == 'C':
					self.Calc_Coins()
				l1=list(Coin_Layout.B[self.board_row+4])
				l1[self.board_column] = 'P'
				Coin_Layout.B[self.board_row+4]="".join(l1)
				self.board_row+=4
		else:
			flag=0
			l1=[]
			l1.append(Coin_Layout.B[self.board_row][self.board_column+3])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column+3])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column+2])
			l1.append(Coin_Layout.B[self.board_row-2][self.board_column+2])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column+2])
			l1.append(Coin_Layout.B[self.board_row-1][self.board_column+1])
		        l1.append(Coin_Layout.B[self.board_row][self.board_column+1])
			l1.append(temp)
			if Coin_Layout.B[self.board_row+1][self.board_column+4] == 'X' or Coin_Layout.B[self.board_row+1][self.board_column+4] == 'H': 
				flag = 1
			self.move_right('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_right('P',l1.pop())
			self.move_up(l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_right('P',l1.pop())
			time.sleep(0.5)
			self.move_down(l1.pop(),'P')
			self.move_right('P',l1.pop())

			if flag == 0:
				l1=[]
				l1=list(Coin_Layout.B[self.board_row])
				l1[self.board_column] = ' '
				Coin_Layout.B[self.board_row] = "".join(l1)
				if Coin_Layout.B[self.board_row+4][self.board_column] == 'C':
					self.Calc_Coins()
				l1=list(Coin_Layout.B[self.board_row+4])
				l1[self.board_column] = 'P'
				Coin_Layout.B[self.board_row+4] = "".join(l1)
				self.board_row+=4
				
	def return_player_coins(self):
		return self.__coins
	def return_player_score(self):
		return self.__score
	def return_player_lives(self):
		return self.__lives
	def Calc_Coins(self):
		self.__coins+=1
		self.__score+=5
							
	def checkCollision(self,row,column):
		if self.__lives>0:
			if Coin_Layout.B[self.board_row][self.board_column-1] == 'O' or Coin_Layout.B[self.board_row][self.board_column+1] == 'O' or Coin_Layout.B[self.board_row-1][self.board_column] == 'O' or Coin_Layout.B[self.board_row+1][self.board_column] == 'O' or Coin_Layout.B[self.board_row][self.board_column-1] == 'D' or Coin_Layout.B[self.board_row][self.board_column+1] == 'D':
				self.__lives=self.__lives-1
				self.__score=self.__score-25
				l1=list(Coin_Layout.B[self.board_row])
				l1[self.board_column]=' '
				Coin_Layout.B[self.board_row]="".join(l1)				
				self.board_row=28
				self.board_column=1
				l1=list(Coin_Layout.B[self.board_row])
				l1[self.board_column]='P'
				Coin_Layout.B[self.board_row]="".join(l1)
				return 1
		else:
			return 2		
		
	def ChangeDirec(self,direc):
		if direc == "left":
			if Coin_Layout.B[self.board_row][self.board_column-1]=='X':
				return 1
		elif Coin_Layout.B[self.board_row][self.board_column+1]=='X':
				return 1
		else:
				return 0

#Class defining the abilities of the Donkey

class Donkey(Element):
	def __init__(self,board_row,board_column):
		self.board_row=board_row
		self.board_column=board_column
	def ChangeDirec(self):	
		if Coin_Layout.B[self.board_row][self.board_column-1]=='X' or Coin_Layout.B[self.board_row+1][self.board_column-1] == ' ':
				return "right"
		elif Coin_Layout.B[self.board_row][self.board_column+1]=='X' or Coin_Layout.B[self.board_row+1][self.board_column+1] == ' ':
				return "left"
		else:
			lis = ["right","left"]
			return (lis[random.randint(0,1)])


def main(level,lives,score,coins):
	global p,r,b,d
	Coin_Layout.B=Coin_Layout.randomize_coins()
	b = Board(level)
	p = Player(lives,score,randomlayout.height-2,1,coins)

	y=50                              #initialising donkey's position in the middle of the floor 	
	d=Donkey(4,y)
	r = 1

main(1,3,0,0)

#Function to control the movement of the Player

def Player_Movement():

	global p,r,b
	choice='t' 

	while choice!='q':
		os.system('clear')
		b.layout(p)
		level=b.return_player_level()
		row=p.return_x_pos()
		column=p.return_y_pos()
		lives=p.return_player_lives()
		score=p.return_player_score()
		coins=p.return_player_coins()

		if row == 1:					#Total levels in game=3
			b=Board(level+1)
			if level < 3:
				main(level+1,lives,score,coins)
			else:
				print "YOU HAVE FINISHED THE GAME!"
				choice = 'q'
			continue

		os.system("stty cbreak -echo")          #enter isn't required for input
		choice=sys.stdin.read(1)
		os.system("stty -cbreak echo")	

		if choice == ' ':	
			os.system("stty cbreak -echo")
			choice1=sys.stdin.read(1)
			os.system("stty -cbreak echo")	

		#The following are the situations in which the player's previous position had an "H"

		if Coin_Layout.B[row-1][column] == 'H' or (Coin_Layout.B[row][column-1] == 'X' and Coin_Layout.B[row][column+1] == 'X') or (Coin_Layout.B[row][column-1] == 'H' and Coin_Layout.B[row][column+1] == 'X') or (Coin_Layout.B[row][column-1] == 'X' and Coin_Layout.B[row][column+1] == 'H') or (Coin_Layout.B[row][column-1] == 'X' and Coin_Layout.B[row][column+1] == ' ' and column!=1) or (Coin_Layout.B[row][column-1] == ' ' and Coin_Layout.B[row][column+1] == 'X' and column!=randomlayout.width-2) or Coin_Layout.B[row-2][column] == 'H':
				temp = 'H'
		else:
			temp = ' '
		if choice == 'a':
			x=p.ChangeDirec("left")
			print "x = "+str(x)
			if x != 1:
				x1=p.checkCollision(p.return_x_pos(),p.return_y_pos())
				if x1==2:
					print "GAME OVER"
					choice='q' 
				elif x1==1:
					p.board_row=28
					p.board_column=1
				else:
					if Coin_Layout.B[row][column-1] == 'C':
						p.Calc_Coins()
					if Coin_Layout.B[row+1][column-1]!=' ':
						p.move_left('P',temp)
					else:
						l1=[]
						l1=list(Coin_Layout.B[row])
						l1[column]=temp
						Coin_Layout.B[row]="".join(l1)
						l1=list(Coin_Layout.B[row+4])
						l1[column-1]='P'
						Coin_Layout.B[row+4]="".join(l1)
						p=Player(lives,score,row+4,column-1,coins)
		elif choice == 'd' :
			x=p.ChangeDirec("right")
			if x!=1:
				x1=p.checkCollision(row,column)
				if x1==2:
					print "GAME OVER"
					choice='q' 
				elif x1==1:
					p.board_row=28
					p.board_column=1
				else:
					if Coin_Layout.B[row][column+1] == 'C':
						p.Calc_Coins()
					if Coin_Layout.B[row+1][column+1]!=' ':
						p.move_right('P',temp)
					else:
						l1=[]
						l1=list(Coin_Layout.B[row])
						l1[column]=temp
						Coin_Layout.B[row]="".join(l1)
						l1=list(Coin_Layout.B[row+4])
						l1[column+1]='P'
						Coin_Layout.B[row+4]="".join(l1)
						p=Player(lives,score,row+4,column+1,coins)
		elif choice == 'w':
			x1=p.checkCollision(row,column)
			if x1==2:
				print "GAME OVER"
				choice='q' 
			elif x1==1:
				p.board_row=28
				p.board_column=1
			else:
				if Coin_Layout.B[row-1][column] == 'C':
					p.Calc_Coins()
				if Coin_Layout.B[row-1][column] == 'H' or ((Coin_Layout.B[row][column-1]=='X' or Coin_Layout.B[row][column+1]=='X') and Coin_Layout.B[row+1][column]=='H'):
					p.move_up(temp)

		elif choice == 's':
			x1=p.checkCollision(row,column)
			if x1==2:
				print "GAME OVER"
				choice='q' 
			elif x1==1:
				p.board_row=28
				p.board_column=1
			else:
				if Coin_Layout.B[row+1][column] == 'H':
					p.move_down(temp,'P')
		elif choice == ' ':
			if choice1 == 'd':
				if Coin_Layout.B[row][column+1] != 'X' and Coin_Layout.B[row][column+2] != 'X' and Coin_Layout.B[row][column+3] != 'X' and Coin_Layout.B[row][column+4] != 'X':						p.jump("right",temp)
			elif choice1 == 'a':					
				if Coin_Layout.B[row][column-1] != 'X' and Coin_Layout.B[row][column-2] != 'X' and Coin_Layout.B[row][column-3] != 'X' and Coin_Layout.B[row][column-4] != 'X':
					p.jump("left",temp)
		
	r = 0

#Function that controls the movement of the donkey on the topmost floor

def Donkey_Movement():		
	global p,b,d,r
	add=' '
	direc=''
	level=b.return_player_level()
	while r:
		d_x=d.return_x_pos()
		d_y=d.return_y_pos()	
		
		direc = d.ChangeDirec()
		if direc == "right":
			add=d.move_right('D',add)
		else:
			add=d.move_left('D',add)
		os.system('clear')
		b.layout(p)
                                                 
		if level==1:                    
			time.sleep(0.4)
		elif level==2:
			time.sleep(0.3)
		else:
			time.sleep(0.2)

#Enables the two functions to work at the same time

thread1=Thread(target=Donkey_Movement)
thread2=Thread(target=Player_Movement)

thread1.start()
thread2.start()
