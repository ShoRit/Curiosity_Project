
#from tkinter import *
# try:
# 	import tkinter as tk
# except:	
import tkinter as tk
import random
import os
import time
import subprocess
from decimal import Decimal

color=['black','white']
transport=['train','boat']
drink=['wine','water']

possible_choices=[(i,j,k) for i in color for j in transport for k in drink ]
random.shuffle(possible_choices)
options=possible_choices[:int(len(possible_choices)/2)]

# response_array=[0,0,0,0]

response_flags=[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
favourite=['','','']
start_time_array=[0,0,0,0,0]

# def add_label(f1,item):
# 	if 

def raise_frame(frame):
	if frame==f1:
		start_time_array[0]=time.time()
		response_flags[0][0]=1
		tk.Label(f1, font=("Georgia", 25), text=text1).pack(side=tk.TOP,pady=10)
		tk.Label(f1, font=("Georgia", 15),text=wtc).pack(side=tk.TOP,pady=10)
		tk.Button(f1,font=("Georgia", 15), text='Yes',height=2,width=10, command=lambda:raise_frame(f2)).pack(side=tk.TOP, padx=50,pady=10)
		tk.Button(f1,font=("Georgia", 15), text='No',height=2,width=10, command=lambda:raise_frame(f4)).pack(side=tk.TOP, padx=50,pady=10)

	if frame==f4:
		start_time_array[1]=time.time()
		response_flags[1][0]=1
	if frame==f7:
		start_time_array[2]=time.time()
		response_flags[2][0]=1
	if frame==f10:
		start_time_array[3]=time.time()
		response_flags[3][0]=1
		try:
			subprocess.call(['mpg123','eerie.mp3'])
		except Exception as e:
			subprocess.call(['afplay','eerie.mp3']) 	

	if frame==f13:
		start_time_array[4]=time.time()	

	if frame==f2:
		response_flags[0][2]=1
	if frame==f3:
		response_flags[0][1]=1
	if frame==f5:
		response_flags[1][2]=1
	if frame==f6:
		response_flags[1][1]=1

	if frame==f8:
		response_flags[2][2]=1
	if frame==f9:
		response_flags[2][1]=1	

	if frame==f11:
		response_flags[3][2]=1

	if frame==f12:
		response_flags[3][1]=1
		if options[3][1]=='train':
			try:
				subprocess.call(['mpg123','train_2.mp3'])
			except Exception as e:
				subprocess.call(['afplay','train_2.mp3'])
		else:
			try:
				subprocess.call(['mpg123','ship_2.mp3'])	
			except Exception as e:
				subprocess.call(['afplay','ship_2.mp3'])			

	if frame==f13:	
		for i in range(0,4):
			for j in range(0,3):
				if response_flags[i][j]==0:
					table_elems[i+1][j+1]='[Did not continue]'
				else:
					if options[i][j] in favourite:
						table_elems[i+1][j+1]=options[i][j]+'*'
					else:
						table_elems[i+1][j+1]=options[i][j]	

		for i in range(1,len(start_time_array)):
			table_elems[i][4]= round(Decimal(start_time_array[i]-start_time_array[i-1]),3)  		 
		for i in range(height): #Rows
			for j in range(width): #Columns
				b = tk.Entry(f13, font=("Georgia", 20) )
				b.grid(row=i, column=j)
				b.insert(tk.END,str(table_elems[i][j]))
			
	# print(table_elems)	
	frame.tkraise()	
	# print(response_flags)

def quit_window():
	root.destroy()

def record_color():
	item=str(var1.get())
	#print(item)
	if item=='white':
		favourite[0]='white'
	if item =='black':
		favourite[0]='black'

def record_transport():
	item=str(var2.get())		
	if item =='train':		
		favourite[1]='train'
	if item =='boat':		
		favourite[1]='boat'

def record_drink():
	item=str(var3.get())		
	if item =='wine':
		favourite[2]='wine'
	if item=='water':
		favourite[2]='water'


root = tk.Tk()
root.minsize(width=666, height=666)
var1=tk.StringVar()
var2=tk.StringVar()
var3=tk.StringVar()
# root.overrideredirect(False)
# root.attributes('-fullscreen',True)

#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
'''
   "1) "	 It was one of  those eerie Mondays in August, a particularly strange day as everything was tinted [color variable]." 

·      "2) "	 Unable to taketake it anymore, Amelia reached for her glass of [drink variable]." 

·      "3) "	 She would not stay here a moment longer. Her bags were packed, and the [transport variable] was waiting."
'''
f1 = tk.Frame(root)
f2 = tk.Frame(root)
f3 = tk.Frame(root)
f4 = tk.Frame(root)
f5 = tk.Frame(root)
f6 = tk.Frame(root)
f7 = tk.Frame(root)
f8 = tk.Frame(root)
f9 = tk.Frame(root)
f10 = tk.Frame(root)
f11 = tk.Frame(root)
f12 = tk.Frame(root)
f13 = tk.Frame(root)
f14 = tk.Frame(root)
f15 = tk.Frame(root)
f16 = tk.Frame(root)

# f=('Georgia',25)

text_start="Hello, Thank you for participating.\n Before we begin we would love to know you a bit better "
tk.Label(f14, text=text_start,font=("Georgia", 15)).pack(side=tk.TOP,pady=10)

fav_col= "What is your favourite color ?"
tk.Label(f14, text=fav_col,font=("Georgia", 20)).pack(side=tk.TOP,pady=20)
tk.Radiobutton(f14, indicatoron=0,width=15, text='White',font=("Georgia", 15),value='white',variable=var1, height=2, command= lambda: record_color()).pack(side=tk.TOP, padx=50,pady=10)
tk.Radiobutton(f14, indicatoron=0,width=15,text='Black',font=("Georgia", 15),value='black', variable= var1,height=2, command= lambda: record_color()).pack(side=tk.TOP, padx=50,pady=10)

fav_trans= "What is your favourite mode of transport ?"
tk.Label(f14, text=fav_trans,font=("Georgia", 20)).pack(side=tk.TOP,pady=20)
tk.Radiobutton(f14, indicatoron=0,width=15, text='Train', font=("Georgia", 15), value='train', variable=var2,  height=2, command= lambda: record_transport()).pack(side=tk.TOP, padx=50,pady=10)
tk.Radiobutton(f14, indicatoron=0,width=15,text='Boat',font=("Georgia", 15),value='boat', variable= var2, height=2, command= lambda: record_transport()).pack(side=tk.TOP, padx=50,pady=10)

fav_drink= "What is your favourite drink ?"
tk.Label(f14, font=("Georgia", 20),text=fav_drink).pack(side=tk.TOP,pady=20)
tk.Radiobutton(f14, indicatoron=0,width=15,text='Water',font=("Georgia", 15),variable=var3, value='water', height=2, command= lambda: record_drink()).pack(side=tk.TOP, padx=50,pady=10)
tk.Radiobutton(f14, indicatoron=0,width=15,text='Wine', font=("Georgia", 15),variable=var3, value='wine', height=2, command= lambda: record_drink()).pack(side=tk.TOP, padx=50,pady=10)


text_end='Thank you for your options. Enjoy'
tk.Label(f14, font=("Georgia", 13), text=text_end).pack(side=tk.TOP,pady=20)
tk.Button(f14, font=("Georgia", 13), text='Proceed',height=2,width=10, command=lambda:raise_frame(f1)).pack(side=tk.TOP, padx=50,pady=10)


for frame in (f1, f2, f3, f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15,f16):

	frame.grid(row=0, column=0, sticky='news')
# For first session
text1="It was one of those eerie Mondays in August, a particularly strange day as everything was tinted "+ options[0][0]
wtc="Do you wish to continue ?"


tk.Label(f2, font=("Georgia", 25), text=text1).pack(side=tk.TOP,pady=10)
tk.Label(f2, font=("Georgia", 15),text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f2, font=("Georgia", 15),text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f2, font=("Georgia", 15), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text2="	 Unable to take it anymore, Amelia reached for her glass of "+ options[0][2] 
tk.Label(f2, font=("Georgia", 25),text=text2).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f2, font=("Georgia", 15),text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f2,font=("Georgia", 15), text='Yes',height=2,width=10, command=lambda:raise_frame(f3)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f2,font=("Georgia", 15), text='No',height=2,width=10, command=lambda:raise_frame(f4)).pack(side=tk.TOP, padx=50)

tk.Label(f3, font=("Georgia", 25), text=text1).pack(side=tk.TOP,pady=10)
tk.Label(f3, font=("Georgia", 15),text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f3, font=("Georgia", 15), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f3,font=("Georgia", 15), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
tk.Label(f3, font=("Georgia", 25),text=text2).pack(side=tk.TOP,pady=10)
tk.Label(f3, font=("Georgia", 15),text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f3, font=("Georgia", 15),text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f3, font=("Georgia", 15),text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text3="	 She would not stay here a moment longer. Her bags were packed, and the "+ options[0][1] +" was waiting." 
tk.Label(f3,font=("Georgia", 25), text=text3).pack(side=tk.TOP,pady=10)
tk.Button(f3,font=("Georgia", 15), text='Please click here',height=2,width=20, command=lambda:raise_frame(f4)).pack(side=tk.TOP, padx=50,pady=10)


# For second session

text4="It was one of those eerie Mondays in August, a particularly strange day as everything was tinted "+ options[1][0]
tk.Label(f4,font=("itc zapf chancery", 30), text=text4).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f4, font=("itc zapf chancery", 20),text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f4, font=("itc zapf chancery", 20), text='Yes',height=2,width=10, command=lambda:raise_frame(f5)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f4, font=("itc zapf chancery", 20),text='No',height=2,width=10, command=lambda:raise_frame(f7)).pack(side=tk.TOP, padx=50,pady=10)


tk.Label(f5,font=("itc zapf chancery", 30), text=text4).pack(side=tk.TOP,pady=10)
tk.Label(f5,font=("itc zapf chancery", 20), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f5,font=("itc zapf chancery", 20), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f5,font=("itc zapf chancery", 20), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text5="	 Unable to take it anymore, Amelia reached for her glass of "+ options[1][2] 
tk.Label(f5,font=("itc zapf chancery", 30), text=text5).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f5,font=("itc zapf chancery", 20), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f5,font=("itc zapf chancery", 20), text='Yes',height=2,width=10, command=lambda:raise_frame(f6)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f5,font=("itc zapf chancery", 20), text='No',height=2,width=10, command=lambda:raise_frame(f7)).pack(side=tk.TOP, padx=50)

tk.Label(f6,font=("itc zapf chancery", 30), text=text4).pack(side=tk.TOP,pady=10)
tk.Label(f6,font=("itc zapf chancery", 20), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f6,font=("itc zapf chancery", 20), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f6,font=("itc zapf chancery", 20), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
tk.Label(f6,font=("itc zapf chancery", 30), text=text5).pack(side=tk.TOP,pady=10)
tk.Label(f6,font=("itc zapf chancery", 20), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f6,font=("itc zapf chancery", 20), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f6,font=("itc zapf chancery", 20), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text6="	 She would not stay here a moment longer. Her bags were packed, and the "+ options[1][1] +" was waiting." 
tk.Label(f6,font=("itc zapf chancery", 30), text=text6).pack(side=tk.TOP,pady=10)
tk.Button(f6,font=("itc zapf chancery", 20), text='Please click here',height=2,width=20, command=lambda:raise_frame(f7)).pack(side=tk.TOP, padx=50,pady=10)

### For third session 
if options[2][0]=='black':
	s3_bg='black'
	tfc='white'
else:
	s3_bg='white'
	tfc='black'		


f7['bg']=s3_bg
f8['bg']=s3_bg
f9['bg']=s3_bg
s3_bg2='black'
text7="	 It was one of those eerie Mondays in August, a particularly strange day as everything was tinted "+ options[2][0]
tk.Label(f7,font=("Georgia", 25), text=text7,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f7,font=("Georgia", 15), text=wtc,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
tk.Button(f7,font=("Georgia", 15), text='Yes',height=2,width=10,bg=s3_bg2, command=lambda:raise_frame(f8)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f7,font=("Georgia", 15), text='No',height=2,width=10,bg=s3_bg2, command=lambda:raise_frame(f10)).pack(side=tk.TOP, padx=50,pady=10)


tk.Label(f8, font=("Georgia", 25), text=text7,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
tk.Label(f8, font=("Georgia", 15),text=wtc,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
tk.Button(f8,font=("Georgia", 15), text='Yes',height=2,width=10,bg=s3_bg2,).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f8, font=("Georgia", 15),text='No',height=2,width=10,bg=s3_bg2,).pack(side=tk.TOP, padx=50)
text8="	 Unable to take it anymore, Amelia reached for her glass of "+ options[2][2] 
tk.Label(f8, font=("Georgia", 25), text=text8,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f8, font=("Georgia", 15),text=wtc,bg=s3_bg,fg=tfc).pack(side=tk.TOP,pady=10)
tk.Button(f8,font=("Georgia", 15),bg=s3_bg2, text='Yes',height=2,width=10, command=lambda:raise_frame(f9)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f8,font=("Georgia", 15),bg=s3_bg2, text='No',height=2,width=10, command=lambda:raise_frame(f10)).pack(side=tk.TOP, padx=50)

tk.Label(f9, font=("Georgia", 25),bg=s3_bg,fg=tfc, text=text7).pack(side=tk.TOP,pady=10)
tk.Label(f9, font=("Georgia", 15),bg=s3_bg,fg=tfc,text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f9,font=("Georgia", 15),bg=s3_bg2, text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f9,font=("Georgia", 15),bg=s3_bg2, text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
tk.Label(f9, font=("Georgia", 25),bg=s3_bg,fg=tfc, text=text8).pack(side=tk.TOP,pady=10)
tk.Label(f9, font=("Georgia", 15),bg=s3_bg,fg=tfc,text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f9,font=("Georgia", 15),bg=s3_bg2, text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f9,font=("Georgia", 15),bg=s3_bg2, text='No',height=2,width=10).pack(side=tk.TOP, padx=50)

# train_logo=tk.PhotoImage(file='train.ppm')
# tk.Label(f9,image=train_logo).place(x=0,y=0,relwidth=1,relheight=1)

# tk.Label(f9, image=train_logo).pack(side=tk.RIGHT,pady=10)
text9="	 She would not stay here a moment longer. Her bags were packed, and the "+ options[2][1] +" was waiting." 
tk.Label(f9,font=("Georgia", 25),bg=s3_bg,fg=tfc, text=text9).pack(side=tk.TOP,pady=10)
tk.Button(f9,font=("Georgia", 15),bg=tfc,fg=s3_bg2, text='Please click here',height=2,width=20, command=lambda:raise_frame(f10)).pack(side=tk.TOP, padx=50,pady=10)

##### For 4th session


text10="It was one of those eerie Mondays in August, a particularly strange day as everything was tinted "+ options[3][0]
tk.Label(f10,font=("Georgia", 25), text=text10).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f10,font=("Georgia", 15), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f10,font=("Georgia", 15), text='Yes',height=2,width=10, command=lambda:raise_frame(f11)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f10,font=("Georgia", 15), text='No',height=2,width=10, command=lambda:raise_frame(f13)).pack(side=tk.TOP, padx=50,pady=10)


tk.Label(f11,font=("Georgia", 25), text=text10).pack(side=tk.TOP,pady=10)
tk.Label(f11,font=("Georgia", 15), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f11,font=("Georgia", 15), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f11,font=("Georgia", 15), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text11="	 Unable to take it anymore, Amelia reached for her glass of "+ options[3][2] 
tk.Label(f11,font=("Georgia", 25), text=text11).pack(side=tk.TOP,pady=10)
wtc="Do you wish to continue ?"
tk.Label(f11,font=("Georgia", 15), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f11,font=("Georgia", 15), text='Yes',height=2,width=10, command=lambda:raise_frame(f12)).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f11,font=("Georgia", 15), text='No',height=2,width=10, command=lambda:raise_frame(f13)).pack(side=tk.TOP, padx=50)

tk.Label(f12,font=("Georgia", 25), text=text10).pack(side=tk.TOP,pady=10)
tk.Label(f12,font=("Georgia", 15), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f12,font=("Georgia", 15), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f12,font=("Georgia", 15), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
tk.Label(f12,font=("Georgia", 25), text=text11).pack(side=tk.TOP,pady=10)
tk.Label(f12,font=("Georgia", 15), text=wtc).pack(side=tk.TOP,pady=10)
tk.Button(f12,font=("Georgia", 15), text='Yes',height=2,width=10).pack(side=tk.TOP, padx=50,pady=10)
tk.Button(f12,font=("Georgia", 15), text='No',height=2,width=10).pack(side=tk.TOP, padx=50)
text12="	 She would not stay here a moment longer. Her bags were packed, and the "+ options[3][1] +" was waiting." 
tk.Label(f12,font=("Georgia", 25), text=text12).pack(side=tk.TOP,pady=10)
tk.Button(f12,font=("Georgia", 15), text='End',height=2,width=20, command=lambda:raise_frame(f13)).pack(side=tk.TOP, padx=50,pady=10)


height = 5
width = 5
table_elems=[['Scenario','Color','Transport','Drink','Task Time(in seconds)'],['S1','','','',''],['S2','','','',''],['S3','','','',''],['S4','','','','']]

tk.Button(f13,font=("Georgia", 15),text='Quit',command=lambda:quit_window()).grid(row=6,column=2)
		
raise_frame(f14)
root.mainloop()

