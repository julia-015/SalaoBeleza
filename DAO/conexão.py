import mysql.connector


conexao = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "fleur"
)

if conexao.is_connected():
    print("Conexão estabelecida com sucesso")

cursor = conexao.cursor()

cursor.execute("")

resultados = cursor.fetchall()




cursor.close()
conexao.close()

print (resultados)
