import tkinter as tk
from tkinter import messagebox, filedialog
question_index = 0
score = 0
wrong_answers = []
selected_answers = []
questions = [
    {
        'question': 'Яка властивість відповідає за фон фрейма?',
        'options': ['width', 'height', 'bg', 'bd'],
        'correct_option': 'bg',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за рельєф межі фрейма?',
        'options': ['state', 'relief', 'highlightthickness', 'width'],
        'correct_option': 'relief',
        'type': 'radio'
    },
    {
        'question': 'Які параметри відповідають за розміщення віджету на вікні?',
        'options': ['__x, __y', 'anchor', 'height / width', ' window'],
        'correct_option': 'anchor',
        'type': 'radio'
    },
    {
        'question': 'Які з властивостей відповідають за вигляд текстового поля, коли воно має фокус?',
        'options': ['activebackground', 'activeforeground', 'highlightcolor', 'highlightbackground'],
        'correct_option': 'highlightbackground',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за колір тексту в полі, коли властивість state = DISABLED?',
        'options': ['fg', 'bd', 'disabledforeground', 'disabledbackground'],
        'correct_option': 'disabledforeground',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за встановлення ширини другої межі текстового поля?',
        'options': ['highlightcolor', 'highlightbackground', 'highlightthickness', 'relief'],
        'correct_option': 'highlightthickness',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за вирівнювання тексту в текстовому полі?',
        'options': ['justify', 'font', 'textvariable', 'selectbackground'],
        'correct_option': 'justify',
        'type': 'radio'
    },
    {
        'question': 'Яке значення властивості state призводить до того, що поле неактивне та не може бути змінене користувачем?',
        'options': ['NORMAL', 'DISABLED', 'ACTIVE', 'FOCUS'],
        'correct_option': 'DISABLED',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за колір фону виділеного фрагмента тексту?',
        'options': ['selectbackground', 'selectforeground', 'insertontime', 'insertofftime'],
        'correct_option': 'selectbackground',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за встановлення стану чекбоксу?',
        'options': ['state', 'checked', 'relief', 'highlightthickness'],
        'correct_option': 'state',
        'type': 'radio'
    },
    {
        'question': 'Яке значення властивості вказує на те, що чекбокс обраний?',
        'options': ['ON', 'OFF', 'CHECKED', 'SELECTED'],
        'correct_option': 'CHECKED',
        'type': 'radio'
    },
    {
        'question': 'Яка властивість відповідає за фон чекбоксу?',
        'options': ['bg', 'fg', 'highlightcolor', 'activebackground'],
        'correct_option': 'bg',
        'type': 'radio'
    }
]
def enable_submit_button():
    submit_button.config(state=tk.NORMAL)
def show_previous_question():
    global question_index
    if question_index > 0:
        question_index -= 1
        show_question()
def show_question():
    global question_index
    if question_index < len(questions):
        question_data = questions[question_index]
        question_label.config(text=f"Питання {question_index + 1}: {question_data['question']}", justify="center")
        for button in option_buttons:
            button.destroy()
        option_buttons.clear()
        if question_data['type'] == 'radio':
            for i in range(4):
                button = tk.Radiobutton(root, text=question_data['options'][i], variable=radio_var, value=i, command=enable_submit_button)
                option_buttons.append(button)
                button.pack()
        enable_submit_button()
def check_answer():
    global question_index, score, wrong_answers, selected_answers
    if questions[question_index]['type'] == 'radio':
        selected_option = radio_var.get()
        if selected_option == "":
            messagebox.showerror("Помилка", "Ви не обрали жодної відповіді. Будь ласка, оберіть відповідь.")
            return
        selected_option = int(selected_option) if selected_option is not None and selected_option.isdigit() else None
        if selected_option is None:
            messagebox.showerror("Помилка", "Ви не обрали жодної відповіді. Будь ласка, оберіть відповідь.")
            return
        selected_answers.append((questions[question_index]['question'], selected_option))
        correct_option_index = questions[question_index]['options'].index(questions[question_index]['correct_option'])
        if selected_option == correct_option_index:
            score += 1  # Збільшуємо бал на 1 за кожну правильну відповідь
        else:
            wrong_answers.append((questions[question_index]['question'], selected_option, correct_option_index))
    elif questions[question_index]['type'] == 'checkbox':
        selected_options = [checkbox_vars[i].get() for i in range(len(checkbox_vars)) if checkbox_vars[i].get()]
        if not selected_options:
            messagebox.showerror("Помилка", "Ви не обрали жодної відповіді. Будь ласка, оберіть відповідь.")
            return
        selected_answers.append((questions[question_index]['question'], selected_options))
        correct_option_indices = [questions[question_index]['options'].index(option) for option in questions[question_index]['correct_option']]
        if set(selected_options) == set(correct_option_indices) and len(selected_options) == len(correct_option_indices):
            score += 1  # Збільшуємо бал на 1 за кожну правильну відповідь
        else:
            wrong_answers.append((questions[question_index]['question'], selected_options, correct_option_indices))
    question_index += 1
    if question_index == len(questions):
        show_result()
    else:
        show_question()
def restart_quiz():
    global question_index, score, wrong_answers, selected_answers
    question_index = 0
    score = 0
    wrong_answers.clear()
    selected_answers.clear()
    show_question()
def exit_program():
    root.destroy()
def save_results():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filename:
        with open(filename, 'w') as file:
            file.write("Результати тестування:\n\n")
            for i, question_data in enumerate(questions):
                question = question_data['question']
                correct_option = question_data['correct_option']
                selected_answer = selected_answers[i] if i < len(selected_answers) else None
                if question_data['type'] == 'radio':
                    selected_option = selected_answer[1] if selected_answer else None
                    file.write(f"Питання {i + 1}: {question}\nВаш вибір: {selected_option}\nПравильна відповідь: {correct_option}\n\n")
                elif question_data['type'] == 'checkbox':
                    selected_options = selected_answer[1] if selected_answer else None
                    file.write(f"Питання {i + 1}: {question}\nВаш вибір: {', '.join(selected_options)}\nПравильна відповідь: {', '.join(correct_option)}\n\n")
            file.write(f"Ваш результат: {score} / {len(questions)}\n")
            percentage_score = (score / len(questions)) * 100
            if percentage_score >= 80:
                grade = "Відмінно"
            elif 60 <= percentage_score < 80:
                grade = "Добре"
            elif 40 <= percentage_score < 60:
                grade = "Задовільно"
            else:
                grade = "Незадовільно"
            file.write(f"Оцінка: {grade}\n")
def show_result():
    show_result_window()
def show_result_window():
    result_window = tk.Toplevel(root)
    result_window.title("Результати тестування")
    result_canvas = tk.Canvas(result_window)
    result_canvas.pack(side=tk.LEFT, fill="both", expand=True)
    scrollbar = tk.Scrollbar(result_window, orient="vertical", command=result_canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill="y")
    result_canvas.configure(yscrollcommand=scrollbar.set)
    result_frame = tk.Frame(result_canvas)
    result_canvas.create_window((0, 0), window=result_frame, anchor="nw")
    result_text = tk.Text(result_frame, wrap="word")
    result_text.pack(fill="both", expand=True)
    result_text.insert(tk.END, "Результати тестування:\n\n")
    for i, question_data in enumerate(questions):
        question = question_data['question']
        correct_option = question_data['correct_option']
        selected_answer = selected_answers[i] if i < len(selected_answers) else None
        if question_data['type'] == 'radio':
            selected_option = selected_answer[1] if selected_answer else None
            result_text.insert(tk.END, f"Питання {i + 1}: {question}\nВаш вибір: {selected_option}\nПравильна відповідь: {correct_option}\n\n")
        elif question_data['type'] == 'checkbox':
            selected_options = selected_answer[1] if selected_answer else None
            result_text.insert(tk.END, f"Питання {i + 1}: {question}\nВаш вибір: {', '.join(selected_options)}\nПравильна відповідь: {', '.join(correct_option)}\n\n")
    result_text.insert(tk.END, f"Ваш результат: {score} / {len(questions)}\n")
    percentage_score = (score / len(questions)) * 100
    if percentage_score >= 80:
        grade = "Відмінно"
    elif 60 <= percentage_score < 80:
        grade = "Добре"
    elif 40 <= percentage_score < 60:
        grade = "Задовільно"
    else:
        grade = "Незадовільно"
    result_text.insert(tk.END, f"Оцінка: {grade}\n")
    result_text.config(state="disabled")
    def on_configure(event):
        result_canvas.configure(scrollregion=result_canvas.bbox("all"))
    result_text.bind("<Configure>", on_configure)
root = tk.Tk()
root.title("Система тестування знань")
root.configure(bg="lightblue")
question_label = tk.Label(root, text="", justify="center", bg="lightblue", fg="black")
question_label.pack()
radio_var = tk.StringVar()
radio_var.set(None)
checkbox_vars = [tk.IntVar() for _ in range(4)]
option_buttons = []
menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=False)
file_menu.add_command(label="Вихід", command=exit_program)
file_menu.add_command(label="Зберегти результат", command=save_results)
menu.add_cascade(label="Файл", menu=file_menu)
menu.add_command(label="Результат", command=show_result)
menu.add_command(label="Ще одна спроба", command=restart_quiz)
button_frame = tk.Frame(root, bg="lightblue")  # Set background color of the frame
back_button = tk.Button(button_frame, text="Назад", command=show_previous_question, bg="gray", fg="white")  # Set button colors
back_button.pack(side=tk.LEFT)
submit_button = tk.Button(button_frame, text="Відповісти", command=check_answer, state=tk.DISABLED, bg="gray", fg="white")  # Set button colors
submit_button.pack(side=tk.RIGHT)
button_frame.pack(side=tk.BOTTOM)
show_question()
root.mainloop()