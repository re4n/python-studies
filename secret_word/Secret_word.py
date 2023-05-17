secret_word = 'balao'
hidden_secret_word = len(secret_word) * '*'
attempts = 0

play = True


def resetGame():
    stopGame = input('Do you want leave? [y] or [n]: ').lower().startswith('y')
    print('Reloading App...')
    global attempts
    attempts = 0
    global hidden_secret_word
    hidden_secret_word = len(secret_word) * '*'

    if stopGame is True:
        print('Finished App...')
        global play
        play = False


while play:
    print('\n============================')
    print('==\ Find The Secret Word /==')
    print('============================\n')

    letterAttempts = input('Type a Letter: ')

    if isinstance(letterAttempts, str) and letterAttempts in secret_word:
        print(f'Right!, "{letterAttempts.upper()}" is in Secret Word!')
        ocorrancy = []

        for i in range(len(secret_word)):
            if secret_word[i] == letterAttempts:
                ocorrancy.append(i)
        hidden_secret_word = list(hidden_secret_word)

        for i in ocorrancy:
            hidden_secret_word[i] = letterAttempts
        hidden_secret_word = ''.join(hidden_secret_word)
        print(f'The secret word so far is: {hidden_secret_word} ')

        if "*" not in hidden_secret_word:
            print(
                f'Congrats, You won!!, the secret word is: {hidden_secret_word}')
            resetGame()

    else:
        print(f"{letterAttempts} it's not in the secret word")
        attempts += 1

        if attempts == 3:
            print('You Lose!')
            resetGame()
