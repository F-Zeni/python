def exibir_menu() -> None:
    print("""
    M E N U
    =========================
    0 - SAIR
    1 - Cadastrar Funcionário
    2 - Consultar Funcionário
    3 - Editar Funcionário
    4 - Excluir Funcionário
    5 - Listar Funcionários

""")
    
def verif_funci(d: dict, funci: str) -> bool:
    return funci in d

def verif_dicionario_vazio(d: dict) -> bool:
    if len(d) == 0:
        return True
    return False

def solic_funci() -> str | float:
    nome = input("Nome....: ").title()
    salario = float(input("Salario.: "))

    return (nome, salario)


def cadastrar_funci(d: dict, funci: str) -> None:

    v = solic_funci()

    d[funci] = {
        "nome": v[0],
        "salario": v[1]
    }
    print("Funcionário cadastrado")

def consultar_funci(d: dict, funci: str) -> None:
    if verif_funci(d, funci):
        func = d[funci]
        print(f"""
CPF.....: {funci}
Nome....: {func['nome']}
Salário.: {func['salario']}
""")
        print(23 * "-")
    else:
        print("Funcionário não encontrado.")
        print(23 * "-")

def editar_funci(d: dict, funci: str) -> None:
    consultar_funci(d, funci)

    v = solic_funci()

    d[funci] = {
        "nome": v[0],
        "salario": v[1]
    }

    print(23 * "-")
    print("Funcionário atualizado com sucesso!")

def excluir_funci(d: dict, funci: str) -> None:
    d.pop(funci)

def listar_funci(d: dict, funci: str) -> None:

    print(f"{'CPF': <14} {'NOME':<21} {'SALARIO'}")
    print(52 * "=")

    for k, funci in d.items():
        print(f"{k:>12} | {funci['nome']:<18} | R$ {funci['salario']:>8.2f}")
        print(52 * "=")