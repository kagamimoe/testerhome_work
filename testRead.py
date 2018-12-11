__author__ = 'kagami'

import os

items = ['item1', 'item2','item3']

class TestDemo(object):


	def fun(self, a, b, _):
		return a, b, _

	def fun1(self):
		for i in range(len(items)):
			print (str(i+1) + ':' + items[i])

	def fun2(self):
		for i, item in enumerate(items):
			print (i, ':', item)

	def get(self, list, index):
		'''
		解析数据后提取数据的index段落
		:param list: index:int
		:return: str
		'''
		for i in range(len(list)):
			if i == index:
				l = list[i]
				s = ""
				num = 0
				for j in range(len(l)):
					if isinstance(l[j], str):
						s+=str(ord(l[j]))
					elif not isinstance(l[j],str):
						num+=int(l[j])
				if num == 0:
					return s
				else:
					return num

	def read_txt(self, path):
		'''
		:param path:
		:return:
		'''
		with open(dir+'/config/'+path,encoding="utf-8") as fd:
			return fd.read()

	# TODO 读写txt文本的其他方法mode:w,rb,a+
	def write_txt(self, path, str):
		'''
		w模式写文件，只可以写，会覆盖文件
		:param path:
		:return:
		'''
		with open(dir+'/config/'+path,mode='w',encoding="utf-8") as fd:
			fd.write(str)

	def write_txt_append(self, path, str):
		'''
		a+模式写文件，不会覆盖文件会追加写在最后面
		:param path:
		:param str:
		:return:
		'''
		with open(dir+'/config/'+path,mode='a+',encoding="utf-8") as fd:
			fd.write(str)

	def read_bianary_file(self, path):
		'''
		rb模式读取二进制文件
		:param path:
		:return:
		'''
		with open(dir+'/config/'+path, mode='rb') as fd:
			return fd.read()

t = TestDemo()
print(t.fun(1,2,3))

data = [[1, 2, 3],['x', 'y', 'z'], ['a', 'b', 'c'], "a", "b"]
print(t.get(data,1))

dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print (os.path.abspath(os.path.join(os.getcwd(), "..")))
print (dir)


print(t.read_txt("1.txt"))
t.write_txt("1.txt", "haha红烧豆腐\n水电费")
print(t.read_txt("1.txt"))
t.write_txt_append("1.txt", "我是追加的一行文字")
print(t.read_txt("1.txt"))
print(t.read_bianary_file("1.txt"))