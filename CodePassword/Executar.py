import Funcoes as f

print ("O que você deseja fazer?")
print ("Para codificar uma senha, digite 1.")
print ("Para descodificar uma senha, digite 2.")

opcao = int(input("Responda: "))

if opcao == 1:
    print ("Digite sua senha: ")
    senha = str(input())
    print ("Codificada: ",f.codificar(senha))
elif opcao == 2:
    print ("Digite a senha codificada: ")
    codificada = str(input())
    print ("Sua Senha é: ", f.descodificar(codificada))
else:
    print ("Opção invalida!")