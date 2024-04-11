from flask import Flask, request, render_template, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Conexão com o banco de dados MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="seu_usuario_mysql",
    password="sua_senha_mysql",
    database="Fleur"
)
cursor = conn.cursor()

# Rota para o formulário de agendamento
@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        mensagem = request.form['mensagem']
        
        # Inserir os dados no banco de dados
        cursor.execute("INSERT INTO agendamentos (nome, email, telefone, mensagem) VALUES (%s, %s, %s, %s)", (nome, email, telefone, mensagem))
        conn.commit()
        
        flash('Formulário enviado com sucesso!')
        return redirect(url_for('form'))
    return render_template('agendamentos.html')

if __name__ == '__main__':
    app.run(debug=True)
