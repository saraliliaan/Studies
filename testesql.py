import sqlite3
#importar banco de dados
conn = sqlite3.connect('aulaBD.db')
#insert - adicionar valores no BD
cursor = conn.cursor()
cursor.execute("""INSERT INTO fornecedor (nome.fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-11, 'São Paulo', 'SP', '11111-111', '2020-01-01')
""")

conn.commit()

#read - ler valor no BD
cursor.execute("SELECT * FROM fornecedor")
resultado = cursor.fetchall()
for linha in resultado:
    print(linha)

#update - inserir um registro no BD
cursor.execute("UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5")
conn.commit()

#delete - deletar um registro do BD
cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = 2")
conn.commit()
