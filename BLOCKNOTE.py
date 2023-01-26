from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def change_theme(theme):
    text_field['bg'] = view_colors[theme]['text_bg']
    text_field['fg'] = view_colors[theme]['text_fg']
    text_field['insertbackground'] = view_colors[theme]['cursor']
    text_field['selectbackground'] = view_colors[theme]['select_bg']

def change_fonts(fontss):
    text_field['font'] = fonts[fontss]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы хотите выйти или нет?')
    if answer:
        root.destroy()

def file_open():
    file_path = filedialog.askopenfilename(title='Выбор фаила', filetypes=(('Текстовые документы,(*.txt)', '*.txt'), ('Все фаилы', '*.*')))
    if file_path:
        text_field.delete('1.0', END)
        text_field.insert('1.0', open(file_path, encoding='utf-8').read())

def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы,(*.txt)', '*.txt'), ('Все фаилы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_field.get('1.0', END)
    f.write(text)
    f.close()





root = Tk()
root.title('БЛОКНОТ')
root.geometry('600x700')

main_menu = Menu(root)
#Фаил
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Открыть', command=file_open)
file_menu.add_separator()
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu = file_menu)

#Вид
view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
view_menu_sub.add_command(label='Тёмная', command=lambda: change_theme('dark'))
view_menu_sub.add_command(label='Светлая', command=lambda: change_theme('light'))
view_menu.add_cascade(label='Тема', menu=view_menu_sub)
view_menu.add_separator()
font_menu_sub.add_command(label='Arial', command=lambda: change_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: change_fonts('Comic Sans MS'))
font_menu_sub.add_command(label='Times New Roman', command=lambda: change_fonts('Times New Roman'))
view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
root.config(menu = view_menu)

#Добавление списков меню
main_menu.add_cascade(label='Фаил', menu=file_menu)
main_menu.add_cascade(label='Вид', menu=view_menu)



root.config(menu = main_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)
view_colors = {
    'dark': {
        'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'white', 'select_bg': 'gray'
    },
    'light': {
        'text_bg': 'white', 'text_fg': 'black', 'cursor': 'gray', 'select_bg': 'silver'

    }


}
fonts = {
    'Arial': {
        'font': 'Arial 14 bold'
    },
    'Comic Sans MS': {
        'font':('Comic Sans MS', 14, 'bold')

    },
    'Times New Roman': {
        'font':('Times New Roman', 14, 'bold')
    }


}
text_field = Text(f_text,
                  bg = 'black',
                  fg = 'lime',
                  padx=10,
                  pady=10,
                  wrap=WORD, #грамотный перенос
                  insertbackground='white', #курсор
                  selectbackground='gray', #выделение текста
                  spacing3=10, #обзацы
                  font='Arial 14 bold'


                  )
text_field.pack(expand=1, fill=BOTH, side=LEFT)
scroll = Scrollbar(f_text, command=text_field.yview)
scroll.pack(side=LEFT, fill=Y)
text_field.config(yscrollcommand=scroll.set)

root.mainloop()
