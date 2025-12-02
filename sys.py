from universidade import UFC
from campus import Campus
from curso import Curso

def menu_cursos(campus):
    while True:
        print(f"\n--- Gerenciar cursos do campus {campus.nome} ---")
        print("1 - Cadastrar curso")
        print("2 - Listar cursos")
        print("3 - Atualizar curso")
        print("4 - Remover curso")
        print("0 - Voltar ao menu de campus")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            codigo = input("Código do curso (ex: SI, MED, DIR): ")
            if campus.buscar_curso(codigo):
                print("Já existe um curso com esse código!")
                continue
            nome = input("Nome do curso: ")
            tipo = input("Tipo do curso (Bacharelado/Licenciatura/Tecnológico): ")
            curso = Curso(codigo, nome, tipo)
            campus.adicionar_curso(curso)
            print("Curso cadastrado com sucesso!")

        elif opcao == "2":
            print(f"\n--- Cursos do campus {campus.nome} ---")
            if not campus.cursos:
                print("Nenhum curso cadastrado.")
            else:
                for curso in campus.listar_cursos():
                    print(curso)

        elif opcao == "3":
            codigo = input("Informe o código do curso a ser atualizado: ")
            curso = campus.buscar_curso(codigo)
            if not curso:
                print("Curso não encontrado.")
            else:
                print(f"Curso atual: {curso}")
                novo_nome = input("Novo nome (ou deixe em branco para manter): ")
                novo_tipo = input("Novo tipo (ou deixe em branco para manter): ")
                curso.atualizar(
                    novo_nome if novo_nome.strip() != "" else None,
                    novo_tipo if novo_tipo.strip() != "" else None
                )
                print("Curso atualizado com sucesso!")

        elif opcao == "4":
            codigo = input("Informe o código do curso a ser removido: ")
            if campus.remover_curso(codigo):
                print("Curso removido com sucesso!")
            else:
                print("Curso não encontrado.")

        elif opcao == "0":
            break
        else:
            print("Opção inválida, tente novamente.")


def menu_principal():
    ufc = UFC()

    while True:
        print("\n====== SISTEMA UFC ======")
        print("1 - Cadastrar campus")
        print("2 - Listar campus")
        print("3 - Atualizar campus")
        print("4 - Remover campus")
        print("5 - Gerenciar cursos de um campus")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                codigo = int(input("Código do campus (número): "))
            except ValueError:
                print("Código inválido! Use apenas números.")
                continue

            if ufc.buscar_campus(codigo):
                print("Já existe um campus com esse código!")
                continue

            nome = input("Nome do campus: ")
            cidade = input("Cidade do campus: ")
            campus = Campus(codigo, nome, cidade)
            ufc.adicionar_campus(campus)
            print("Campus cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- Lista de campi da UFC ---")
            if not ufc.campi:
                print("Nenhum campus cadastrado.")
            else:
                for campus in ufc.listar_campi():
                    print(campus)

        elif opcao == "3":
            try:
                codigo = int(input("Informe o código do campus a ser atualizado: "))
            except ValueError:
                print("Código inválido!")
                continue

            campus = ufc.buscar_campus(codigo)
            if not campus:
                print("Campus não encontrado.")
            else:
                print(f"Campus atual: {campus}")
                novo_nome = input("Novo nome (ou deixe em branco para manter): ")
                nova_cidade = input("Nova cidade (ou deixe em branco para manter): ")

                campus.atualizar(
                    novo_nome if novo_nome.strip() != "" else None,
                    nova_cidade if nova_cidade.strip() != "" else None
                )

                print("Campus atualizado com sucesso!")

        elif opcao == "4":
            try:
                codigo = int(input("Informe o código do campus a ser removido: "))
            except ValueError:
                print("Código inválido!")
                continue

            if ufc.remover_campus(codigo):
                print("Campus removido com sucesso!")
            else:
                print("Campus não encontrado.")

        elif opcao == "5":
            try:
                codigo = int(input("Informe o código do campus para gerenciar seus cursos: "))
            except ValueError:
                print("Código inválido!")
                continue

            campus = ufc.buscar_campus(codigo)
            if not campus:
                print("Campus não encontrado.")
            else:
                menu_cursos(campus)

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu_principal()