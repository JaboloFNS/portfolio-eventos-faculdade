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
    "001":{ "Nome": "Ednaldo Pereira", "Nascimento": date(1987, 1, 5), "Curso": "ADS", "Senha": "0123"},
    "002":{ "Nome": "Fernanda Rodrigues", "Nascimento": date(1992, 11, 28), "Curso": "GTI", "Senha": "456"},
    "003":{ "Nome": "Rodrigo Amadeu", "Nascimento": date(2001, 4, 25), "Curso": "ADM", "Senha": "789"}
}

def acesso_aluno():
    #Com a opção '1' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como aluno da Unifecaf.
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


def inscricao_aluno_evento():
#Funcionalidade ainda não construída
 print()
        

def menu_aluno():
    print(f"{Fore.BLUE}------------------------------------------------------")
    print(f"{Fore.YELLOW}--------- PORTAL DO ALUNO - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}------------------------------------------------------","\n \n")
    lista_eventos()
    resposta = input("Deseja se cadastrar em um evento? [s/n]")
    resposta.lower()
    if resposta == "s" and len(resposta) == 1:
        inscricao_aluno_evento()
    
    pause()

#--------------------------------- REFERENTE AO ACESSO PERMITIDO À STAFFS DA INSTITUIÇÃO ----------------------------
staff = {
    #Dentro desse dicionário o número identificador equivale ao número do RA do aluno, 
    #a partir dele tempos acesso ao restante das informações.
    "S01":{ "Nome": "Fabrício José", "Nascimento": date(1968, 11, 9), "Cargo": "Professor", "Disciplina":"Matemática Financeira", "Senha": "123"},
    "S02":{ "Nome": "Elizeu Pereira", "Nascimento": date(1977, 8, 25), "Cargo": "Professor", "Disciplina":"Lógica Computacional", "Senha": "456"},
    "S03":{ "Nome": "Júlia Vasconcelos", "Nascimento": date(1999, 2, 17), "Cargo": "Professor", "Disciplina":"Agile Methods", "Senha": "789"}}

def acesso_staff():
    #Com a opção '2' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como staff da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais condizem com os dados que possuímos armazenados.
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.MAGENTA}-------- ACESSO STAFF CADASTRADO ----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
    #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
    for i in range(3,0,-1):
        re_staff_acesso = str(input(f"{Fore.MAGENTA}Ensira seu Registro de STAFF: "))
        if len(re_staff_acesso) != 3:
            print(f"{Fore.RED}Erro: O número do Registro de STAFF é composto por 3 dígitos. Tentativas de login restantes: {i-1}")
            continue
        re_staff_senha = str(input(f"{Fore.MAGENTA}Ensira sua senha: "))

        if re_staff_acesso in staff:
            staff_logado = staff[re_staff_acesso]
            if re_staff_senha == staff_logado["Senha"]:
                print("\n")
                print(f"{Fore.GREEN}Logado com sucesso. Bem vindo, {staff_logado["Nome"]}.")
                print("\n")
                menu_staff()
                return
            else:
                print(f"{Fore.RED}Senha incorreta. Tentativas de login restantes: {i-1}")
        else:
            print(f"{Fore.RED}RA não encontrado. Tentativas de login restantes: {i-1}")
    pause()

def menu_staff():
    print(f"{Fore.BLUE}----------------------------------------------------------")
    print(f"{Fore.MAGENTA}--------- GERENCIAMENTO STAFF - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}----------------------------------------------------------","\n \n \n")
    print("Opções de Gerenciamento: \n")
    print("1 - Visualizar Eventos")
    print("2 - Adicionar Evento")
    print("3 - Atualizar Evento Existente")
    print("4 - Excluir/Cancelar Evento")
    print("0 - Sair")
    opcao_staff = input("Digite o código númerico da opção desejada: ")




#--------------------------------- REFERENTE AO ARMAZENAMENTO E VISUALIZAÇÃO DE EVENTOS ------------------------------

eventos = { "1":{"Descrição": "Workshop - Lógica Computacional com Python", "Data-inicio":(2025,2,25,8,00),
    "Data-fim":(2025,2,25,12,00), "Professor":"Irineu da Silva Sauro","Local":"Campus Centro - Lab 1", "Vagas Disponíveis": 18,
    "Alunos Cadastrados": ["003","002"]},
    "2":{"Descrição": "Workshop - Banco de Dados Relacionais com MySQL Server", "Data-inicio":(2025,3,24,8,00),
    "Data-fim":(2025,3,24,12,00), "Professor":"Joel Santana","Local":"Campus Centro - Lab 2", "Vagas Disponíveis": 49,
    "Alunos Cadastrados": ["003"]},
    "3":{"Descrição": "Palestra - Desenvolvimento Pessoal e Empregabilidade", "Data-inicio":(2025,3,24,8,00),
    "Data-fim":(2025,3,24,12,00), "Professor":"Maria Gadu","Local":"Campus Taboão Centro - Lab 11", "Vagas Disponíveis": 50,
    "Alunos Cadastrados": []},
}


def lista_eventos ():
    print(f"{Fore.GREEN}--------- EVENTOS DISPONÍVEIS ----------")
    for id_evento, dados_evento  in eventos.items():
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"Código do Evento: {id_evento}")
        for chave, valor in dados_evento.items():
            if chave != "Alunos Cadastrados":
                print (f"{chave}: {valor}")




#------------------------------ REFERENTE AO MENU INICIAL ------------------------------------

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
    print("2 - Staff")
    print("0 - Sair")
    opcao = int(input("Ensira o número correspondente ao seu perfil: "))
    if opcao == 1:
        acesso_aluno()
    elif opcao == 2:
        print ("Olá, Staff")
        acesso_staff()
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