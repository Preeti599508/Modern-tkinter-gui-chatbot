import os
import openai
import customtkinter as ctk

# openai.api_key=os.getenv("")
# response=openai.ChatCompletion.creat(
#     model="get-3.5-turbo",
#     message=[
#         {"role":"user","content":"Hi Chatgpt.Saky hi back"}
#     ]
# )
# answer=response.choices[0].message.content

def generate():
    prompt="please generate 10 ideas for coding project,"
    language=language_dropdown.get()
    prompt+="The programming language is  " + language + ", "
    difficulty=difficulty.value.get()
    prompt +="The difficulty is " + difficulty + " ,"
    if checkbox1.get():
        prompt +="The project should include a database. "
    if checkbox2.get():
        prompt +=" The project should include in API"
    print(prompt)

    openai.api_key=os.getenv("")
    response=openai.ChatCompletion.creat(
        model="get-3.5-turbo",
        message=[
            {"role":"user","content": prompt}
        ]
    )
    answer=response.choices[0].message.content
    print(answer)
    result.insert("0.0",answer)




root=ctk.CTk()
root.geometry("750x550")
root.title("ChatGOT Project Idea Generator")

ctk.set_appearance_mode("dark")

title_label=ctk.CTkLabel(root,text="Project Idea Generator",font=ctk.CTkFont(size=30,weight="bold"))
title_label.pack(padx=10,pady=(40,20))

frame=ctk.CTkFrame(root)
frame.pack(fil='x',padx=100)

language_frame=ctk.CTkFrame(frame)
language_frame.pack(padx=100,pady=(20,5),fill=('both'))
language_label=ctk.CTkLabel(language_frame,text="Programming Language",font=ctk.CTkFont(weight="bold"))
language_label.pack()

language_dropdown=ctk.CTkComboBox(language_frame,values=["Python","Java","C","C++","Javascript"])
language_dropdown.pack(pady=10)

difficulty_frame=ctk.CTk(frame)
difficulty_frame.pack(padx=100,pady=5,fill="both")
difficulty_label=ctk.CTkLabel(difficulty_frame,text="Project difficulty",font=ctk.CTkFont(weight="bold"))
difficulty_label.pack()
difficulty_values=ctk.CTkStringVar(value="Easy")
radiobutton=ctk.CTkRadioButton(difficulty_frame,text="Easy",variable=difficulty_values,values="Easy")
radiobutton.pack(side="left",padx=(20,10),pady=10)

radiobutton2=ctk.CTkRadioButton(difficulty_frame,text="Medium",variable=difficulty_values,values="Medium")
radiobutton2.pack(side="left",padx=(20,10),pady=10)

radiobutton3=ctk.CTkRadioButton(difficulty_frame,text="Hard",variable=difficulty_values,values="Hard")
radiobutton3.pack(side="left",padx=(20,10),pady=10)

features_frame=ctk.CTk(frame)
features_frame.pack(padx=100,pady=5,fill="both")
features_label=ctk.CTkLabel(features_frame,text="Features",font=ctk.CTkFont(weight="bold"))
features_label.pack()
checkbox1=ctk.CTkCheckBox(features_frame,text="Database")
checkbox1.pack(padx=50,pady=10,side="left")
checkbox2=ctk.CTkCheckBox(features_frame,text="API")
checkbox2.pack(padx=50,pady=10,side="left")

button=ctk.CTkButton(frame,text="Generate Ideas",command=generate)
button.pack(padx=100,pady=(5,20),fill="x")

result=ctk.CTkTextbox(root,font=ctk.CTkFont(size=15))

root.mainloop()