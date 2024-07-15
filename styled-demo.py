import customtkinter as ctk
from Styled.styled_questions import Test
from Styled.customizers import (
	Cust_Label,
	Cust_Entry,
	Cust_Button,
	Cust_Combobox,
	Cust_Radiobutton,
)

class App(ctk.CTk):

	def __init__(self):

		# Window
		super().__init__(fg_color = ("white","#22252a"))
		self.title = "Questions"
		self.geometry("600x400")

		# Questions
		self.questions = [
			{
				"type":"MCH",
				"question":"A multiple choice question",
				"answer":"option 2",
				"options":["option 1","option 2","option 3"],
				"marks": 4
			},
			{
				"type":"ET",
				"question":"A enter text question",
				"answer":"Y2K",
				"marks": 6
			},
			{
				"type":"EN",
				"question":"A enter number question",
				"answer": 3.52,
				"marks": 8
			},
			{
				"type":"MCO",
				"question":"A match columns question",
				"column 1": ["1._World","2.Hello_","3.This is writen in _"],
				"column 2":["World","Hello","Python"],
				"answer":{"1":"Hello","2":"World","3":"Python"}
			}
		]
	
		# Define Paper
		self.paper = (
			"Formative 1",
			"A little something about this paper",
			"Mathematics",
			0,
			21
		)

		# Styles
		label = Cust_Label(
			corner_radius = 5,
			fg_color = ("white","#2d3035"),
			text_color = ("#22252a","#8a8d93"),
			font = ("monoscope",18,"normal","roman",False,False)
		)
		match_colums= (
			label,
			Cust_Combobox(
				corner_radius = 5,
				fg_color = ("white","#2d3035"),
				border_color = ("grey","#8a8d93"),
				button_color = ("grey","white"),
				button_hover_color =("grey","white"),
				dropdown_fg_color = ("white","white"),
				dropdown_hover_color = ("grey","lightgrey"),
				dropdown_text_color = ("black","black"),
				text_color = ("black","#8a8d93"),
				text_color_disabled = ("grey","white")
			)	
		)
		multiple_choice = (
			label,
			Cust_Radiobutton(
				corner_radius = 5,
				fg_color = ("grey","white"),
				hover_color = ("grey","white"),
				text_color = ("black","#8a8d93"),
				hover = False
			)
		)
		entry = (
			label,
			Cust_Entry(
				corner_radius = 5,
				fg_color = ("white","white"),
				text_color = ("black","black"),
				placeholder_text_color = "grey"
			)
		)	
		button = Cust_Button(
			corner_radius = 5,
			fg_color = ("blue","blue"),
			hover_color = ("lightblue","lightblue"),
			border_color = ("blue","blue"),
			text_color = ("white","white"),
			text_color_disabled = ("grey","grey"),
		)

		frame_style = ("white","#2d3035")
	
		test = Test(
			parent = self,
			questions = self.questions,
			paper = self.paper,
			frame_style = frame_style,
			style = (
				button,
				multiple_choice,
				match_colums,
				entry,
				entry
			),
		)


		def toggle_mode():
			global modestr
			if modestr == "light":
				ctk.set_appearance_mode("dark")
				modestr = "dark"
			else:
				ctk.set_appearance_mode("light")
				modestr = "light"

		btn = ctk.CTkButton(
			master = self,
			text = "toggle mode",
			command = toggle_mode,	
		)

		
		btn.pack()

		
		global modestr 
		modestr = "light"
		self.mainloop()

App()
