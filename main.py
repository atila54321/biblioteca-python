livros = []

while True:
    print("\n==== SISTEMA DE BIBLIOTECA ====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Remover livro")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "":
        print("❌ Digite uma opção!")
        continue

    if opcao == "1":
        titulo = input("Título do livro: ").strip()

        if titulo == "":
            print("❌ O título não pode ficar vazio!")
            continue

        autor = input("Autor do livro: ").strip()

        if autor == "":
            print("❌ O autor não pode ficar vazio!")
            continue

        livro = {
            "titulo": titulo,
            "autor": autor,
            "emprestado": False
        }

        livros.append(livro)

        print("✅ Livro cadastrado com sucesso!")

    elif opcao == "2":
        print("\n==== LIVROS CADASTRADOS ====")

        if len(livros) == 0:
            print("Nenhum livro cadastrado.")
        else:
            for livro in livros:
                status = "Emprestado" if livro["emprestado"] else "Disponível"

                print(
                    f"Título: {livro['titulo']} | "
                    f"Autor: {livro['autor']} | "
                    f"Status: {status}"
                )

    elif opcao == "3":
        titulo_busca = input("Digite o título do livro: ").strip()

        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo_busca.lower():

                status = "Emprestado" if livro["emprestado"] else "Disponível"

                print(
                    f"Título: {livro['titulo']} | "
                    f"Autor: {livro['autor']} | "
                    f"Status: {status}"
                )

                encontrado = True
                break

        if not encontrado:
            print("❌ Livro não encontrado.")

    elif opcao == "4":
        titulo = input("Digite o título do livro: ").strip()

        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo.lower():

                encontrado = True

                if livro["emprestado"]:
                    print("❌ Este livro já está emprestado.")
                else:
                    livro["emprestado"] = True
                    print("✅ Livro emprestado com sucesso!")

                break

        if not encontrado:
            print("❌ Livro não encontrado.")

    elif opcao == "5":
        titulo = input("Digite o título do livro: ").strip()

        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo.lower():

                encontrado = True

                if not livro["emprestado"]:
                    print("❌ Este livro já está disponível.")
                else:
                    livro["emprestado"] = False
                    print("✅ Livro devolvido com sucesso!")

                break

        if not encontrado:
            print("❌ Livro não encontrado.")

    elif opcao == "6":
        titulo_remover = input("Digite o título do livro para remover: ").strip()

        encontrado = False

        for livro in livros:
            if livro["titulo"].lower() == titulo_remover.lower():

                livros.remove(livro)
                encontrado = True

                print("✅ Livro removido com sucesso!")
                break

        if not encontrado:
            print("❌ Livro não encontrado.")

    elif opcao == "7":
        print("Encerrando sistema...")
        break

    else:
        print("❌ Opção inválida!")