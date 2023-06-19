# CodePassword
#Portugues
Olá, este projeto foi desenvolvido para encriptar senhas para usuários que gostariam de guarda-las de alguma forma com segurança.
Utilizei um dicionário para que seja utilizado diversos caracteres durante a encriptação. Este dicionário poderia ser alterado de acordo com a necessidade do usuário.

Existem alguns pontos de segurança que ainda precisam ser desenvolvidos, como por exemplo se alguém tentar descobrir este algoritmo com tentativas utilizando a contagem de caracteres para descrobrir o dicionário, pode chegar próximo à codificação. Porém fiz um teste utilizando a Open Ai fornecendo algumas sequencias com os retornos para que a inteligência artificial tentasse descobrir o algoritmo e mesmo assim ela não foi capaz.

Ainda é preciso desenvolver um loyout ou view utilizando a PySimpleGUI.

No arquivo executar, é oferecido duas opções ao usuário:
Codificar uma senha
Descodificar uma Senha.

Na primeira opção, O usuário vai digitar sua senha e retornará sua senha encriptada.
Na segunda opção, o usuário vai digitar o codigo da sua senha e retornará sua senha.

Exemplo de execução:
O que você deseja fazer?
Para codificar uma senha, digite 1.   
Para descodificar uma senha, digite 2.
Responda: 1
Digite sua senha:
1234abcd
Codificada:  R7EWQ568

O que você deseja fazer?
Para codificar uma senha, digite 1.
Para descodificar uma senha, digite 2.
Responda: 2
Digite a senha codificada:
R7EWQ568
Sua Senha é:  1234abcd

Ensglish
Hello, this project was developed to encrypt passwords for users who would like to keep them safe somehow.
I used a dictionary so that different characters are used during encryption. This dictionary could be changed according to the user's needs.

There are some security points that still need to be developed, for example if someone tries to discover this algorithm with attempts using the character count to discover the dictionary, it can come close to encoding. However, I did a test using Open Ai providing some sequences with the returns so that the artificial intelligence could try to discover the algorithm and even then it was not able to.

You still need to develop a loyout or view using PySimpleGUI.

In the run file, the user is offered two options:
encode a password
Decode a Password.

In the first option, the user will enter his password and will return his encrypted password.
In the second option, the user will enter his password code and will return his password.

Execution example:
What do you want to do?
To encode a password, type 1.
To decode a password, type 2.
Answer: 1
Type your password:
1234abcd
Encoded: R7EWQ568

What do you want to do?
To encode a password, type 1.
To decode a password, type 2.
Answer: 2
Enter the encoded password:
R7EWQ568
Your Password is: 1234abcd
