import random
import keyboard
from time import sleep

running = True
Correct = 0
Incorrect = 0

class hiragana():
    
    def __init__(self,i):
        global Correct
        global Incorrect
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
        
        print(f"What is this charector? {chars[i]}")

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
    'wa', 'wo','n'
]
        ans1 = input("Enter your answer :-")
        
        if ans1 == romaji[i]:
            print("Correct")
            Correct = Correct + 1
            sleep(1)
        else:
            print("Wrong")
            Incorrect = Incorrect + 1
            sleep(1)
            print(f"The correct answer is {romaji[i]}")
            sleep(1)
        
    

       
def score():
    
    print(f"Correct: {Correct}\nIncorrect: {Incorrect}")
    sleep(1)

    
def stop_program():
    global running
    running = False
    print("\nThe program has ended")
    score()
    keyboard.unhook_all()
    
keyboard.add_hotkey('esc', stop_program)

print("-------------Welcome to the Japanese Quiz---------------\nLearn Hiragana Charectors with us")
sleep(1)
while running:
    n = random.randint(0,45)
    a = hiragana(n)
    print("------------Press escape anytime to quit and get score------------")
    sleep(1)


