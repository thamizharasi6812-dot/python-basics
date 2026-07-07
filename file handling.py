# file handling is to read any type of in python way
# write
file=open('action_series.txt','w')
file.write('high & low:''thai series\n')
file.write('high school frenemy:''thai series\n')
file.write('weak hero class:''korean series')
print('file created')
file.close()

# read
file=open('action_series.txt','r')
file.read()
file.close()

# append
file=open('action_series.txt','a')
file.write('\nstudy group:''korean series')
file.close()

# create
file=open('series.txt','x')
file.write('    series list    \n')
file.write('last twilight\n')
file.write('ticket to heaven\n')
file.write('perfect 10 liners')
file.close()

# write and read
file=open('series.txt','w+')
file.write('\nbad buddy')
file.read()
file.close()

# read and write
file=open('series.txt','r+')
file.read()
file.write('\nwe are')
file.close()

file=open('C:/Users/poojh/Python-thamizh/text.jpg','rb')
text=file.read()
file.close()
print(text)

file=open('C:/Users/poojh/Python-thamizh/text1.jpg','wb')
file.write(text)
file.close()
print(text)
