from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

class TicTacToe(App):
    def build(self):
        self.player = "X"
        self.moves = [""] * 9
        self.game_over = False

        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        self.info = Label(text="Player X", font_size=28, size_hint_y=None, height=50)
        root.add_widget(self.info)

        self.grid = GridLayout(cols=3, spacing=5)
        self.buttons = []
        for i in range(9):
            btn = Button(text="", font_size=48)
            btn.index = i
            btn.bind(on_press=self.on_press)
            self.buttons.append(btn)
            self.grid.add_widget(btn)
        root.add_widget(self.grid)

        control_bar = BoxLayout(size_hint_y=None, height=50, spacing=10)
        reset_btn = Button(text="Reset")
        reset_btn.bind(on_press=self.reset)
        control_bar.add_widget(reset_btn)
        root.add_widget(control_bar)

        return root

    def on_press(self, btn):
        if self.game_over or btn.text != "":
            return
        btn.text = self.player
        self.moves[btn.index] = self.player
        if self.check_winner(self.player):
            self.info.text = f"Player {self.player} wins! 🎉"
            self.game_over = True
            return
        if all(m != "" for m in self.moves):
            self.info.text = "It's a draw 🤝"
            self.game_over = True
            return
        self.player = "O" if self.player == "X" else "X"
        self.info.text = f"Player {self.player}"

    def check_winner(self, p):
        for a, b, c in WIN_COMBOS:
            if self.moves[a] == self.moves[b] == self.moves[c] == p:
                # highlight winning buttons
                for i in (a, b, c):
                    self.buttons[i].background_color = (0, 1, 0, 1)
                return True
        return False

    def reset(self, *_):
        self.player = "X"
        self.moves = [""] * 9
        self.game_over = False
        self.info.text = "Player X"
        for btn in self.buttons:
            btn.text = ""
            btn.background_color = (1, 1, 1, 1)

if __name__ == "__main__":
    TicTacToe().run()