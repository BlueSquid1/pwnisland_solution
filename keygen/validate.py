import struct
import math
import tkinter
import random

def rsa_encrypt(messageNum, mod, expo):
   return pow(messageNum, expo, mod)
   
def rsa_decrypt(cypro, mod, d):
   return pow(cypro, d, mod)

def hex_list_to_int_96bits(hex_list):
   # dealing with little endian
   reversedList = hex_list[::-1]
   bufferString = "0x"
   for i in range(len(reversedList)):
       bufferString += hex(reversedList[i])[2:]
   return int(bufferString, 16)

def int_96bits_to_hex_list(value):
   hex_string = hex(value)[2:]
   if len(hex_string) < 24:
       paddingNum = 24 - len(hex_string)
       hex_string = paddingNum*"0" + hex_string
   hex_list = []    
   for i in range(len(hex_string) - 1, 0, -2):
       hex_list.append(int(hex_string[i-1] + hex_string[i], 16))
   return hex_list

def generateDlcCode():
	#rsa encryption
	"""
	#sudo code
	buffer_len_15= 
	buffer_len_12 = buffer_len_15[0:12]
	buffer_len_12[11] = buffer_len_12[11] & 0x3

	buffer_len_4 = buffer_len_15[11:15]
	num = dword(buffer_len_4)
	num = num >> 2
	num = num ^ 0x2badc0de
	buffer_len_4 = num
	key_len_12 = buffer_len_4 + "PWNADV3\00"

	mod = 0x03c9921ac0185b3aaae37e1b
	expo = 0x010001
	encrypted_len_12 = rsa_encrypt(buffer_len_12, mod, expo)
	return encrypted_len_12 == key_len_12
	"""

	#messageNum = 0x02307b9ac5a928398a418820
	mod = 0x03c9921ac0185b3aaae37e1b
	expo = 0x10001
	d = 0x611c0519e05065e8f38da1
	buffer_len_15 = [0] * 15


	buffer_len_4 = [random.randint(0,0x40), random.randint(0,0x100), random.randint(0,0x100), random.randint(0,0x100)]
	buffer_len_4[0] = buffer_len_4[0] & 0x3F
	buffer_len_15[11:15] = buffer_len_4
	num = struct.unpack("<I",bytes(buffer_len_4))[0]
	num = num >> 2
	num = num ^ 0x2badc0de
	buffer_len_4 = list(struct.pack("<I", num))
	key_len_12 = buffer_len_4 + list(bytearray("PWNADV3\00", encoding="utf-8", errors="strict"))
	num1 = hex_list_to_int_96bits(key_len_12)
	input_num = rsa_decrypt(num1, mod, d)
	buffer_len_12 = int_96bits_to_hex_list(input_num)
	buffer_len_12[11] = buffer_len_12[11] & 0x3
	buffer_len_15[0:11] = buffer_len_12[0:11]
	buffer_len_15[11] = buffer_len_15[11] | buffer_len_12[11]



	#base32
	""" 
	#sudo code

	input_key_numbers_len_25 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
	buffer_len_15 = [0] * 15
	for i2 in range(24):
	   num = input_key_numbers_len_25[i2]
	   for bitNum in range(0,5):
	      mask1 = 0x1
	      mask1 = mask1 << bitNum
	      if mask1 & num != 0:
	          mask2 = 0x1
	          pos = i2*5 + bitNum
	          pos = pos % 8
	          mask2 = mask2 << pos
	          
	          pos2 = math.floor( (i2*5 + bitNum) / 8 )
	          buffer_len_15[pos2] = buffer_len_15[pos2] | mask2

	#print(buffer_len_15)        
	#print(str([hex(no) for no in buffer_len_15]))
	"""

	input_key_numbers_len_25 = [0] * 25
	buffer_byte = 0
	buffer_bit = 0
	for keyNum in range(24):
	   for keyNum_bit in range(5):
	      #select the bit
	      mask1 = 0x1
	      mask1 = mask1 << buffer_bit
	      if buffer_len_15[buffer_byte] & mask1 != 0x0:
	         #write to input_key_numbers_len_25
	         mask2 = 0x1
	         mask2 = mask2 << keyNum_bit
	         input_key_numbers_len_25[keyNum] = input_key_numbers_len_25[keyNum] | mask2   
	      buffer_bit += 1
	      if buffer_bit >= 8:
	         buffer_bit = 0
	         buffer_byte += 1


	#generate checksum
	checkSum = 0
	for keyNum in range(24):
	   checkSum += input_key_numbers_len_25[keyNum]
	   checkSum %= 256
	checkSum = checkSum & 0x1f
	input_key_numbers_len_25[24] = checkSum


	#convert to anscii
	validCharactors = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','H','J','K','L','M','N','P','Q','R','T','U','V','W','X','Y','Z']

	userInput_len_25 = [None] * 25
	for i in range(len(input_key_numbers_len_25)):
	   keyValue = input_key_numbers_len_25[i]
	   userInput_len_25[i] = validCharactors[keyValue]


	dlcCode = ''.join(userInput_len_25)
	generatedCode = dlcCode[0:5] + "-" + dlcCode[5:10] + "-" + dlcCode[10:15] + "-" + dlcCode[15:20] + "-" + dlcCode[20:25]
	w.delete(1.0, tkinter.END)
	w.insert(1.0, generatedCode)

top = tkinter.Tk()
top.geometry("1600x800")
B = tkinter.Button(top, text = "Generate", command = generateDlcCode)
B.place(x = 800,y = 400, anchor=tkinter.CENTER)
var = tkinter.StringVar()
w = tkinter.Text(top, height=1, width = 29)
w.insert(1.0, "00000-00000-00000-00000-00000")
w.place(x = 800, y = 600, anchor=tkinter.CENTER)
w.configure(bg=top.cget('bg'), relief=tkinter.FLAT)

top.mainloop()


