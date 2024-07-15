from dataclasses import dataclass


@dataclass
class Cust_Radiobutton:
	corner_radius: int
	fg_color: (str,str)
	hover_color: (str,str)
	text_color: (str,str)
	hover: bool

@dataclass
class Cust_Label:
	corner_radius: int
	fg_color: (str,str)
	text_color: (str,str)

	# family,size(in px),weight(bold/normal),slant(italic/roman),underline,overstrike
	font: (str,int,str,str,bool,bool) 

@dataclass
class Cust_Entry:
	corner_radius: int
	fg_color: (str,str)
	text_color: (str,str)
	placeholder_text_color: (str,str)

@dataclass
class Cust_Button:
	corner_radius: int
	fg_color: (str,str)
	hover_color: (str,str)
	border_color: (str,str)
	text_color: (str,str)
	text_color_disabled: (str,str)

@dataclass
class Cust_Combobox:
	corner_radius: int
	fg_color: (str,str)
	border_color: (str,str)
	button_color: (str,str)
	button_hover_color: (str,str)
	dropdown_fg_color: (str,str)
	dropdown_hover_color: (str,str)
	dropdown_text_color: (str,str)
	text_color: (str,str)
	text_color_disabled: (str,str)

@dataclass
class Cust_Frame:
	fg_color: (str,str)
	border_color: (str,str)
