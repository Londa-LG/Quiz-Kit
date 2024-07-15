import tkinter as tk
from default.questions import Test

class App(tk.Tk):

	def __init__(self):
		super().__init__()
		self.title = "Questions"
		self.geometry("800x400")
		self.questions = [
			{"type":"MCO","question":"A match columns question","column 1": ["1","2","3"],"column 2":["World","Hello","Python"],"answer":{"1":"Hello","2":"World","3":"Python"}},
			{"type":"MCH","question":"A multiple choice question","answer":"option 2","options":["option 1","option 2","option 3"],"marks": 4},
			{"type":"ET","question":"A enter text question","answer":"Y2K","marks": 6},
			{"type":"EN","question":"A enter number question","answer": 3.52,"marks": 8}
		]
	
		self.paper = ("Formative 1","A little something about this paper","Mathematics",0,21)
	
		test = Test(self,self.questions,self.paper)
		
		self.mainloop()

App()
