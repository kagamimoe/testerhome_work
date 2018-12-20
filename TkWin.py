import tkinter,os
from selenium import webdriver

class TkWin():
	def __init__(self,title = 'title',size = '200x200',url = ''):
		self.title = title
		self.size = size
		self.url = url
		root = tkinter.Tk()
		root.title(self.title)
		root.geometry(self.size)
		lb1_source = tkinter.Label(root,text = 'url')
		lb1_source.grid(row=0,column=0)
		global entry_source
		entry_source = tkinter.Entry(root)
		entry_source.grid(row=0,column=1)
		but_back = tkinter.Button(root,text='open')
		but_back.grid(row=3,column=0)
		but_back['command'] = self.open_url
		root.mainloop()

	def open_url(self):
		self.url = entry_source.get()
		dr = webdriver.Chrome()
		dr.get(self.url)



title = 'IE'
size = '800x600'
w = TkWin(title, size)

