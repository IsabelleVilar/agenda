import re

def validar_nome(nome):
    return nome.strip() != ''

def validar_telefone(telefone):
    telefone = telefone.replace(' ', '')
    if len(telefone) != 10:
        return False
    if not telefone.isdigit():
        return False
    return True
    
def validar_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

def salvar_contato(agenda):
    telefone = ''
    email = ''
    
    nome = input('Digite o nome: ')
    while not validar_nome(nome):
        print('Nome inválido. Por favor, insira um nome válido.')
        nome = input('Digite o nome: ')

    incluir_telefone = input('Deseja incluir telefone? (S/N): ').upper()
    if incluir_telefone == 'S':
        telefone = input('Digite o telefone no formato (XX)XXXX-XXXX - apenas números: ')
        while not validar_telefone(telefone):
            print('Telefone inválido. Por favor, insira um telefone válido.')
            telefone = input('Digite o telefone no formato (XX)XXXX-XXXX - apenas números: ')

    incluir_email = input('Deseja incluir email? (S/N): ').upper()
    if incluir_email == 'S':
        email = input('Digite o e-mail: ')
        while not validar_email(email):
            print('Email inválido. Por favor, insira um email válido.')
            email = input('Digite o e-mail: ')

    agenda[nome] = {'Telefone': telefone, 'Email': email}
    print('\nContato salvo com sucesso!')

def visualizar_contato_completo(agenda):
    print('Lista de contatos:')
    for i, (nome, info) in enumerate(agenda.items(), start=1):
        telefone = info.get('Telefone', '')
        email = info.get('Email', '')
        favorito = info.get('Favorito', False)
        
        favorito_str = " [✓] Favorito" if favorito else ''
        
        print(f'{i}. Nome: {nome}')
        print(f'   Telefone: {info['Telefone']}')
        print(f'   Email: {info['Email']}')
        print(f"  {favorito_str}")
    return

def visualizar_contato(agenda):
    print('Lista de contatos:')
    for i, (nome, info) in enumerate(agenda.items(), start=1):
        print(f'{i}. Nome: {nome}')
    return

def editar_contato(agenda):
    indice = int(input('Digite o índice do contato que deseja editar: '))
    if indice not in range (1, len(agenda) + 1):
        print('Não existe contato para o índice informado.')
        return
    
    contato = list(agenda.items())[indice - 1]
    nome = contato[0]
    info = contato[1]
            
    opcao_nome = input('Deseja alterar o nome? (S/N): ').upper()
    if opcao_nome == 'S':
        novo_nome = input('Digite o novo nome: ')
        while not validar_nome(novo_nome):
            print('Nome inválido. Por favor, insira um nome válido.')
            novo_nome = input('Digite o nome: ')
        agenda[novo_nome] = agenda.pop(nome)

    opcao_telefone = input("Deseja alterar o telefone? (S/N): ").upper()
    if opcao_telefone == "S":
        novo_telefone = input("Digite o novo telefone: ")
        while not validar_telefone(novo_telefone):
            print('Telefone inválido. Por favor, insira um telefone válido.')
            novo_telefone = input('Digite o telefone no formato (XX)XXXX-XXXX - apenas números: ')
        info['Telefone'] = novo_telefone

    opcao_email = input("Deseja alterar o email? (S/N): ").upper()
    if opcao_email == "S":
        novo_email = input("Digite o novo email: ")
        while not validar_email(novo_email):
            print('Email inválido. Por favor, insira um email válido.')
            novo_email = input('Digite o e-mail: ')
        info['Email'] = novo_email

    opcao_favorito = input("Deseja alterar como favorito? (S/N): ").upper()
    if opcao_favorito == 'S':
        if 'Favorito' in info and info['Favorito']:
            info['Favorito'] = False
            print(f"{nome} foi desmarcado como favorito.")
        else:
            info['Favorito'] = True
            print(f"{nome} foi marcado como favorito.")

def marcar_favorito(agenda):
    indice = int(input("Digite o índice do contato que deseja marcar/desmarcar como favorito: "))
    if indice not in range(1, len(agenda) + 1):
        print("Não existe contato para o índice informado.")
        return
    
    contato = list(agenda.items())[indice - 1]
    nome = contato[0]
    info = contato[1]

    favorito = info.get('Favorito', False)
    if favorito:
        print(f"{nome} já está marcado como favorito.")
        opcao = input("Deseja desmarcar como favorito? (S/N): ").upper()
        if opcao == 'S':
            info['Favorito'] = False
            print(f"{nome} foi desmarcado como favorito.")
    else:
        print(f"{nome} não está marcado como favorito.")
        opcao = input("Deseja marcar como favorito? (S/N): ").upper()
        if opcao == 'S':
            info['Favorito'] = True
            print(f"{nome} foi marcado como favorito.")

def visualizar_favoritos(agenda):
    favoritos = [contato for contato, info in agenda.items() if info.get('Favorito', False)]
    
    if favoritos:
        print("Contatos Favoritos:")
        for i, contato in enumerate(favoritos, start=1):
            print(f"{i}. Nome: {contato}")
    else:
        print("Nenhum contato marcado como favorito.")

def apagar_contato(agenda):
    indice = int(input("Digite o índice do contato que deseja apagar: "))
    if indice not in range(1, len(agenda) + 1):
        print("Não existe contato para o índice informado.")
        return

    contato = list(agenda.items())[indice - 1]
    nome = contato[0]

    opcao = input(f"Deseja realmente apagar o contato '{nome}'? (S/N): ").upper()
    if opcao == 'S':
        del agenda[nome]
        print(f"Contato '{nome}' apagado com sucesso.")

def menu():
    print('\nMenu da Agenda:')
    print('1. Salvar contato')
    print('2. Visualizar contatos cadastrados')
    print('3. Editar contato')
    print('4. Marcar/desmarcar contato como favorito')
    print('5. Ver contatos favoritos')
    print('6. Deletar contato')
    print('7. Sair')

def main():
    agenda = {}
    while True:
        menu()
        escolha = int(input('\nDigite a sua opção: '))
        if escolha == 1:
            salvar_contato(agenda)
        elif escolha == 2:
            visualizar_contato_completo(agenda)
        elif escolha == 3:
            visualizar_contato_completo(agenda)
            editar_contato(agenda)            
        elif escolha == 4:
            visualizar_contato(agenda)
            marcar_favorito(agenda)
        elif escolha == 5:
            visualizar_favoritos(agenda)
        elif escolha == 6:
            visualizar_contato(agenda)
            apagar_contato(agenda)
        elif escolha == 7:
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
    print('Programa finalizado!\n')

if __name__ == '__main__':
    main()
