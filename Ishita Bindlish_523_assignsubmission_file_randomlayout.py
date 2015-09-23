import random
width=80
height=30
def randomlayoutfunction():
	global width,height
	min_floor_width=55
	max_floor_width=70
	cage_width=6
	begin_ladder=0
	begin_broken=0
	broken_count=0	
	begin_cage=random.randint(1,width-1-cage_width)
	princess=random.randint(begin_cage+1,begin_cage+cage_width-2)

	if begin_cage+cage_width-1 > 55 :
		direc = "right"
	else:
		direc = "left"
	
	#Boundary
	B=[]
	for i in range(height):
		B_sub=[]
		if i == 0 or i == height-1:
			for j in range(width):
				B_sub.append('X')
		elif i == 1:
			for j in range(width):
				if j == 0 or j == begin_cage or j == begin_cage+cage_width-1 or j == width-1:
					B_sub.append('X')
				elif j == princess:
					B_sub.append('Q')
				else:
					B_sub.append(' ')
		elif i == 2:
			begin_ladder=random.randint(begin_cage+1,begin_cage+cage_width-2)
			for j in range(width):
				if j == 0 or j == width-1:
					B_sub.append('X')
				elif j >= begin_cage and j<= begin_cage+cage_width-1:
					B_sub.append('X')
				else:	
					B_sub.append(' ')
			
		elif (i-5)%4 == 0:
			floor_width=random.randint(min_floor_width,max_floor_width)
			if direc == "left":
				begin_floor = 1
				direc = "right"
			else:
				begin_floor = width-floor_width-1
				direc = "left"
			for j in range(width):
				if j == 0 or j == width-1 or (j>=begin_floor and j<=begin_floor+floor_width+1):
					B_sub.append('X')
				else:
					B_sub.append(' ')
		else:
			for j in range(width):
				if j == 0 or j == width-1:
					B_sub.append('X')
				else:
			 		B_sub.append(' ')

		B_sub="".join(B_sub)
		B.append(B_sub)

	i=0
	for j in B:
		j=list(j)
		if i == 2:
			begin_ladder=random.randint(begin_cage+1,begin_cage+cage_width-2)	
			j[begin_ladder]='H'
		elif (i-5)%4 == 0 and i!=height-1 and i!=1:
			x=0
			y=0
			if i+4 != height-1:
				for a in range(1,width-2):
					if B[i][a] == ' ' and B[i][a+1] == 'X' and a!=width-2:
						x = a+1
					elif B[i][a-1] == 'X' and B[i][a] == ' ' and a!=1:
						y = a-1
					elif B[i+4][a-1] == 'X' and B[i+4][a] == ' ' and a!=1:
						y = a-1 
					elif B[i+4][a] == ' ' and B[i+4][a+1] == 'X' and a!=width-2:
						x = a+1
			else:
		  		for a in range(1,width-2):
					if B[i][a] == ' ' and B[i][a+1] == 'X' and a!=width-2:
						x = a+1
						y = width-2
					elif B[i][a-1] == 'X' and B[i][a] == ' ' and a!=1:
						y = a-1
						x = 1
			begin_ladder=random.randint(x,y)
			begin_broken=begin_ladder
			broken_count=1
			while begin_ladder == begin_broken:
				begin_broken=random.randint(x,y)
			j[begin_ladder]='H'
			j[begin_broken]='H'
		elif i > 2 and i!=height-1:
			k=0
			if i>5:
				broken_count+=1
			while k<width:
				if k == begin_ladder:
					j[begin_ladder] = 'H'
				elif k == begin_broken and broken_count != 3 and i>5:
					j[begin_broken] = 'H'
				k=k+1
		j="".join(j)
		B[i]=j
		i=i+1
	return B
		
