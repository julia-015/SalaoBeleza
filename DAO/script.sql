create database Fleur;

use fleur;

create table clientes(
	id int(6) auto_increment primary key,
	nome varchar(30),
	email varchar(30),
	telefone int (11)
    );
    
create table agendamentos(
	id int auto_increment primary key,
	clienteName varchar(30),
    foreign key (cliente_id) REFERENCES clientes(id),
    serviço int (2),
	telefone int (11),
	horario int (4),
	dia int (8)
    );


INSERT INTO clientes (nome, email, telefone) 
VALUES ('Julia Martins', 'julia.martins@example.com', 198765432),
('Roberto Lima', 'roberto.lima@example.com', 198765432),
('Fernanda Correia', 'fernanda.correia@example.com', 198765432),
('Lucas Alves', 'lucas.alves@example.com', 198765432),
('Sofia Ferreira', 'sofia.ferreira@example.com', 198765432),
('Rafael Santos', 'rafael.santos@example.com', 198765432),
('Camila Gomes', 'camila.gomes@example.com', 198765432),
('Eduardo Souza', 'eduardo.souza@example.com', 019876543),
('Patrícia Oliveira', 'patricia.oliveira@example.com', 119876543);

INSERT INTO agendamentos (clienteName, serviço, telefone, horario, dia) 
VALUES ('Julia Martins', 1, 198765432, 930, 20220301),
('Roberto Lima', 2, 198765432, 1030, 20220302),
('Fernanda Correia', 3, 198765432, 1430, 20220303),
('Lucas Alves', 1, 198765432, 1630, 20220304),
('Sofia Ferreira', 2, 198765432, 930, 20220305),
('Rafael Santos', 3, 198765432, 1030, 20220306),
('Camila Gomes', 1, 198765432, 1430, 20220307),
('Eduardo Souza', 2, 019876543, 1630, 20220308),
('Patrícia Oliveira', 3, 119876543, 930, 20220309);