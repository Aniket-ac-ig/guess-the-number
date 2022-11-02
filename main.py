import random

logo = """  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       """

# tidy up the code***************************************************************************************************


print(logo)

ANS = random.randint(1, 100)
EASY = 10
HARD = 5

is_game_over = False

lives = input("type 'e' for easy level and 'h' for hard level: ")
if (lives == 'e'):
    lives = EASY
elif (lives == 'h'):
    lives = HARD

print(f"you will have {lives} lives")

while (not is_game_over and lives > 0):
    guess = int(input("Enter a guess: "))
    if (guess > ANS):
        print("too high")
        lives -= 1
        print(f"you have {lives} lives left")
    elif (guess < ANS):
        print("too low")
        lives -= 1
        print(f"you have {lives} lives left")
    else:
        print("you guessed correctly")
        is_game_over = True
else:
    if (not lives):
        print("you lost")
