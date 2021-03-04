from PIL import Image
import sys

args = sys.argv

def encode(image,arr,output,c):

	img = Image.open(image)
	data = img.load()
	if int(c) not in [0,1,2]:
		if c == r:
			c = 0
		elif c == g:
			c = 1
		elif c == b:
			c = 2
	c = int(c)
	try:
		arr = bin(int(arr))[2:]
	except ValueError:
		x = ""
		for ele in list(arr):
			x+="110010111100111110000110000111000111100101"
			x+=str(bin(ord(ele))[2:])
			x+="110010111100111110000110000111000111100101"

			
		arr = x
	arr = str(((img.width*img.height)-len(arr))*"0"+arr)
	x = 0
	for i in range(img.width):
		for j in range(img.height):
			val = str("0b"+(8-len(bin(data[i,j][c])[2:]))*"0"+bin(data[i,j][c])[2:])
			val = val[:9] + arr[x]
			data[i,j] = (int(val,2),data[i,j][1],data[i,j][2])
			x+=1
	print("LSB image saved as",output)
	img.save(output)


def decode(image,c):

	img = Image.open(image)
	data = img.load()
	dec = []

	if int(c) not in [0,1,2]:
		if c == r:
			c = 0
		elif c == g:
			c = 1
		elif c == b:
			c = 2
	c = int(c)

	for i in range(img.width):
		for j in range(img.height):
			val = (8-len(bin(data[i,j][c])))*"0"+bin(data[i,j][c])[2:]
			dec.append(str(val)[len(val)-1])
	for ele in "".join(dec).split("110010111100111110000110000111000111100101")[1:]:
		if ele != "":
			print(chr(int("0b"+ele,2)),end="")
	print("")


if "-h" in args:
	print("-d : decode\n-e : encode\n\n Encoding : input file (.png) ; message to encrypt ; output file name ; channel (r,g,b)\n Decoding : input file (.png) ; channel (r,g,b)")
	exit()
if "-d" not in args and "-e" not in args and "-h" not in args:
	print("les arguments lmao 1")
	exit()
if "-e" in args:
	if len(args) != 6:
		print("les arguments lmao 2")
		exit()
	if args[3] == "inp":
		args[3] = input()
	encode(args[2],args[3],args[4],args[5])
if args[1] == "-d":
	if len(args) != 4:
		print("les arguments lmao")
		exit()
	decode(args[2],args[3])

