n = 10 #размерность карты

#элементы будут считаться от 1 до n-1, 0 и n -вспомогательные элементы = 0

a = list(range(n+2))
a[0] = list(map(lambda x: 0, list(range(n+2))))
a[n+1] = list(map(lambda x: 0, list(range(n+2))))

f = open("map_life.txt", "r")

i = 1

for line in f:

	a[i] = list(map(int, list(line[0:n]))) #исключаем 10й символ, превращаем в list и конвертируем символы в числа
	a[i].append(0)
	a[i].insert(0, 0)
	i+=1

t = 1
count = 0

while t:
	
	count = 0
	
	b = list(range(n+2))
	b[0] = list(map(lambda x: 0, list(range(n+2))))
	b[n+1] = list(map(lambda x: 0, list(range(n+2))))
	
	i = 1
	
	for lin in a[1:n+1]:
		
		j = 1
		
		b[i] = list(map(lambda x: 0, list(range(n+2))))
		
		for items in lin[1:n+1]:
			
			#печатаем ячейку поля
			
			#print(a[i][j])
			
			if a[i][j] == 0:
				print(" ", end = "")
			else:
				print("#", end = "")
		
			#рассматриваем ячейку a[i][j]
			#считаем живых соседей
			k = a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
			
			b[i][j] = a[i][j]
			
			if k <= 1:
				b[i][j] = 0
			
			if k == 2:
				b[i][j] = a[i][j]
			
			if k == 3 and a[i][j] == 0:
				b[i][j] = 1
				
			if k > 3:
				b[i][j] = 0
				
			#в count записываем количество живых клеток в новом поле
			count += b[i][j]
			k = 0
			
			j += 1
			
		i += 1
			
		#перенос строки
		print("|")
	
	print("_")
	
	if(a == b or count == 0):
		t = 0
		if a == b:
			print("stat")
		if count == 0:
			print("all died out")
	else:
		a = b

print("*The End*")