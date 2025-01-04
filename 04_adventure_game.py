adventures = {
    "env": "You are at river and there is a bridge.",
    "choices": [
        {
            "choice": "swim",
            "env": "Oh no you were caught by aligator.",
            "isGameOver": True
        },
        {
            "choice": "cross",
            "env": "You walked across bridge. You met a person.",
            "choices": [
                {
                    "choice": "Talk to that Person",
                    "env": "He showed you the way to village.",
                    "choices": [
                        {
                            "choice": "run",
                            "env": "You reached the village.",
                            "isWin": True
                        },
                        {
                            "choice": "walk",
                            "env": "You walked slow and it is night. Now you are lost!",
                            "isGameOver": True,
                        }
                    ]
                },
                {
                    "choice": "Ignore that Person",
                    "env": "You got lost! should have asked way!",
                    "isGameOver": True
                }
            ]
        }
    ]
}

gameState = adventures

while True:
    print(f"\n{gameState['env']}")

    if 'isGameOver' in gameState and  gameState['isGameOver']:
        print("Game Over!")
        break

    if 'isWin' in gameState and gameState['isWin']:
        print("You Won! - Adventure Completed!")
        break

    choice = input(f"Choices: 0 = {gameState['choices'][0]['choice']}, 1 = {gameState['choices'][1]['choice']}: ")

    if choice.isdigit():
        choice = int(choice)
    else:
        print("Invalid!")
        continue

    if choice != 0 and choice != 1:
        print("Invalid!")
        continue
    
    gameState = gameState['choices'][choice]
