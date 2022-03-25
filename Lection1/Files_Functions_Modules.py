# Work with files
# a - open for adding data
# r - open for reading data
# w - open for writing data
# w+, r+
#######Examples#######
###########1########## WRITING №1

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.write('\nLINE 12\n')
# data.write('LINE 13')
# data.close()

###########2########## WRITING №2

# with open('file.txt', 'w') as data:
#     data.write('line1\n')
#     data.write('line2\n')

###########3########## READING

path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()