﻿import os			#для паузы после отладки
print("ax^2+bx+c\n")		#вывод формулы дискриминанта
a=int(input("введите a: "))#ввод первой переменной
b=int(input("введите b: "))#ввод второй переменной
c=0				#переменной с присваивается значение 0
print("\nРешение через while\n")	#вывод сообщения о решении задачи через цикл while
while c<10:			#цикл while, пока значение с не станет равным 10
	c=c+1			#на каждом шаге цикла значение c увеличивается на 1
	d=b^2-4*a*c		#расчёт дискриминанта и запись его в переменную d
	if d<0:			#если дискриминант меньше 0
		print("d<0")	#вывести d<0
	else:			#иначе
		d=pow(d, 0.5)		#значению d присваивается корень дискриминанта
		x1=(-(b)-d)/(2*a)	#расчёт первого корня по формуле
		x2=(-(b)+d)/(2*a)	#расчёт второго корня по формуле
		print("для c=",c,"\n")	#вывод значения c, для которого рассчитываются корни
		print("x1 =",x1,"\nx2 =",x2,"\n")	#вывод корней
os.system("pause")					#пауза после отладки
