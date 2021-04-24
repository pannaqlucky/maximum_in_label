from PIL import Image
import os
import pandas as pd 
import csv
from tqdm import trange

Image.MAX_IMAGE_PIXELS = 100000000000000
'''
def mesh(x,y,a):
	for i in range(30):
		for j in range(30):
		 max_value=max(true_label)
		 label=true_label.index(max_value)
		 r, g, b = rgb_im.getpixel((x+i, y+i))
		 if  r==0 and g==0 and b==255 :
		  true_label[0]=true_label[0]+1
		 elif r==150 and g==50 and b==20 :
		  true_label[1]=true_label[1]+1
		 elif r==255 and g==255 and b==0 :
		  true_label[2]=true_label[2]+1
		 elif r==0 and g==200 and b==255 :
		  true_label[3]=true_label[3]+1
		 elif r==255 and g==0 and b==0 :
		  true_label[4]=true_label[4]+1
		 elif r==20 and g==150 and b==150 :
		  true_label[5]=true_label[5]+1
		 elif r==0 and g==0 and b==0 :
		  true_label[6]=true_label[6]+1
		 elif r==255 and g==255 and b==255 :
		  true_label[7]=true_label[7]+1
	print(x, y, label, file=a)


true_folder = "./true_label"

imlist = os.listdir(true_folder)
imlist.sort()

true_label=[0, 0, 0, 0, 0, 0, 0, 0]

a = open("0.3m_label.csv", 'w+')

for imagename in imlist:
	imurl = os.path.join(true_folder,imagename)
	print(imurl)
	im = Image.open(imurl)
	rgb_im = im.convert('RGB')
	for x in trange(0,14470,30):
		for y in range(0,13970,30):
			mesh(x,y,a)
			true_label=[0, 0, 0, 0, 0, 0, 0, 0]
'''

c = open("202010_0.99m_label.csv", 'w+')
true_folder = "./true_label"

imlist = os.listdir(true_folder)
imlist.sort()

true_label=[0, 0, 0, 0, 0, 0, 0, 0]

for imagename in imlist:
	imurl = os.path.join(true_folder,imagename)
	print(imurl)
	im = Image.open(imurl)
	rgb_im = im.convert('RGB')
for x in trange(0,50080,33):
	for y in range(0,22298,33):
		for a in range(10):
			for h in range(10):
#			 print(x+a, y+h, true_label, file=c)
			 max_value=max(true_label)
			 label = true_label.index(max_value)
			 r, g, b = rgb_im.getpixel((x+a, y+h))
			 if  r==0 and g==0 and b==255 :
			  true_label[0]=true_label[0]+1
			 if r==150 and g==50 and b==20 :
			  true_label[1]=true_label[1]+1
			 if r==255 and g==255 and b==0 :
			  true_label[2]=true_label[2]+1
			 if r==0 and g==200 and b==255 :
			  true_label[3]=true_label[3]+1
			 if r==255 and g==0 and b==0 :
			  true_label[4]=true_label[4]+1
			 if r==20 and g==150 and b==150 :
			  true_label[5]=true_label[5]+1
			 if r==0 and g==0 and b==0 :
			  true_label[6]=true_label[6]+1
#			 elif r==255 and g==255 and b==255 :
#			  true_label[5]=true_label[5]+1
			 elif true_label[0] ==0 and true_label[1] ==0 and true_label[2] ==0 and true_label[3] ==0 and true_label[4] ==0 and true_label[5] ==0:
			  true_label[7]=true_label[7]+1
#			 elif true_label[0] >0 or true_label[1] >0 or true_label[2] >0 or true_label[3] >0 or true_label[4] >0 :
#			  true_label[5]=0
		print(-34842.503368065358+0.99*x/33, -142342.71785129176-0.99*y/33, label, file=c)
		true_label=[0, 0, 0, 0, 0, 0, 0, 0]

with open('202010_0.99m_label.csv',newline='') as c:
	 r = csv.reader(c)
	 data = [line for line in r]
with open('202010_0.99m_label.csv','w',newline='') as c:
	 w = csv.writer(c)
	 w.writerow(['x','y','true_label'])
	 w.writerows(data)
print('完成')
