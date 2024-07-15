import customtkinter as ctk
from dataclasses import dataclass


class Multiple_Choice(ctk.CTkFrame):
	def __init__(self,parent,question,answer,options,total_marks,style,frame_style):
		super().__init__(parent)
		self.grade = 0
		self.options = []
		# style order (label,radio button)
		self.style = style
		self.font = ctk.CTkFont(
			family = style[0].font[0],
			size = style[0].font[1],
			weight = style[0].font[2],
			slant = style[0].font[3],
			underline = style[0].font[4],
			overstrike = style[0].font[5]
		)
		self.question = question
		self.value = ctk.StringVar()
		self.options_list = options
		self.total_marks = total_marks
		self.answer = str(answer).upper()
		self.configure(fg_color = frame_style)

		self.Create()
		
	def Create(self):

		# Create and display the question, options and an empty answer label

		self.question_label = ctk.CTkLabel(
			master = self,
			text = self.question,
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)

		for option in self.options_list:
			btn = ctk.CTkRadioButton(
				master = self,
				text = option,
				value = str(option).upper(),
				variable = self.value,
				command = self.Grade,
				corner_radius = self.style[1].corner_radius,
				fg_color = self.style[1].fg_color,
				hover_color = self.style[1].hover_color,
				text_color = self.style[1].text_color,
				hover = self.style[1].hover
			)
			self.options.append(btn)
		self.columnconfigure(0, weight =1)
		self.rowconfigure(0,weight = 2)
		for index in range(len(self.options)):
			self.rowconfigure((index + 1),weight =1)
		self.answer_label = ctk.CTkLabel(
			master = self,
			text = "Correct answer: \n" + self.answer.capitalize(),
			corner_radius = self.style[1].corner_radius,
			fg_color = self.style[1].fg_color,
			text_color = self.style[1].text_color,
		)
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


class Enter_Text(ctk.CTkFrame):
	def __init__(self,parent,question,answer,total_marks,style,frame_style):
		# (Label,Entry)
		super().__init__(parent)
		self.style = style
		self.font = ctk.CTkFont(
			family = style[0].font[0],
			size = style[0].font[1],
			weight = style[0].font[2],
			slant = style[0].font[3],
			underline = style[0].font[4],
			overstrike = style[0].font[5]
		)
		self.grade = 0
		self.user_answer = ctk.StringVar()
		self.answer = answer.upper()
		self.question = question
		self.total_marks = total_marks
		self.configure(fg_color = frame_style)
		self.Create()

	def Create(self):
		# Widgets
		self.question_label = ctk.CTkLabel(
			master = self,
			text = self.question,
			corner_radius = self.style[0].corner_radius,	
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)
		self.input_widget = ctk.CTkEntry(
			master = self,
			textvariable = self.user_answer,
			corner_radius =  self.style[1].corner_radius,
			fg_color = self.style[1].fg_color,
			text_color = self.style[1].text_color,
			placeholder_text_color = self.style[1].placeholder_text_color
		)
		self.answer_label = ctk.CTkLabel(
			master = self,
			text = "Correct answer: \n" + self.answer.capitalize(),
			corner_radius = self.style[0].corner_radius,	
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)
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


class Enter_Number(ctk.CTkFrame):
	def __init__(self,parent,question,answer,total_marks,style,frame_style):
		super().__init__(parent)
		self.style = style
		self.font = ctk.CTkFont(
			family = style[0].font[0],
			size = style[0].font[1],
			weight = style[0].font[2],
			slant = style[0].font[3],
			underline = style[0].font[4],
			overstrike = style[0].font[5]
		)
		self.grade = 0
		self.user_answer = ctk.DoubleVar()
		self.answer = answer
		self.question = question
		self.total_marks = total_marks
		self.configure(fg_color = frame_style)
		self.Create()

	def Create(self):
		self.question_label = ctk.CTkLabel(
			master = self,
			text = self.question,
			corner_radius = self.style[0].corner_radius,	
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)
		self.input_widget = ctk.CTkEntry(
			master = self, 
			textvariable = self.user_answer,
			corner_radius =  self.style[1].corner_radius,
			fg_color = self.style[1].fg_color,
			text_color = self.style[1].text_color,
			placeholder_text_color = self.style[1].placeholder_text_color
		)
		self.answer_label = ctk.CTkLabel(
			master = self,
			text = "Correct answer: \n" + str(self.answer),
			corner_radius = self.style[0].corner_radius,	
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)
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




class Match_Columns(ctk.CTkFrame):
	def __init__(self,parent,question,column_1,column_2,answer,style,frame_style):
		super().__init__(parent)
		# (Label,Combobox)
		self.style = style
		self.font = ctk.CTkFont(
			family = style[0].font[0],
			size = style[0].font[1],
			weight = style[0].font[2],
			slant = style[0].font[3],
			underline = style[0].font[4],
			overstrike = style[0].font[5]
		)
		self.column_1 = column_1
		self.column_2 = column_2
		self.labels = []
		self.comboboxs = []
		self.answer = answer
		self.question = question
		self.grade = 0
		self.configure(fg_color = frame_style)
		self.Create()

	def Create(self):
		# Widgets
		answerString ="Answer:\n"
		self.question_label = ctk.CTkLabel(
			master = self, 
			text = self.question,
			corner_radius = self.style[0].corner_radius,	
			fg_color = self.style[0].fg_color,
			text_color = self.style[0].text_color,
			font = self.font
		)
		for index in range(len(self.column_1)):
			newLabel = ctk.CTkLabel(
				master = self,
				text=self.column_1[index],
				corner_radius = self.style[0].corner_radius,	
				fg_color = self.style[0].fg_color,
				text_color = self.style[0].text_color,
				font = self.font
			)
			self.labels.append(newLabel)
			newCombobox = ctk.CTkComboBox(
				master =self,
				values = self.column_2,
				corner_radius = self.style[1].corner_radius,
				fg_color = self.style[1].fg_color,
				border_color = self.style[1].border_color,
				button_color = self.style[1].button_color,
				button_hover_color = self.style[1].button_hover_color,
				dropdown_fg_color = self.style[1].dropdown_fg_color,
				dropdown_hover_color = self.style[1].dropdown_hover_color,
				dropdown_text_color = self.style[1].dropdown_text_color,
				text_color = self.style[1].text_color,
				text_color_disabled = self.style[1].text_color_disabled 
			)
			self.comboboxs.append(newCombobox)
			answerString = answerString + f"{index + 1}. " + self.answer[f"{(index + 1)}"] + "\n" 
		# Grid
		self.columnconfigure(0, weight = 1)
		self.columnconfigure(1, weight = 1)
		self.rowconfigure(0,weight = 1)
		for index in range(len(self.column_2)):
			self.rowconfigure((index + 1),weight = 1)
		self.rowconfigure((len(self.column_1) + 1),weight=1)
		self.answer_label = ctk.CTkLabel(master = self,text = answerString,font = self.font)
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

class Test(ctk.CTkFrame):

	# The class that handles the testing process

	def __init__(self,parent,questions,paper,style,frame_style):
		super().__init__(parent)
		# (Navbtn,Multiple,Match,EnterText,EnterNumber)
		self.style = style
		self.questions = {}
		self.nav_btns = []
		self.properties = Question_Paper(title =paper[0],description =paper[1],subject =paper[0],grade =paper[3],total = paper[4])
		self.question_index = 1
		self.rowconfigure(index = (0,1,2,3,4,5,6,7,8,9,10,11), weight = 1)
		self.columnconfigure(index = (0,1,2,3,4,5,6,7,8), weight = 1)
		self.frame_style = frame_style
		self.configure(fg_color = frame_style)
		self.next_btn = ctk.CTkButton(
			master = self,
			text = "Next",
			command = self.Load_Next_Question,
			corner_radius = self.style[0].corner_radius,
			fg_color = self.style[0].fg_color,
			hover_color = self.style[0].hover_color,
			border_color = self.style[0].border_color, 
			text_color = self.style[0].text_color,
			text_color_disabled = self.style[0].text_color,
		)	
		self.prev_btn = ctk.CTkButton(
			master = self,
			text = "Previous",
			command = self.Load_Previous_Question,
			corner_radius = self.style[0].corner_radius,
			fg_color = self.style[0].fg_color,
			hover_color = self.style[0].hover_color,
			border_color = self.style[0].border_color, 
			text_color = self.style[0].text_color,
			text_color_disabled = self.style[0].text_color,
		)	
		self.submit_btn = ctk.CTkButton(
			master = self,
			text = "Submit Test",
			command = self.Submit_Test,
			corner_radius = self.style[0].corner_radius,
			fg_color = self.style[0].fg_color,
			hover_color = self.style[0].hover_color,
			border_color = self.style[0].border_color, 
			text_color = self.style[0].text_color,
			text_color_disabled = self.style[0].text_color,
		)	

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
				self.questions[(index + 1)] = Match_Columns(
					self,
					question = f"Questions {index + 1}\n\n" + questions[index]["question"],
					column_1 = questions[index]["column 1"],
					column_2 = questions[index]["column 2"],
					answer = questions[index]["answer"],
					style = self.style[2],
					frame_style = self.frame_style
				)
			elif questions[index]["type"] == "MCH":
				self.questions[(index + 1)] = Multiple_Choice(
					self,
					question = f"Questions {index + 1}\n\n" + questions[index]["question"],
					answer = questions[index]["answer"],
					options = questions[index]["options"],
					total_marks = questions[index]["marks"],
					style = self.style[1],
					frame_style=self.frame_style
				)
			elif questions[index]["type"] == "ET":
				self.questions[(index +1 )] = Enter_Text(
					self,
					question = f"Questions {index + 1}\n\n" + questions[index]["question"],
					answer = questions[index]["answer"],
					total_marks = questions[index]["marks"],
					style = self.style[3],
					frame_style=self.frame_style
				)
			elif questions[index]["type"] == "EN":
				self.questions[(index + 1)] = Enter_Number(
					self,
					question = f"Questions {index + 1}\n\n" + questions[index]["question"],
					answer = questions[index]["answer"],
					total_marks = questions[index]["marks"],
					style = self.style[4],
					frame_style=self.frame_style
				)
	
		
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

