counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
 
print (counter)
print (miles)
print (name)

a=20
b=20
if a is b:
    print ('good')
else:
    print('no')

count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1
 
print ("Good bye!")

for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前水果 :', fruit)
 
print ("Good bye!")

#rows = int(input('输入列数： '))
rows=5
print(rows)


i=j=k=1
for i in range(0,rows):
    for j in range(0,rows-i):
        print ("*"*j),
        j=j+1
    i=i+1
    print('\n')    

print('****'*2)

def ChangeInt( b ):
    b= 10
 
b = 2
ChangeInt(b)
print (b) # 结果是 2

def run ():
    print("first var")

run()

class student:
    age =18
    def page(self):
        print(self.age)


def run(a):
    print(a)
    print(a)

run('**************************')


a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

flag =True;
print(not flag);

a=0
b=1

def fb(c):
    sum=1
    bef=1
    for a in range(c):
        p=sum
        sum=p+bef
        bef=p

    return sum

for c in range(10):

    print(fb(c))


def add(a=0, b=0, c=0):
    return a + b + c



# 如果没有指定参数那么使用默认值摇两颗色子

# 摇三颗色子
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))

def foo():
    print('hello, world!')


def foo():
    print('goodbye, world!')


# 下面的代码会输出什么呢？
foo()

def foo():
    b = 'hello'

    def bar():  # Python中可以在函数内部再定义函数
        c = True
        print(a)
        print(b)
        print(c)

    bar()
    # print(c)  # NameError: name 'c' is not defined


if __name__ == '__main__':
    a = 100
    # print(b)  # NameError: name 'b' is not defined
    foo()


import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


import json
def main():
    #file_path = '{0}/{1}.{2}'.format(os.getcwd(),'1','jpg')
    #print(file_path)
    
    data = '{"msg_name": "action", "msg_data": {"round_id": 2, "action": [{"player_id": 0, "move": ["up"], "team": 1}]}}'
    data = '{"msg_name":"leg_start","b":2}'
    data = 'abcdefg'
    data = data[5:]
    print (data)
    
   
if __name__ == '__main__':
    main()