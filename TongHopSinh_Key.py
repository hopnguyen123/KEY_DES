def ShiftLeft_1(LIST):
    len_ = len(LIST)
    l_=LIST[0]
    for i in range(len_-1):
        LIST[i]=LIST[i+1]
    LIST[len_-1]=l_

def ShiftLeft_2(LIST):
    len_ = len(LIST)
    l0=LIST[0]
    l1=LIST[1]
    for i in range(len_-2):
        LIST[i]=LIST[i+2]
    LIST[len_-1]=l1
    LIST[len_-2]=l0

list_index_Permuted2=[13,16,10,23,0,4,2,27,
                      14,5,20,9,22,18,11,3,
                      25,7,15,6,26,19,12,1,
                      40,51,30,36,46,54,29,39,
                      50,44,32,47,43,48,38,55,
                      33,52,45,41,49,35,28,31]


LIST_SUBKEY=[]
LIST_SHIFTLEFT=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
ROUND=1

#Nhập Key đầu vào 64bit, hệ HEX(16)
key = input()
key_binary=""

#Chuyển Key HEX -> BINARY
for i in key:
	if i == 'A' or i =='a':
		key_binary+="1010"
	elif i == 'B' or i =='b':
		key_binary+="1011"
	elif i == 'C' or i =='c':
		key_binary+="1100"
	elif i == 'D' or i =='d':
		key_binary+="1101"
	elif i == 'E' or i =='e':
		key_binary+="1110"
	elif i == 'F' or i =='f':
		key_binary+="1111"
	else:
		key_binary += bin(ord(i))[4:]

#Chuyển từ String -> List
List_key_binary= list(key_binary)

#Hoán Vị Key
list_key_Permuted1=[]
list_Index_permuted1=[56,48,40,32,24,16,8,
				    0,57,49,41,33,25,17,
				    9,1,58,50,42,34,26,
				    18,10,2,59,51,43,35,
				    62,54,46,38,30,22,14,
				    6,61,53,45,37,29,21,
				    13,5,60,52,44,36,28,
				    20,12,4,27,19,11,3]
ROUND=1
for i in list_Index_permuted1:
	list_key_Permuted1.append(List_key_binary[i])

list_key_left=[]
list_key_left=list_key_Permuted1[:28]
list_key_right=[]
list_key_right=list_key_Permuted1[28:]

if ROUND==1 or ROUND==2 or ROUND==9 or ROUND ==16:
	ShiftLeft_1(list_key_left)
	ShiftLeft_1(list_key_right)
else:
	ShiftLeft_2(list_key_left)
	ShiftLeft_2(list_key_right)

list_p2=[]
for i in list_key_left:
	list_p2.append(i)
for i in list_key_right:
	list_p2.append(i)

list_key_permuted2=[]
for i in list_index_Permuted2:
    list_key_permuted2.append(list_p2[i])

LIST_SUBKEY.append(list_key_permuted2)
# print(list_key_permuted2)
# a = ''.join((list_key_permuted2))
# print(a)
ROUND = ROUND +1
#============================================================
while ROUND <=16:
	# list_key_left = list_key_permuted2[:28]
	# list_key_right = list_key_permuted2[28:]

	if ROUND == 1 or ROUND == 2 or ROUND == 9 or ROUND == 16:
		ShiftLeft_1(list_key_left)
		ShiftLeft_1(list_key_right)
	else:
		ShiftLeft_2(list_key_left)
		ShiftLeft_2(list_key_right)

	list_p2 = []
	for i in list_key_left:
		list_p2.append(i)
	for i in list_key_right:
		list_p2.append(i)

	list_key_permuted2 = []
	for i in list_index_Permuted2:
		list_key_permuted2.append(list_p2[i])

	LIST_SUBKEY.append(list_key_permuted2)

	ROUND = ROUND + 1

for i in LIST_SUBKEY:
	a=''.join(i)
	print(a)

