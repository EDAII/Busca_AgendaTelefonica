# contatos_base.py
import random

# Bases de nomes e sobrenomes
nomes_base = [
    "Ana", "Bruno", "Carlos", "Daniela", "Alice", "Arthur", "Sophia", "Bernardo",
    "Isabella", "Davi", "Cecília", "Heitor", "Lívia", "Lucas", "Julia", "Pedro",
    "Mariana", "Gabriel", "Beatriz", "Matheus", "Laura", "Felipe", "Isabela",
    "Rafael", "Manuela", "Gustavo", "Lorenzo", "Maria Luíza", "Théo", "Júlia",
    "Samuel", "Eloá", "Benício", "Manuella", "Joaquim", "Yasmin", "Nicolas",
    "Lara", "Henrique", "Gabriela", "Enzo", "Valentina", "Miguel", "Helena"
]

sobrenomes_base = [
    "Silva", "Souza", "Oliveira", "Pereira", "Costa", "Santos", "Almeida",
    "Gomes", "Ribeiro", "Martins", "Carvalho", "Lima", "Barbosa", "Rocha",
    "Fernandes", "Moura", "Azevedo", "Medeiros", "Cavalcante", "Freitas"
]

dominios_email = ["gmail.com", "outlook.com", "yahoo.com", "hotmail.com"]

contatos_iniciais = []

for i in range(5000):  # gerar 5000 contatos
    nome = random.choice(nomes_base)
    sobrenome = random.choice(sobrenomes_base)
    nome_completo = f"{nome} {sobrenome}"
    
    # telefone no formato (DDD) 9XXXX-XXXX
    ddd = random.randint(11, 99)
    telefone = f"({ddd}) 9{random.randint(1000,9999)}-{random.randint(1000,9999)}"
    
    # e-mail com domínios variados
    dominio = random.choice(dominios_email)
    email = f"{nome.lower()}.{sobrenome.lower()}{i}@{dominio}"
    
    contatos_iniciais.append({
        "nome": nome_completo,
        "telefone": telefone,
        "email": email
    })

# Exemplo: imprimir o primeiro contato
# print(contatos_iniciais[0])
