import csv
import os.path
tipos = ['Provas', 'Trabalhos', 'Estudos']
# tipoEntrada = type str
# descrição = type str
# dataEvento = type str
# registros = open("eventos.txt", "w")
# print("----OPÇÕES----")
# for i in range(0,3):
# print("Adicionar uma atividade de",tipos[i], "-> digite", i)
# Login - um arquivo para senhas e outro para usuários
newPassword = ""
def login():
    print('------ Instruções para o seu login no primeiro acesso: ------\n Usuário: digite o seu CPF sem pontos ou caracteres, apenas o número, \n Senha: digite a sua senha ou no caso de primeiro acesso digite "alunoEcomp"\n')
    if os.path.isfile("firstAcess.csv"):
        user = input("Usuário: ")
        with open('firstAcess.csv', 'r', newline='') as acessFile:
            csv_reader = csv.reader(acessFile, delimiter=',')
            csv_reader.__next__()
            for row in csv_reader:            
              if user != row[0]:
                print("CPF não cadastrado")
              else:
                if not os.path.isfile("passwords.csv"):
                    newPassword = (input("Digite uma nova senha: ")) 
                    with open('passwords.csv', 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(["Users", "Senhas"])
                        writer.writerow([user,newPassword]) 
                    file.close
                else: 
                    newPassword = (input("Senha: "))
                    with open('passwords.csv', 'r', newline='') as csv_file:
                        csv_reader = csv.reader(csv_file, delimiter=',')
                        csv_reader.__next__()
                        for row in csv_reader:
                            if newPassword == row[1]:
                                print("ok")
                            else:
                                print("Você digitou a senha errada")
    else: 
        print("else")
        user = input("Usuário: ")
        password = (input("senha: "))
        if password == "alunoEcomp":  
            with open('firstAcess.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Users", "Senhas"])
                writer.writerow([user,password]) 
                print("sucess") 
        else: 
            print("você digitou a senha errada")
login()



 