import random

words = ['amor', 'odio', 'calendario', 'dia', 
         'mesa', 'calendario', 'uniforme', 'empresa',
         'codigo', 'programa', 'agua', 'garrafa']

nome = input('Digite seu nome: ')
print(f'Olá {nome}, vamos começar o jogo da forca! Boa sorte. \n')

#pega uma palavra aleatória da lista de palavras criada
chosen_word = random.choice(words)
ramaining_letters = set(chosen_word)
failed_guess = 0


while any(ramaining_letters):
    try:
        guess = input('\nDigite uma letra: ')
        ramaining_letters.remove(guess)
        hidden_word = " ".join(
            "_" if letter in ramaining_letters else letter for letter in chosen_word)
        print(hidden_word)
        if not any(ramaining_letters):
            print(f'Parabéns {nome}, você ganhouuu!')
    except KeyError:
        failed_guess += 1
        if failed_guess == 1:
            print("   +---+")
            print("   O   |")
            print("       |")
            print("       |")
            print("      ===")
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
