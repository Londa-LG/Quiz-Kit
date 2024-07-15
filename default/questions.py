import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass


class Multiple_Choice(ttk.Frame):
	def __init__(self,parent,question = "A multiple choice question",answer = "Option 2",options = ["Option 1","Option 2","Option 3"],total_marks = 4):
		super().__init__(parent)
		self.grade = 0
		self.options = []
		self.total_marks = total_marks
		self.question = question
		self.options_list = options
		self.value = tk.StringVar()
		self.answer = str(answer).upper()

		self.Create()
		
	def Create(self):

		# Create and display the question, options and an empty answer label

		self.question_label = ttk.Label(master = self,text = self.question)
		for option in self.options_list:
			btn = ttk.Radiobutton(master = self,text = option,value = str(option).upper(),variable = self.value,command = self.Grade)
			self.options.append(btn)
		self.columnconfigure(0, weight =1)
		self.rowconfigure(0,weight = 2)
		for index in range(len(self.options)):
			self.rowconfigure((index + 1),weight =1)
		self.answer_label = ttk.Label(master = self, text = "Correct answer: \n" + self.answer.capitalize())
		self.rowconfigure((len(self.options) + 1),weight=1)

		self.question_label.grid(row = 0, column = 0, sticky = 'ew')		
		for index in range(len(self.options)):
			self.options[index].grid(row = (index + 1),column = 0, sticky = 'ew')	
	
	def Grade(self):
		if self.value.get() == self.answer:
			self.grade = self.total_marks
		else:
			self.grade = 0

	def Get_Grade(self):
		return self.grade

	def Show_Answer(self):
		self.answer_label.grid(row = (len(self.options) + 1),column = 0, sticky = 'ew')

	def Get_Memo(self):
		memo_string = "Answer: \n" + self.answer 
		return memo_string


class Enter_Text(ttk.Frame):
	def __init__(self,parent,question ="The question",answer = "The answer",total_marks= 8):
		super().__init__(parent)
		self.grade = 0
		self.user_answer = tk.StringVar()
		self.answer = answer.upper()
		self.question = question
		self.total_marks = total_marks
		self.Create()

	def Create(self):
		# Widgets
		self.question_label = ttk.Label(master = self,text = self.question)
		self.input_widget = ttk.Entry(master = self, textvariable = self.user_answer)
		self.answer_label = ttk.Label(master = self,text = "Correct answer: \n" + self.answer.capitalize())
		# Grid
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		# Display
		self.question_label.grid(row = 0, column = 0, sticky = 'ew')
		self.input_widget.grid(row = 1, column = 0, sticky = 'ew')

	def Grade(self):	
		if self.input_widget.get().upper() == self.answer:
			self.grade = self.total_marks	

	def Get_Grade(self):
		self.Grade()
		return self.grade
		
	def Show_Answer(self):
		self.answer_label.grid(row = 2,column = 0, sticky = 'ew')

	def Get_Memo(self):
		memo_string = "Answer: \n" + self.answer 
		return memo_string


class Enter_Number(ttk.Frame):
	def __init__(self,parent,question ="What's 11 - 1?",answer =10.2,total_marks= 4):
		super().__init__(parent)
		self.grade = 0
		self.user_answer = tk.DoubleVar()
		self.answer = answer
		self.question = question
		self.total_marks = total_marks
		self.Create()

	def Create(self):
		# Widgets
		self.question_label = ttk.Label(master = self,text = self.question)
		self.input_widget = ttk.Entry(master = self, textvariable = self.user_answer)
		self.answer_label = ttk.Label(master = self,text = "Correct answer: \n" + str(self.answer))
		# Grid
		self.columnconfigure(0, weight = 1)
		self.rowconfigure(0, weight = 1)
		self.rowconfigure(1, weight = 1)
		self.rowconfigure(2, weight = 1)
		# Display
		self.question_label.grid(row = 0, column = 0, sticky = 'ew')
		self.input_widget.grid(row = 1, column = 0, sticky = 'ew')

	def Grade(self):	
		if float(self.input_widget.get()) == self.answer:
			self.grade = self.total_marks	

	def Get_Grade(self):
		self.Grade()
		return self.grade
		
	def Show_Answer(self):
		self.answer_label.grid(row = 2,column = 0, sticky = 'ew')

	def Get_Memo(self):
		memo_string = "Answer: \n" + str(self.answer) 
		return memo_string




class Match_Columns(ttk.Frame):
	def __init__(self,parent,question="Match the columns",column_1 = ["1.","2.","3."],column_2 = ["value 2","value 1","value 3"],answer ={"1":"value 1","2":"value 2","3":"value 3",}):
		super().__init__(parent)
		self.column_1 = column_1
		self.column_2 = column_2
		self.labels = []
		self.comboboxs = []
		self.answer = answer
		self.question = question
		self.grade = 0
		self.Create()

	def Create(self):
		# Widgets
		answerString ="Answer:\n"
		self.question_label = ttk.Label(master = self, text = self.question)
		for index in range(len(self.column_1)):
			newLabel = ttk.Label(master = self,text=self.column_1[index])
			self.labels.append(newLabel)
			newCombobox = ttk.Combobox(self)
			newCombobox.configure(values = self.column_2)
			self.comboboxs.append(newCombobox)
			answerString = answerString + f"{index + 1}. " + self.answer[f"{(index + 1)}"] + "\n" 
		# Grid
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		self.rowconfigure(0,weight = 1)
		for index in range(len(self.column_2)):
			self.rowconfigure((index + 1),weight = 1)
		self.rowconfigure((len(self.column_1) + 1),weight=1)
		self.answer_label = ttk.Label(master = self,text = answerString)
		# Display
		self.question_label.grid(row = 0, column = 0, sticky = "ew")
		for index in range(len(self.column_1)):
			self.labels[index].grid(row = (index + 1), column = 0, sticky = "w")
			self.comboboxs[index].grid(row = (index + 1),column = 1, sticky = "ew")

	def Grade(self):
		for index in range(len(self.comboboxs)):
			if self.comboboxs[index].get() == self.answer[f"{index + 1}"]:
				self.grade += 1

	def Get_Grade(self):
		self.Grade()
		return self.grade
	
	def Show_Answer(self):
		self.answer_label.grid(row = (len(self.column_1) + 1),column = 0, sticky = 'ew')


@dataclass
class Question_Paper():
		title: str
		description: str
		subject: str
		grade: int
		total: int

class Test(ttk.Frame):

	# The class that handles the testing process

	def __init__(self,parent,questions,paper):
		super().__init__(parent)
		self.questions = {}
		self.nav_btns = []
		self.properties = Question_Paper(title =paper[0],description =paper[1],subject =paper[0],grade =paper[3],total = paper[4])
		self.question_index = 1
		self.rowconfigure(index = (0,1,2,3,4,5,6,7,8,9,10,11), weight = 1)
		self.columnconfigure(index = (0,1,2,3,4,5,6,7,8,9,10,11), weight = 1)
		self.next_btn = ttk.Button(master = self, text = "Next", command = self.Load_Next_Question)	
		self.prev_btn = ttk.Button(master = self,text = "Previous", command = self.Load_Previous_Question)	
		self.submit_btn = ttk.Button(master = self, text = "Submit Test", command = self.Submit_Test)	
	
		self.Create_Questions(questions)
		self.Start_Test()

		self.pack(expand = True,fill = "both",padx=10)

	def Create_Questions(self,questions):

		# MCO: matching column question
		# MCH: multiple choice question 
		# ET: Enter text question
		# EN: Enter a number question

		for index in range(len(questions)):
			if questions[index]["type"] == "MCO":
				self.questions[(index + 1)] = Match_Columns(self,question = f"Questions {index + 1}\n\n" + questions[index]["question"],column_1 = questions[index]["column 1"],column_2 = questions[index]["column 2"],answer = questions[index]["answer"])
			elif questions[index]["type"] == "MCH":
				self.questions[(index + 1)] = Multiple_Choice(self,question = f"Questions {index + 1}\n\n" + questions[index]["question"],answer = questions[index]["answer"],options = questions[index]["options"],total_marks = questions[index]["marks"])
			elif questions[index]["type"] == "ET":
				self.questions[(index +1 )] = Enter_Text(self, question = f"Questions {index + 1}\n\n" + questions[index]["question"],answer = questions[index]["answer"],total_marks = questions[index]["marks"])
			elif questions[index]["type"] == "EN":
				self.questions[(index + 1)] = Enter_Number(self, question = f"Questions {index + 1}\n\n" + questions[index]["question"], answer = questions[index]["answer"],total_marks = questions[index]["marks"])
	
		
	def Start_Test(self):
		self.questions[self.question_index].grid(row = 1,column = 1, rowspan = 8, columnspan = 7, sticky = "nesw")
		self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")

	def Display_Question(self,caller):
		if caller == 'N':
			self.questions[self.question_index].grid(row = 1,column = 1, rowspan = 8, columnspan = 7, sticky = "nesw") 
			if self.question_index > 1:
				self.prev_btn.grid(row = 10, column = 1, columnspan = 3, sticky = "nesw")

			if self.question_index == len(self.questions):
				self.next_btn.grid_forget()
				self.submit_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
			else:
				self.submit_btn.grid_forget()
				self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
		elif caller == 'P':
			self.questions[self.question_index].grid(row = 1,column = 1, rowspan = 8, columnspan = 7, sticky = "nesw")
			if self.question_index > 1:
				self.prev_btn.grid(row = 10, column = 1, columnspan = 3, sticky = "nesw")
			else:
				self.prev_btn.grid_forget()
			self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
			if self.question_index == len(self.questions):
				self.next_btn.grid_forget()
				self.submit_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
			else:
				self.submit_btn.grid_forget()
				self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
		else:
			self.questions[self.question_index].grid(row = 1,column = 1, rowspan = 8, columnspan = 7, sticky = "nesw")
			if self.question_index > 1:
				self.prev_btn.grid(row = 10, column = 1, columnspan = 3, sticky = "nesw")
			else:
				self.prev_btn.grid_forget()
			self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
			if self.question_index == len(self.questions):
				self.next_btn.grid_forget()
				self.submit_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")
			else:
				self.submit_btn.grid_forget()
				self.next_btn.grid(row = 10, column = 5, columnspan = 3, sticky = "nesw")

	def Load_Next_Question(self):
		if self.question_index < len(self.questions):
			self.questions[self.question_index].grid_forget()
			self.question_index += 1
			self.Display_Question('N')

	def Load_Previous_Question(self):
		if self.question_index > 1:
			self.questions[self.question_index].grid_forget()
			self.question_index -= 1
			self.Display_Question('P')

	def Load_Specific(self,index):
		self.questions[self.question_index].grid_forget()
		self.question_index = index 
		self.Display_Question()

	def Show_Answers(self):
		for index in range(len(self.questions)):
			self.questions[(index +1)].Show_Answer()

	def Get_Question_Index(self):
		return self.question_index

	def Submit_Test(self):
		if self.properties.grade == 0:
			total = 0
			for index in range(len(self.questions)):
				grade = self.questions[(index + 1)].Get_Grade()
				total += grade
			self.properties.grade = total
			self.Display_Results()
			
	def Display_Results(self):
		pass

	def Display_Cover_Page(self):
		pass
