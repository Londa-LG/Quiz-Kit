# Quiz-Kit

This is a quiz library for adding quizs to a tkinter applications.

## Why this exist?

I'm currently working on a learning management system and I wanted a way to abstract away the quiz specific logic, so building will boil down to using prebuilt classes.

## Quick Start


To quickly get a quick demo do the following: clone this repo.

```bash
git clone https://github.com/Londa-LG/Quiz-Kit.git
```
Create a virtual environment and activate it

```bash
python3 -m venv venv
source venv/bin/activate
```

Install customtkinter

```bash
pip install customtkinter
```

Run the demo

```bash
python demo.py
```

## Usage

### Question classes

**Multiple_Choice**

A class that returns a multiple choice question.

**Example**
```python
import tkinter as tk
from default.questtions import Multiple_Choice

window = tk.Tk()
window.title("Multiple Choice question")
window.geometry("400x400")

Multiple_choice(
	parent = window,
	question = "What's 1 + 1",
	answer = "2",
	options = ["3","8","4","2"],
	total_mark = 2
)

window.mainloop()
```

**Match_Columns**

A class used to match values is a table together.

Note: when grading each key pair amounts to 1 mark.

**Example**
```python
import tkinter as tk
from default.questtions import Match_Columns

window = tk.Tk()
window.title("Matching columns question")
window.geometry("400x400")

Match_Columns(
	parent = window,
	question = "Match the acronyms",
	column_1 = ["KFC","SAAS","RAM","ROM"],
	columnt_2 = ["Kentucky fried chicken","Software as a service","Random access memory","Read only memory"],
	answer = {"KFC":"Kentucky fried chicken","SAAS":"Software as a service","RAM":"Random access memory","ROM":"Read only memory"}
)

window.mainloop()
```

**Enter_Text**

A class used to create a question that requires the user to enter a string as an answer.


**Example**
```python
import tkinter as tk
from default.questtions import Enter_Text

window = tk.Tk()
window.title("Enter Text question")
window.geometry("400x400")

Enter_Text(
	parent = window,
	question = "What is the 6th month of the year?",
	answer = "June",
	total_mark = 2
)

window.mainloop()
```

**Enter_Number**

A class used to create a question that requires the user to enter a number as an answer.


**Example**
```python
import tkinter as tk
from default.questtions import Enter_Number

window = tk.Tk()
window.title("Enter number question")
window.geometry("400x400")

Enter_Number(
	parent = window,
	question = "What year is it?",
	answer = "2024",
	total_mark = 2
)

window.mainloop()
```
### Test class

Used for creating tests.

```python
import tkinter as tk
from default.questtions import Test

window = tk.Tk()
window.title("First term exam")
window.geometry("400x400")

# (title,description,subject,users grade,test total)
Test_details = (
	"First term exam",
	"Covers units 1-3, no calculators allowed",
	"Grade 6 Mathematics",
	9,
	20
)

Test_questions = [
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

Test(
	parent = window,
	paper = Test_details,
	questions = Test_questions,
)

window.mainloop()
```

### Customizer classes

Customizing widgets is done using customtkinter for more info on that check out the [docs](https://www.customtkinter.tomschimansky.com/), however since widgets are made in the question classes I've written dataclasses to build objects that'll hold the customizations, which I can then pass to their respective classes.

**Customizing the Multiple Choice question**

```python
import tkinter as tk
from default.questtions import Multiple_Choice
from Styled.customizers import (
	Cust_Label,
	Cust_Frame,
	Cust_Radiobutton
)

window = tk.Tk()
window.title("Multiple Choice question")
window.geometry("400x400")

# Customizers
custom_label = Cust_Label(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("#22252a","#8a8d93"),
	font = ("monoscope",18,"normal","roman",False,False)
)
custom_radiobutton = Cust_Radiobutton(
	corner_radius = 5,
	fg_color = ("grey","white"),
	hover_color = ("grey","white"),
	text_color = ("black","#8a8d93"),
	hover = False
)
custom_frame = Cust_Frame(
	fg_color = ("white","#2d3035"),
	border_color = ("white","#2d3035")
)

Multiple_choice(
	parent = window,
	question = "What's 1 + 1",
	answer = "2",
	options = ["3","8","4","2"],
	total_mark = 2,
	style = (custom_label,custom_radiobutton),
	frame_style = custom_frame
)

window.mainloop()
```

**Customizing the Match Columns question**

```python
import tkinter as tk
from default.questtions import Match_Columns
from Styled.customizers import (
	Cust_Label,
	Cust_Frame,
	Cust_Combobox
)

window = tk.Tk()
window.title("Matching columns question")
window.geometry("400x400")


# Customizers
custom_label = Cust_Label(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("#22252a","#8a8d93"),
	font = ("monoscope",18,"normal","roman",False,False)
)
custom_combobox = Cust_Combobox(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	button_color = ("grey","white"),
	text_color = ("black","#8a8d93"),
	border_color = ("grey","#8a8d93"),
	button_hover_color = ("grey","white"),
	dropdown_fg_color = ("white","white"),
	text_color_disabled = ("grey","white"),
	dropdown_text_color = ("black","black"),
	dropdown_hover_color = ("grey","#8a8d93"),
)
custom_frame = Cust_Frame(
	fg_color = ("white","#2d3035"),
	border_color = ("white","#2d3035")
)

Match_Columns(
	parent = window,
	question = "Match the acronyms",
	column_1 = ["KFC","SAAS","RAM","ROM"],
	columnt_2 = ["Kentucky fried chicken","Software as a service","Random access memory","Read only memory"],
	answer = {"KFC":"Kentucky fried chicken","SAAS":"Software as a service","RAM":"Random access memory","ROM":"Read only memory"},
	style = (custom_label,custom_combobox),
	frame_style = custom_frame
)

window.mainloop()
```

**Customizing the Enter Text question**

```python
import tkinter as tk
from default.questtions import Enter_Text
from Styled.customizers import (
	Cust_Label,
	Cust_Frame,
	Cust_Entry
)

window = tk.Tk()
window.title("Enter Text question")
window.geometry("400x400")

# Customizers
custom_label = Cust_Label(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("#22252a","#8a8d93"),
	font = ("monoscope",18,"normal","roman",False,False)
)
custom_entry = Cust_Entry(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("black","#8a8d93"),
	placeholder_text_color = "grey"
)
custom_frame = Cust_Frame(
	fg_color = ("white","#2d3035"),
	border_color = ("white","#2d3035")
)

Enter_Text(
	parent = window,
	question = "What is the 6th month of the year?",
	answer = "June",
	total_mark = 2,
	style = (custom_label,custom_entry),
	frame_style = custom_frame
)

window.mainloop()
```

**Customizing the Enter Number question**

```python
import tkinter as tk
from default.questtions import Enter_Number
from Styled.customizers import (
	Cust_Label,
	Cust_Frame,
	Cust_Entry
)

window = tk.Tk()
window.title("Enter number question")
window.geometry("400x400")

# Customizers
custom_label = Cust_Label(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("#22252a","#8a8d93"),
	font = ("monoscope",18,"normal","roman",False,False)
)
custom_entry = Cust_Entry(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("black","#8a8d93"),
	placeholder_text_color = "grey"
)
custom_frame = Cust_Frame(
	fg_color = ("white","#2d3035"),
	border_color = ("white","#2d3035")
)

Enter_Number(
	parent = window,
	question = "What year is it?",
	answer = "2024",
	total_mark = 2,
	style = (custom_label,custom_entry)
)

window.mainloop()
```

**Customizing when using the Test class**

```python
import tkinter as tk
from default.questtions import Test
from Styled.customizers import
	Cust_Label,
	Cust_Entry,
	Cust_Button,
	Cust_Combobox,
	Cust_Radiobutton

window = tk.Tk()
window.title("First term exam")
window.geometry("400x400")

Test_details = (
	"First term exam",
	"Covers units 1-3, no calculators allowed",
	"Grade 6 Mathematics",
	9,
	20
)

Test_questions = [
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

# Customizers
custom_label = Cust_Label(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("#22252a","#8a8d93"),
	font = ("monoscope",18,"normal","roman",False,False)
)
custom_radiobutton = Cust_Radiobutton(
	corner_radius = 5,
	fg_color = ("grey","white"),
	hover_color = ("grey","white"),
	text_color = ("black","#8a8d93"),
	hover = False
)
custom_combobox = Cust_Combobox(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	button_color = ("grey","white"),
	text_color = ("black","#8a8d93"),
	border_color = ("grey","#8a8d93"),
	button_hover_color = ("grey","white"),
	dropdown_fg_color = ("white","white"),
	text_color_disabled = ("grey","white"),
	dropdown_text_color = ("black","black"),
	dropdown_hover_color = ("grey","#8a8d93"),
)
custom_entry = Cust_Entry(
	corner_radius = 5,
	fg_color = ("white","#2d3035"),
	text_color = ("black","#8a8d93"),
	placeholder_text_color = "grey"
)
custom_frame = Cust_Frame(
	fg_color = ("white","#2d3035"),
	border_color = ("white","#2d3035")
)
custom_button = Cust_Button(
	corner_radius = 5,
	fg_color = ("blue","blue"),
	hover_color = ("lightblue","lightblue"),
	border_color = ("blue","blue"),
	text_color = ("white","white"),
	text_color_disabled = ("grey","grey"),
)

Test(
	parent = window,
	paper = Test_details,
	questions = Test_questions,
	frame_style = custom_frame,
	# (navbtns,Multiple choice,EnterText,EnterNumber) in that order
	style = (
		custom_button,
		(custom_label,custom_radiobutton),
		(custom_label,custom_combobox),
		(custom_label,custom_entry),
		(custom_label,custom_entry)
	)
)

window.mainloop()
```

## Contributions

### Clone the repo

```bash
git clone https://github.com/Londa-LG/Quiz-Kit.git
cd Quiz-Kit
```

### Create the virtual environment

```bash
python -m venv venv
```

### Install customtkinter

```bash
pip install customtkinter
```

### Test install

Run styled-demo.py to makesure everything works

```bash
python styled-demo.py
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request.
