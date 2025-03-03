"""
- Usa-se o print'...' para fazer o programa escrever algo

- Usa-se ... = X para associar algo a algo

- Usa-se # antes de uma linha de comandos para fazer o python entender que aquilo é somente uma observação e não
executa-los

- Usa-se ...=input('...') para fazer uma pergunta e associar a resposta ao ...

- Usa-se + para somar duas coisas e , para juntar (O + também pode juntar se houver aspas)

* print('...' , variável) junta uma frase pronta com algo variável já programado
* ... =print 'Exemplo' faz com que a frase dita após uma pergunta escreva algo

-Operações: + mais , - menos , * vezes , / dividido , ** potência , // divisão inteira , **(1/2) raiz quadrada.
*Para somar dois valores vc tem que colocar int (de inteiro) antes dos input dos números
* O símbolo % não representa a operação porcentagem e sim o módulo de algo (O resto)
Ordem de precedência: 1°() ; 2°* ; 3°*,/,//,% ; 4° + e -

Na biblioteca math:
*A função sqrt da biblioteca math serve para tirar a raiz quadrada 
*A função math.cos mostra o cosseno, math.sin o seno e math.tan a tangente
*A função radians transforma o número em radianos

-Você pode fazer algo str se repetir multiplicando ele por um número (Ex: 'Oi' * 5)

-Pode-se escrever em alguma quantidade de caracteres usando {:.20} com as {} significando algo no forma de .format{}
* < > ^ servem para informar onde a palavra ficará

-Pode-se definir a quantidade de casas depois da vírgula com {:.2f} por exemplo

-Usa-se /n para quebrar as linhas e end=' ' para não quebrar a linha (juntar com a linha de baixo)

-Tipos primitivos: int() números inteiros, float() números quebrados(reais), bool() true ou false, str() string

-Para importar alguma biblioteca usa-se import ... já para importar algo específico da biblioteca usa-se from ...
import ...

*Quando se importa com o from não precisa colocar o nome da biblioteca

-Uma lista é criada com []

-Na biblioteca random: 
*random.shuffle(...) é colocado só em alguma linha e embaralha o ...
*random.choice(...) escolhe algum da lista já feita anteriormente com []

-Para executar uma música podemos utilizar o programa mixer da biblioteca pygame. Utilizamos mixer.init() para iniciar
o programa, mixer.load.music('Nome da música com .mp3') e mixer.play().
*É necessário manter o programa funcionando para a música tocar.Ex: executar um input('Qual é a música?'), por exemplo.

-Manipulando textos:
Os textos ocupam um espaço de micro-memória no PC sendo contados do 0, uma frase normal está na mesma ''família'' de
micro-memórias
* Índice: Número sequencial de 0 até n;
* Para fatiar uma frase e escolher uma letra se usa frase[3] por exemplo.
* Para mostrar a frase do início ao 3 caractere por exemplo, usa-se print(frase[:3]), lembrando que o primeiro caractere
sempre é o 0
* Para mostrar do 3 caractere ao final usa-se print(frase[3:])
* O comando [::2] por exemplo, vai mostrar do início ao final pulando de 2 em 2
* O comando [3::2] por exemplo, serve para o Python escrever do 3 ao final pulando de 2 em 2, mostrando o 2
(Tipo: ABCDEFGHI ficaria DFH)
* O comando len(frase) serve para indicar a quantidade de caracteres na frase já atribuida por um input, por exemplo
* O comando frase.count('o') por exemplo, serve para o python contar quantas vezes o ''o'' apareceu na frase
* No fatiamento o último valor sempre é ignorado pelo python.
* O comando frase.find('deo') serve para indicar onde começou o deo na frase ''curso em video'' por exemplo, sendo igual
a 11
* Quando mandamos o python procurar algo que não existe na frase ele te da como resultado -1, indicando que aquilo não
está na frase. Exemplo: print(frase.find('cagão') da frase cherapeido não existe, logo, ele vai ter como resultado -1
* O operador in serve para indicar se existe aquela parte já associada na frase também já associada.
Ex: print(parte in frase)
* O comando frase.replace('python , 'android') por exemplo, serve para substituir o python da frase já associada por
android. Ex: print(frase.replace('python, 'android') da frase já associada: curso em vídeo python
* O comando frase.upper() serve para deixar todas as letras da frase, já associada, mas, letras já em maiúsculas
continuam em maiúsculas
* O comando frase.lower() deixa as letras maiúsculas em minúsculas, minúsculas permanecem em minúsculas
* Dentro da string:
 - \t -> Adiciona um tab dentro da string.
 - \n -> Pula/adiciona uma linha para baixo na string.
* A função frase.capitalize() serve para deixar todos os caracteres da frase já associada para minúsculo e deixar
 somente a primeira letra em maiúsculo
* O comando frase.title() serve para deixar as letras após espaços em maiúsculas
* A função frase.strip() remove todos os espaços inúteis, os entre palavras e letras continuam.
* A função frase.rstrip() retira os espaços da direita, final do texto
* A função frase.lstrip() retira os espaços da esquerda, início do texto
* A função frase.split() serve para separar as palavras em diferentes famílias de micro-memórias
* A função '-'.join(frase) por exemplo, serve para juntar famílias de micro-memórias com o que esta entre as aspas
* A função print com (3 vezes ' " ') serve para o python escrever do mesmo modo que foi escrito, com quebras de linhas,
bom para textos grandes.
* Quando usamos o comando frase.split() associado a dividido por exemplo, em uma frase já associada, o comando
print(dividido[0]) mostrará a primeira família de micro-memórias, 1 a segunda, 2 a terceira e assim em diante
"""

frase = "Curso em Vídeo Python"

# DICAS EXCLUSIVAS!!!
# Printar um texto grande:
print("""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o 
Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), 
title(), strip(), junção com join().""")
# Usar múltiplos comandos ao mesmo tempo:
print(frase.upper().count('O'))

dividido = frase.split()
print(dividido[2][3])
# Console: 'e' -> Primeiro ele divide a frase em 4. dividido[2][3] sendo '2' a terceira palavra: Vídeo, e '3' a quarta
# letra.


# ***** Fatiamento -> *****
# 1º frase[n] printa o n-ésimo caractere
print(frase[9])
# Console: "V"

# 2º frase[n:m] -> printa do n-ésimo caractere até m-1 ésimo caractere
print(frase[9:13])
# Console: "Víde" -> 13 - 9 = 4 caracteres

print(frase[9:21])
# Console: "Vídeo Python" -> vai até o 21-1 = 20º caractere

# 3º Ex: print(frase[n:m:k]) printa de 'n' até 'm-1' pulando de 'k' em 'k' caracteres
print(frase[9:21:2])
# Console: "VdoPto"

# 4º frase[:m] printa do começo ('0' caractere) até m-1 caractere
print(frase[:5])
# Console: "Curso"

# 5º frase[n:] printa de 'n' até o último caractere
print(frase[15:])
# Console: "Python"

# 6º frase[n::k] printa de 'n' até o último caractere pulando de 'k' em 'k'
print(frase[9::3])
# Console: "VePh"


# ***** Análise -> *****
# 1º len[frase] -> 'len()' vem de 'length' = comprimento; Mostra a quantidade de caracteres de uma string.
print(len(frase))
# Console: "21"

# 2.1º frase.count('p') -> 'p' é o caractere em que é contado quantas vezes aparece na string.
print(frase.count('o'))
# Console: "3" -> Existem 3 caracteres com a letra 'o'

# 2.2º 'Count com fatiamento'; frase.count('p', n, m) -> Conta quantas vezes existe o caractere 'p' de 'n' até
# 'm-1' dentro da string.
print(frase.count('o', 0, 13))
# Console: "1" -> Existe apenas 1 'o' dentre os caracteres 0 e 13 - 1 = 12.

# 3º find('palavra') -> Procura e mostra a posição da primeira letra em que foi encontrado a palavra 'palavra'
# Caso falso, retorna o valor '-1'.
# rfind -> Mostra a posição da última 'palavra' encontrada
print(frase.find('deo'))
print(frase.find('Android'))
print(frase.rfind('o'))
# Console: "11" -> '11' é onde começa o 'd', e termina em '13'.
# Console: "-1" -> Pois não existe uma cadeia correspondente a 'Android' na frase.
# Console: "19" -> '19' é a última

# 4º Condição: "'palavra' in frase"
# Retorna verdadeiro/falso se existe 'palavra' na frase.
print('Curso' in frase)
# Console: 'True' -> Verdadeiro. Existe a palavra 'Curso' dentro da frase.


# ***** Transformação -> *****
# 1º Replace:   frase.replace('Python', 'Android') -> Substitui a 'string_1' por 'string_2'
print(frase.replace('Python', 'Android'))
# Console: 'Curso em Vídeo Android' -> Foi substituído a palavra 'Python' por 'Android'

# 2º Upper e Lower:
# frase.upper() -> Transforma todas as letras minúsculas em maiúsculas.
# frase.lower() -> Transforma todas as letras maiúsculas em minúsculas.
print(frase.upper())
print(frase.lower())
# Console: "CURSO EM VÍDEO PYTHON" e "curso em vídeo python" -> Funcionou como esperado.

# 3º Capitalize e Title:
# frase.capitalize() -> Deixa tudo minúsculo e coloca a primeira letra em maiúsculo.
# frase.title() -> Coloca cada letra de cada começo de uma palavra em maiúsculo.
print(frase.capitalize())
print(frase.title())
# Console: "Curso em vídeo python" -> para frase.capitalize()
# Console: "Curso Em Vídeo Python" -> para frase.title()

frase_1 = "   Aprenda Python  "
# 4º Strip:
# frase.strip -> Remove todos os espaços em brancos tanto no começo quanto no final.
# frase.rstrip -> Remove o espaço em branco apenas da direita.
# frase.lstrip -> Remove o espaço em branco apenas da esquerda.
print(frase_1.strip())
print(frase_1.rstrip())
print(frase_1.lstrip())
# Console: "Aprenda Python"
# Console: "   Aprenda Python"
# Console: "Aprenda Python  "


# ***** Divisão -> *****
# 1º Split:
# frase.split(separator, maxsplit) -> Faz a divisão das palavras entre espaços em branco e vira uma lista
"""
* separator -> Opcional. Especifica o separador para quando fazer uma divisão na string. Como padrão qualquer espaço 
em branco é um separador.
* maxsplit -> Opcional. Especifica quantas separações fazer. Como padrão é '-1', no qual são 'todas as ocorrências'.
"""
print(frase.split())
print(frase.split('em', 2))
print(frase.split(' ', 2))
print(frase.split(' ', 1))
# Console: "['Curso', 'em', 'Vídeo', 'Python']"
# Console: "['Curso ', ' Vídeo Python']"
# Console: "['Curso', 'em', 'Vídeo Python']"
# Console: "['Curso', 'em Vídeo Python']"

# 2º Join: 'caractere'.join(frase) -> Junta todos os elementos de 'frase' dentre eles o 'caractere'
frase = frase.split()
print('-'.join(frase))
# Console: "Curso-em-Vídeo-Python"








