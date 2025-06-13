import tkinter as tk
import random

questions = [
    ("Stolica Francji?", ["Paryż", "Berlin", "Madryt", "Rzym"]),
    ("Ile nóg ma pająk?", ["8", "6", "10", "12"]),
    ("Który pierwiastek ma symbol H?", ["Wodór", "Hel", "Rtęć", "Wapń"]),
    ("Największy ocean?", ["Spokojny", "Atlantycki", "Indyjski", "Arktyczny"]),
    ("Autor 'Pana Tadeusza'?", ["Adam Mickiewicz", "Juliusz Słowacki", "Henryk Sienkiewicz", "Bolesław Prus"]),
    ("Który kraj nie graniczy z Polską?", ["Włochy", "Czechy", "Ukraina", "Słowacja"]),
    ("Ile to 5 * 6?", ["30", "35", "25", "20"]),
    ("Który kontynent jest najmniejszy?", ["Australia", "Europa", "Antarktyda", "Afryka"]),
    ("Który zwierzak jest ssakiem?", ["Nietoperz", "Kura", "Żaba", "Żółw"]),
    ("Który kolor nie jest w tęczy?", ["Różowy", "Fioletowy", "Czerwony", "Zielony"])
]

class MillionaireGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Milionerzy")
        self.root.configure(bg="#001f3f")

        self.score = 0
        self.question_index = 0
        self.selected_questions = random.sample(questions, 3)

        self.label = tk.Label(root, text="", wraplength=600, font=("Arial", 18, "bold"),
                              bg="#001f3f", fg="white")
        self.label.pack(pady=30)

        self.button_frame = tk.Frame(root, bg="#001f3f")
        self.button_frame.pack()

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.button_frame, text="", font=("Arial", 14),
                            width=25, height=2, bg="#0074D9", fg="white",
                            activebackground="#FF851B", activeforeground="black",
                            command=lambda b=i: self.check_answer(b))
            self.buttons.append(btn)

        self.buttons[0].grid(row=0, column=0, padx=20, pady=10)
        self.buttons[1].grid(row=0, column=1, padx=20, pady=10)
        self.buttons[2].grid(row=1, column=0, padx=20, pady=10)
        self.buttons[3].grid(row=1, column=1, padx=20, pady=10)

        self.next_question()

    def next_question(self):
        for btn in self.buttons:
            btn.config(state="normal", bg="#0074D9")
        
        if self.question_index < len(self.selected_questions):
            question, answers = self.selected_questions[self.question_index]
            self.correct_answer = answers[0]
            random.shuffle(answers)
            self.label.config(text=f"Pytanie {self.question_index + 1}: {question}")
            for i, btn in enumerate(self.buttons):
                btn.config(text=answers[i])
        else:
            self.show_result()

    def check_answer(self, button_index):
        chosen = self.buttons[button_index].cget("text")
        for btn in self.buttons:
            btn.config(state="disabled")
        if chosen == self.correct_answer:
            self.score += 1
            self.buttons[button_index].config(bg="green")
        else:
            self.buttons[button_index].config(bg="red")
            for btn in self.buttons:
                if btn.cget("text") == self.correct_answer:
                    btn.config(bg="green")
        self.root.after(1500, self.advance)

    def advance(self):
        self.question_index += 1
        self.next_question()

    def show_result(self):
        for btn in self.buttons:
            btn.destroy()
        percent = int((self.score / 3) * 100)
        wynik = {33: "Słabo", 66: "Nieźle!", 100: "Milion rubli w kieszeni!"}.get(percent, "Coś nie pykło")
        self.label.config(text=f"Koniec gry!\nTwój wynik: {percent}%\n{wynik}")

if __name__ == "__main__":
    root = tk.Tk()
    game = MillionaireGame(root)
    root.mainloop()
