#Importando o módulo colorama para melhorar a visibilidade dos menus e possíveis mensagens de erro
from colorama import init, Fore, Back
init(autoreset=True)

from datetime import date, datetime

def pause():
    #Função destinada a pausar o sistema em determinados pontos.
    input ("Pressione a tecla ENTER para retornar...")

#------------------------------------------------REFERENTE AO ACESSO PERMITIDO À ALUNOS DA INSTITUIÇÃO------------------------------------------
aluno = {
    #Dentro desse dicionário o número identificador equivale ao número do RA do aluno, 
    #a partir dele tempos acesso ao restante das informações.
    "001":{ "Nome": "Ednaldo Pereira", "Nascimento": date(1987, 1, 5), "Curso": "ADS", "Senha": "04123759"},
    "002":{ "Nome": "Fernanda Rodrigues", "Nascimento": date(1992, 11, 28), "Curso": "GTI", "Senha": "01054764"},
    "003":{ "Nome": "Rodrigo Amadeu", "Nascimento": date(2001, 4, 25), "Curso": "ADM", "Senha": "47856124"}
}

def acesso_aluno():
    #Com a opção 01 selecionada no menu inicial, essa função é chamada para realizar o login do usuário como aluno da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais condizem com os dados de alunos que possuímos armazenados.
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.YELLOW}--------- ACESSO ALUNO CADASTRADO -----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
    #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
    for i in range(3,0,-1):
        ra_aluno_acesso = str(input(f"{Fore.YELLOW}Ensira seu RA: "))
        if len(ra_aluno_acesso) != 3  or not ra_aluno_acesso.isdigit():
            print(f"{Fore.RED}Erro: O número do RA é composto por 3 dígitos. Tentativas de login restantes: {i-1}")
            continue
        senha_aluno_acesso = str(input(f"{Fore.YELLOW}Ensira sua senha:"))

        if ra_aluno_acesso in aluno:
            aluno_logado = aluno[ra_aluno_acesso]
            if senha_aluno_acesso == aluno_logado["Senha"]:
                print("\n")
                print(f"{Fore.GREEN}Logado com sucesso. Bem vindo, {aluno_logado["Nome"]}.")
                print("\n")
                menu_aluno()
                return
            else:
                print(f"{Fore.RED}Senha incorreta. Tentativas de login restantes: {i-1}")
        else:
            print(f"{Fore.RED}RA não encontrado. Tentativas de login restantes: {i-1}")
    pause()


def menu_aluno():
    print(f"{Fore.BLUE}------------------------------------------------------")
    print(f"{Fore.BLUE}--------- PORTAL DO ALUNO - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}------------------------------------------------------","\n")
    pause()





def menu_inicial():
    #O Menu inicial é a primeira tela a ser mostrada quando o usuário abrir o sistema,
    #a partir dela ele terá duas opções de acesso disponíveis.
    print("\n")
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.BLUE}--------- UNIFECAF GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}---------------------------------------------\n")
    print("Acesse nossa plataforma para estar por dentro de todas as novidades! \n"),
    print("Você é: ")
    print("1 - Aluno")
    print("2 - Organizador de eventos")
    print("0 - Sair")
    opcao = int(input("Ensira o número correspondente ao seu perfil: "))
    if opcao == 1:
        acesso_aluno()
    elif opcao == 2:
        print ("Olá, organizador")
        # acesso_organizador()
    elif opcao == 0:
        print(f"{Fore.RED}----------------------------------------------")
        print(f"{Fore.RED}------ ACESSO ENCERRADO - VOLTE SEMPRE! ------")
        print(f"{Fore.RED}----------------------------------------------")
        exit(0)
    else:
        print(f"{Fore.RED}Opção inválida! Confira as opções disponíveis e tente novamente.")
        pause()
    menu_inicial()



menu_inicial()