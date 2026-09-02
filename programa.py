import os
os.system("cls")

from subalgoritmos import *

funcionarios = {}

while True:
    exibir_menu()
    escolha = input("Escolha: ")
    match escolha:
        case '0':
            break
        case '1':
            print("""
 CADASTRANDO FUNCIONÁRIO:
 ========================
 """)
            cpf = input("CPF.....: ")
            if verif_funci(funcionarios, cpf):
                print(23 * '-')
                print("Funcionário já existe!")
                print(23 * '-')
            else:
                cadastrar_funci(funcionarios, cpf)
        case '2':
            os.system("cls")
            print("""
CONSULTANDO FUNCIONÁRIO
=======================
""")
            cpf = input("CPF.....: ")
            consultar_funci(funcionarios, cpf)
        case '3':
            os.system("cls")
            print("Edite os campos:")
            print(23 * '-')
            cpf = input("CPF.....: ")
            editar_funci(funcionarios, cpf)
        case '4':
            os.system("cls")
            if verif_dicionario_vazio(funcionarios):
                print(23 * "-")
                print("Nenhum funcionário cadastrado!")
                print(23 * "-")

            print("""
EXCLUINDO FUNCIONÁRIO
---------------------
""")
            cpf = input("CPF.....: ")
            print(23 * "-")

            if not verif_funci(funcionarios, cpf):
                print("""
------------------------
FUNCIONÁRIO INEXISTENTE!
------------------------
""")
 
            resp = input("Confirme a exclusão do funcionário [S/N]?")
            if resp.upper() == 'S':
                excluir_funci(funcionarios, cpf)
                print("""
---------------------
FUNCIONÁRIO EXCLUÍDO!
---------------------
""")
            else:
                print("Exclusão cancelada...")

        case '5':
            funci = input("CPF.....: ")
            listar_funci(funcionarios, funci)
        case _:
            print("Informe uma opção válida!")

    input("Pressione alguma tecla para continuar...")