import sqlite3
#importar banco de dados
conn = sqlite3.connect('aulaBD.db')
#adicionar valores no BD
cursor = conn.cursor()
cursor.execute("""INSERT INTO fornecedor (nome.fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11, 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

conn.commit()

#ler valores no BD
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)