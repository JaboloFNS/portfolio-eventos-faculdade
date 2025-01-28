#Importando o módulo colorama para melhorar a visibilidade dos menus e das mensagens de erro
from colorama import init, Fore, Back
init(autoreset=True)

def pause():
    #Função destinada a pausar o sistema em determinados pontos.
    input ("Pressione a tecla ENTER para retornar...")

#------------------------------------------------REFERENTE AO ACESSO PERMITIDO À ALUNOS DA INSTITUIÇÃO------------------------------------------
aluno = {
    #Dentro desse dicionário o número identificador equivale ao número do RA do aluno, 
    #a partir dele tempos acesso ao restante das informações.
    "001":{ "Nome": "Ednaldo Pereira", "Nascimento": "15/01/11967", "Curso": "ADS", "Senha": "0123"},
    "002":{ "Nome": "Fernanda Rodrigues", "Nascimento": "28/11/1992", "Curso": "GTI", "Senha": "456"},
    "003":{ "Nome": "Rodrigo Amadeu", "Nascimento": "25/04/2001", "Curso": "ADM", "Senha": "789"}
}

def acesso_aluno():
    #Com a opção '1' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como aluno da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais inseridas condizem com os dados de alunos que possuímos armazenados.
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.YELLOW}--------- ACESSO ALUNO CADASTRADO -----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    for i in range(3,0,-1):
        #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
        #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
        ra_aluno_acesso = str(input(f"{Fore.YELLOW}Ensira seu RA: "))
        if len(ra_aluno_acesso) != 3  or not ra_aluno_acesso.isdigit():
            print(f"{Fore.RED}Erro: O número do RA é composto por 3 dígitos. Tentativas de login restantes: {i-1}")
            continue
        senha_aluno_acesso = str(input(f"{Fore.YELLOW}Insira sua senha: "))

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
    #Uma vez logado, o aluno tem acesso a essa tela que lista os eventos disponíveis e dá a opção de se inscrever em um deles.
    #Após a inscrição em um dos eventos disponíveis, é questionado se deseja se inscrever em mais um.
    print(f"{Fore.BLUE}------------------------------------------------------")
    print(f"{Fore.YELLOW}--------- PORTAL DO ALUNO - GRANDES EVENTOS ----------")
    print(f"{Fore.BLUE}------------------------------------------------------","\n \n")
    lista_eventos()
    print(f"{Fore.YELLOW}---------------------------------------------")
    resposta = input("Deseja se cadastrar em um evento? [s/n]: ")
    resposta = resposta.lower()
    if resposta == "s" and len(resposta) == 1:
        inscricao_aluno_evento()
    pause()

#--------------------------------- REFERENTE AO ACESSO PERMITIDO À STAFFS DA INSTITUIÇÃO ----------------------------
staff = {
    #Dentro desse dicionário o número identificador equivale à um código nomeado como "Registro de STAFF" para membros docentes da faculdade,
    # o código é composto por uma letra e dois numerais para diferenciação dos RAs dos alunos que possuem 3 digitos numerais.
    "S01":{ "Nome": "Fabrício José", "Nascimento": "09/11/1968", "Cargo": "Professor", "Disciplina":"Matemática Financeira", "Senha": "123"},
    "S02":{ "Nome": "Elizeu Pereira", "Nascimento": "25/08/1977", "Cargo": "Professor", "Disciplina":"Lógica Computacional", "Senha": "456"},
    "S03":{ "Nome": "Júlia Vasconcelos", "Nascimento": "01/01/2002", "Cargo": "Professor", "Disciplina":"Agile Methods", "Senha": "789"}}

def acesso_staff():
    #Com a opção '2' selecionada no menu inicial, essa função é chamada para realizar o login do usuário como staff da Unifecaf.
    # O Código ira buscar dentro do sistema se as credenciais condizem com os dados que possuímos armazenados.
    print(f"{Fore.BLUE}---------------------------------------------")
    print(f"{Fore.MAGENTA}-------- ACESSO STAFF CADASTRADO ----------")
    print(f"{Fore.BLUE}---------------------------------------------","\n")

    #Dentro desse FOR construímos a possibilidade de tentar logar-se 3 vezes, uma vez atingido o limite, retorna ao menu inicial.
    #Também temos validações de inserção de dados, retornando mensagens de erros de acordo.
    for i in range(3,0,-1):
        re_staff_acesso = str(input(f"{Fore.MAGENTA}Insira seu Registro de STAFF: "))
        re_staff_acesso = re_staff_acesso.upper()
        if len(re_staff_acesso) != 3 and not re_staff_acesso.startswith("S"):
            print(f"{Fore.RED}Erro: O código do Registro de Staff exige 3 caracteres. Tentativas de login restantes: {i-1}")
            continue
        re_staff_senha = str(input(f"{Fore.MAGENTA}Insira sua senha: "))

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

def alternativas_staff(opcao_staff):
    match opcao_staff:
        case "1":
            lista_eventos(exibir_alunos_cadastrados=True)
            print("\n")
            pause()
            menu_staff()
        case "2":
            print("Adicionar Evento...")
            adicionar_eventos()
        case "3":
            print("Atualizar Evento...")
            #atualizar_evento()
        case "4":
            print ("Excluir Evento...")
            #excluir_evento()
        case "0":
            print("Saindo...")
            menu_inicial()
        case _:
            print(f"{Fore.RED}Opção inválida. Reveja as opções disponíveis e tente novamente.")
    
def menu_staff():
    #O Menu de membros da Staff é mais complexo do que dos alunos, tendo diversas opções de gerenciamento de eventos disponíveis.
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
    alternativas_staff(opcao_staff)

#--------------------------------- REFERENTE AO ARMAZENAMENTO E GERENCIAMENTO DE EVENTOS ------------------------------

eventos = { "1":{"Descrição": "Workshop - Lógica Computacional com Python", "Data-inicio": "25/02/2025 às 08:00",
    "Data-fim": "25/02/2025 às 12h", "Professor":"Irineu da Silva Sauro","Local":"Campus Centro - Lab 1", "Vagas Disponíveis": 18,
    "Alunos Cadastrados": ["003","002"]},
    "2":{"Descrição": "Workshop - Banco de Dados Relacionais com MySQL Server", "Data-inicio": "24/03/2025 às 08:00",
    "Data-fim": "24/03/2025 às 12:00", "Professor":"Joel Santana","Local":"Campus Centro - Lab 2", "Vagas Disponíveis": 49,
    "Alunos Cadastrados": ["003"]},
    "3":{"Descrição": "Palestra - Desenvolvimento Pessoal e Empregabilidade", "Data-inicio": "27/04/2025 às 08:00",
    "Data-fim": "27/04/2025 às 10:00", "Professor":"Maria Gadu","Local":"Campus Taboão - Lab 11", "Vagas Disponíveis": 50,
    "Alunos Cadastrados": []},
}

cont_id_evento = len(eventos) + 1


def lista_eventos (exibir_alunos_cadastrados=False):
    #Essa função lista cada um dos eventos disponíveis com seus dados informativos.
    #Foi inserido uma validação de dados que permite imprimir mais ou menos informações dependendo de que função chamou a lista_eventos(),
    #se ela foi chamada a partir de um login de alunos, a chave "Alunos Cadastrados" não é impressa, apenas se for chamado por um login Staff
    print(f"{Fore.GREEN}--------- EVENTOS DISPONÍVEIS ----------")
    for id_evento, dados_evento  in eventos.items():
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"Código do Evento: {id_evento}")
        for chave, valor in dados_evento.items():
            if chave == "Alunos Cadastrados":
                if exibir_alunos_cadastrados:
                    print(f"{Fore.YELLOW}{chave}: ")
                    if valor:
                        for ra in valor:
                            print(f"- RA: {ra} ")
                    else:
                        print(f"{Fore.RED}Nenhum aluno cadastrado no evento")
                else:
                    continue
            else:
                print (f"{chave}: {valor}")

def adicionar_eventos():
    global cont_id_evento
    print(f"{Fore.YELLOW}---------------------------------------------")
    print("Vamos agendar seu novo evento. Adicione as informações a seguir:")

    descricao_novo = str(input("Adicione a descrição de seu evento: (Tipo do evento) - (Título dod Evento) \n"))
    data_inicio_novo = input("Ensira a data de início do evento: (DIA/MÊS/ANO HR:MIN) ")
    data_fim_novo = input("Ensira a data do final do evento:(DIA/MÊS/ANO HR:MIN)")
    professor_novo = str(input("Ensira o nome do responsável pelo evento (Professor ou Palestrante): "))
    local_novo = str(input("Ensira o local onde será realizado o evento: "))
    vagas_novo = int(input("Ensira a quantidade de vagas disponíveis para participar do evento: "))

    novo_evento = {
        "Descrição": descricao_novo,
        "Data-inicio": data_inicio_novo,
        "Data-fim": data_fim_novo,
        "Professor": professor_novo,
        "Local": local_novo,
        "Vagas Disponíveis": vagas_novo,
        "Alunos Cadastrados": []
    }

    eventos [str(cont_id_evento)] = novo_evento
    if eventos [str(cont_id_evento)] == novo_evento:
        print(f"{Fore.YELLOW}---------------------------------------------")
        print(f"{Fore.GREEN}Novo evento agendado com sucesso!")
        for id_evento, dados_evento  in eventos.items():
            print(f"Código do Evento: {id_evento}")
            for chave, valor in dados_evento.items():
                if chave == cont_id_evento:
                    print(f"{chave}: {valor}")
                    if "Alunos Cadastrados" in dados_evento:
                        if not dados_evento["Alunos Cadastrados"]:
                            print("Ainda não há cadastros.")




    




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
    opcao = int(input("Insira o número correspondente ao seu perfil: "))
    if opcao == 1:
        acesso_aluno()
    elif opcao == 2:
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