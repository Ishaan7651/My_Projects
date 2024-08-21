import random
import keyboard
from time import sleep

class HiraganaQuiz:
    def __init__(self):
        self.running = True
        self.correct = 0
        self.incorrect = 0

    def run(self):
        keyboard.add_hotkey('esc', self.stop_program)
        while self.running:
            n = random.randint(0, 45)
            self.check_character(n)
        keyboard.remove_hotkey('esc')

    def check_character(self, i):
        chars = [
            'あ', 'い', 'う', 'え', 'お',
            'か', 'き', 'く', 'け', 'こ',
            'さ', 'し', 'す', 'せ', 'そ',
            'た', 'ち', 'つ', 'て', 'と',
            'な', 'に', 'ぬ', 'ね', 'の',
            'は', 'ひ', 'ふ', 'へ', 'ほ',
            'ま', 'み', 'む', 'め', 'も',
            'や', 'ゆ', 'よ',
            'ら', 'り', 'る', 'れ', 'ろ',
            'わ', 'を', 'ん'
        ]

        print(f"What is this character? {chars[i]}")

        romaji = [
            'a', 'i', 'u', 'e', 'o',
            'ka', 'ki', 'ku', 'ke', 'ko',
            'sa', 'shi', 'su', 'se', 'so',
            'ta', 'chi', 'tsu', 'te', 'to',
            'na', 'ni', 'nu', 'ne', 'no',
            'ha', 'hi', 'fu', 'he', 'ho',
            'ma', 'mi', 'mu', 'me', 'mo',
            'ya', 'yu', 'yo',
            'ra', 'ri', 'ru', 're', 'ro',
            'wa', 'wo', 'n'
        ]

        ans1 = input("Enter your answer: ")

        if ans1 == romaji[i]:
            print("Correct")
            self.correct += 1
            sleep(1)
        else:
            print("Wrong")
            self.incorrect += 1
            sleep(1)
            print(f"The correct answer is {romaji[i]}")
            sleep(1)

    def score(self):
        print(f"Correct: {self.correct}\nIncorrect: {self.incorrect}")
        sleep(1)

    def stop_program(self):
        self.running = False
        print("\nThe program has ended")
        self.score()

# Instantiate and run the quiz
quiz = HiraganaQuiz()
quiz.run()
