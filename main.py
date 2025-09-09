# main.py
from contatos_base import contatos_iniciais
import time
import re

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"{self.nome} - {self.telefone} - {self.email}"


agenda = []

# Domínios permitidos para e-mail
dominios_email = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

# --------------------------
# Funções de validação
# --------------------------
def validar_nome(nome):
    # Permite letras, espaços e acentuação
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome.strip()))

def validar_telefone(telefone):
    # Formato (XX) 9XXXX-XXXX
    return bool(re.fullmatch(r"\(\d{2}\) 9\d{4}-\d{4}", telefone.strip()))

def validar_email(email):
    # Verifica formato e domínio permitido
    match = re.fullmatch(r"([a-zA-Z0-9_.+-]+)@([a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email.strip())
    if match:
        dominio = match.group(2)
        return dominio in dominios_email
    return False

# --------------------------
# Funções principais
# --------------------------
def inserir_contato(nome, telefone, email):
    # Validações antes de inserir
    if not validar_nome(nome):
        print("Nome inválido! Apenas letras e espaços são permitidos.")
        return False
    if not validar_telefone(telefone):
        print("Telefone inválido! Use o formato (XX) 9XXXX-XXXX.")
        return False
    if not validar_email(email):
        print(f"E-mail inválido! Apenas domínios permitidos: {', '.join(dominios_email)}")
        return False

    contato = Contato(nome, telefone, email)
    agenda.append(contato)
    print("Contato adicionado com sucesso!\n")
    return True

def listar_contatos():
    if not agenda:
        print("Agenda vazia.\n")
    else:
        print("\n--- Lista de Contatos ---")
        for contato in agenda:
            print(contato)
        print()

def buscar_sequencial(nome):
    inicio = time.perf_counter()
    for contato in agenda:
        if contato.nome.lower() == nome.lower():
            fim = time.perf_counter()
            print(f"Busca sequencial levou {fim - inicio:.6f} segundos")
            return contato
    fim = time.perf_counter()
    print(f"Busca sequencial levou {fim - inicio:.6f} segundos")
    return None

def buscar_binaria(nome):
    agenda.sort(key=lambda contato: contato.nome.lower())
    inicio = time.perf_counter()
    esquerda, direita = 0, len(agenda) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if agenda[meio].nome.lower() == nome.lower():
            fim = time.perf_counter()
            print(f"Busca binária levou {fim - inicio:.6f} segundos")
            return agenda[meio]
        elif agenda[meio].nome.lower() < nome.lower():
            esquerda = meio + 1
        else:
            direita = meio - 1
    fim = time.perf_counter()
    print(f"Busca binária levou {fim - inicio:.6f} segundos")
    return None

# --------------------------
# Carregar contatos iniciais
# --------------------------
def carregar_contatos_iniciais():
    for c in contatos_iniciais:
        inserir_contato(c["nome"], c["telefone"], c["email"])

# --------------------------
# Função principal
# --------------------------
def main():
    carregar_contatos_iniciais()

    while True:
        print("=== Agenda Telefônica ===")
        print("1. Inserir contato")
        print("2. Listar contatos")
        print("3. Buscar contato (Sequencial)")
        print("4. Buscar contato (Binária)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            inserir_contato(nome, telefone, email)

        elif opcao == "2":
            listar_contatos()

        elif opcao == "3":
            nome = input("Digite o nome para buscar (sequencial): ")
            contato = buscar_sequencial(nome)
            print(f"Resultado: {contato}\n" if contato else "Contato não encontrado.\n")

        elif opcao == "4":
            nome = input("Digite o nome para buscar (binária): ")
            contato = buscar_binaria(nome)
            print(f"Resultado: {contato}\n" if contato else "Contato não encontrado.\n")

        elif opcao == "0":
            print("Encerrando a agenda...")
            break

        else:
            print("Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    main()
