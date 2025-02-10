import random

# Store the highest score
highest_score = 0

def play_round(question, correct_answer, hint):
    chances = 5  # Maximum attempts
    print(f"\n🧐 QUESTION: {question}")

    while chances > 0:
        answer = input("\nEnter your answer: ").strip().lower()

        if answer == correct_answer:
            print("\n🎉 Correct! You won this round! 🥳")
            return 1  

        else:
            chances -= 1
            print(f"\n❌ Wrong answer! Remaining chances: {chances}")

            if chances == 3:  
                print(f"\n💡 Hint: {hint}")

    print(f"\n😞 You lost this round! The correct answer was '{correct_answer.capitalize()}'.")
    return 0  


def main():
    global highest_score 
    print("\n\t\t🎮 WORD GUESSING GAME 🎮")
    name = input("Enter your name: ").strip()
    print(f"\nGood Luck! 😇 {name}")

   
    questions = [
        ("Against which country did Virat Kohli get his first Test century?", "australia", "Its capital is Canberra."),
        ("What is the red planet in our solar system?", "mars", "Named after the Roman god of war."),
        ("What is the largest ocean in the world?", "pacific ocean", "It covers more area than all the land combined."),
        ("Who is known as the 'God of Cricket'?", "sachin tendulkar", "His jersey number was 10."),
        ("Which country won the FIFA World Cup in 2018?", "france", "The team captain was Hugo Lloris.")
    ]

    random.shuffle(questions)  

    score = 0
    for question, answer, hint in questions:
        score += play_round(question, answer, hint)

       
        again = input("\nDo you want to continue playing? (yes/no): ").strip().lower()
        while again not in ["yes", "no"]:
            again = input("⚠️ Invalid input! Please enter 'yes' or 'no': ").strip().lower()

        if again == "no":
            break 

   
    if score > highest_score:
        highest_score = score
        print(f"\n🏆 New High Score: {highest_score} 🏆")

    print(f"\n🎊 Thanks for playing, {name}! Your final score is {score}. 🎊")

  
    restart = input("\nDo you want to play again? (yes/no): ").strip().lower()
    while restart not in ["yes", "no"]:
        restart = input("⚠️ Invalid input! Please enter 'yes' or 'no': ").strip().lower()

    if restart == "yes":
        main()  # Restart the game

# Run the game
if __name__ == "__main__":
    main()
