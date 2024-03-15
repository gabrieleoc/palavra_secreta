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
print('Jogo da Palavra secreta.')

word = 'jogo'
n = 0
letra = word[n]
ast = '*'* len(word)

while True:
    enter = input('Digite a letra: ')
    
    if len(enter) > 1:
        print('Digite somente uma letra.')
        continue
    
        
    sair = input('Quer sair? [s]im\n').lower().startswith('s')
    if sair is True:
        print(f'A palavra secreta era {word}.')
        break
        