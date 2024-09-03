# Directory -> Folder
'''
import os
current_dir = os.getcwd()
# print(current_dir)

# os.chdir('../New Folder')
current_dir = os.getcwd()
# print(current_dir)
files = os.listdir('./')
# print(files)
os.mkdir('new_directory')
files = os.listdir('./')
print(files)'''

'''
 r - Read
 w - Write
 a - Append
 r+ - Read and Write

 read()
 readline()
 readlines()
'''
'''
file = open('content.txt', 'r')
# content = file.read()
# content = file.readline()
content = file.readlines()
print(content)
file.close()
'''
'''
file = open('content.txt', 'w')
file.write('Content by Write Mode')
file.close()
'''
'''
file = open('content.txt', 'a')
file.write('\nThis is an additional line.')
file = open('content.txt', 'r')
print(file.readlines())
file.close()
'''

# file = open('content.txt', 'r+')
# print(file.read())
# file.write('\nContent from Read and Write')
# # print("After Write Operation: ", file.readlines())
# print(file.readlines())
# file.close()

'''
import os
os.remove('./new_directory/content.txt')

if os.path.exists('./new_directory/content.txt'):
    print("content.txt exists")
else:
    print("content.txt does not exists")
'''

file = open('content1.txt', 'r')
content1 = file.readlines()
print(content1)
file = open('content2.txt', 'a')
for c in content1:
    file.write(c)