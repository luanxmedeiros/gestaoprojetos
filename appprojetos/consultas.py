
# LUAN, EU ACHEI ISSO AQUI, NÃO SEI SE É CERTO, NÃO RODEL, SÓ COLOQUEI PRA VOCE VER.


import sqlite3
#conectando..
conn = sqlite3.connect("django.db")

# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute\
("""
    CREATE TABLE IF NOT EXISTS membros
    (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            email TEXT NOT NULL,
            fone TEXT,
    );
""")

print('Tabela criada com sucesso.')

# desconectando...
conn.close()

