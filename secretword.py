"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

print('Jogo da Palavra secreta.')

word = 'jogo'
letras_acertadas = ''
num_tentativas = 0

while True:
    letra_digitada = input('Digite a letra: ')
    num_tentativas += 1
    
    if len(letra_digitada) > 1:
         print('Digite somente uma letra.')
         continue
    
    if letra_digitada in word:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in word:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == word:
        os.system("cls")
        print('Você acertou!')
        print(f'A palavra era: {word}')
        print(f'Tentativas: {num_tentativas}')
        letras_acertadas = ''
        num_tentativas = 0
        
        sair = input('Quer sair? [s]im\n').lower().startswith('s')
        if sair is True:
         break