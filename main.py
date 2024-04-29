import random

words = ['amor', 'odio', 'calendario', 'dia', 
         'mesa', 'calendario', 'uniforme', 'empresa',
         'codigo', 'programa', 'agua', 'garrafa']

nome = input('Digite seu nome: ')
print(f'Olá {nome}, vamos começar o jogo da forca! Boa sorte. \n')

#pega uma palavra aleatória da lista de palavras criada
chosen_word = random.choice(words)
failed_guess = 0

#mostrar a quantidade de letras da palavra escolhida através do for
hidden_word = []
for letter in range(len(chosen_word)):
    hidden_word.append('_')

#pq o loop tá na palavra escondida? pq é nela que tá a quantidade de letras,
#e ela está sendo como base para a palavra escolhida (chosen_word)
while '_' in hidden_word:
    guess = input('\nDigite uma letra: ')
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                hidden_word[i] = guess
        print(' '.join(hidden_word))
        if '_' not in hidden_word:
            print(f'Parabéns {nome}, você ganhouuu!')
    else:
        failed_guess += 1
        if failed_guess == 1:
            print("   +---+")
            print("   O   |")
            print("       |")
            print("       |")
            print("      ===")
            print(' '.join(hidden_word))
        elif failed_guess == 2:
            print("   +---+")
            print("   O   |")
            print("   |   |")
            print("       |")
            print("      ===")
        elif failed_guess == 3:
            print("   +---+")
            print("   O   |")
            print("  /|   |")
            print("       |")
            print("      ===")
        elif failed_guess == 4:
            print("   +---+")
            print("   O   |")
            print("  /|\  |")
            print("       |")
            print("      ===")
        elif failed_guess == 5:
            print("   +---+")
            print("   O   |")
            print("  /|\  |")
            print("  /    |")
            print("      ===")
            
        elif failed_guess == 6:
            print("   +---+")
            print("   O   |")
            print("  /|\  |")
            print("  / \  |")
            print("      ===")
            print(f'Você perdeu {nome}! A palavra era', chosen_word)
            break