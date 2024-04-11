import datetime

pip install datetime
class Agendamento:
    def __init__(self, data, hora, descricao):
        self.data = data
        self.hora = hora
        self.descricao = descricao

agendamentos = []

def adicionar_agendamento(data, hora, descricao):
    novo_agendamento = Agendamento(data, hora, descricao)
    agendamentos.append(novo_agendamento)

def visualizar_agendamentos():
    for agendamento in agendamentos:
        print(f"Data: {agendamento.data}, Hora: {agendamento.hora}, Descrição: {agendamento.descricao}")

adicionar_agendamento("2024-04-11", "15:00", "Reunião de equipe")
adicionar_agendamento("2024-04-12", "10:30", "Entrevista de emprego")
visualizar_agendamentos()



