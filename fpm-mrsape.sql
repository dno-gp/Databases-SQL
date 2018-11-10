/****************************
 **FPM-Microrregião Sapé-PB**
 ****************************/
-- 

create database fpmmrsape /*nome do banco*/;
-- Selecionando o banco de dados 
use fpmmrsape;

-- Criando as tabelas
create table municipios(
idmunic int(1) auto_increment primary key,
municipio varchar(45) not null,
populacao int
)charset='utf8';

create table transferencias(
idreg int auto_increment primary key,
uf char(2),
municipio int(1),
ano year,
mes varchar(2),
transferencia varchar(45),
valor decimal(10,2),
foreign key (municipio) references municipios(idmunic)
)charset = 'utf8';

-- Adicionando os municípios - Microrregião Sapé
insert into municipios (municipio) 
values("Cruz do Espírito Santo"), ("Juripiranga"),("Mari"),
("Pilar"), ("Riachão do Poço"), ("São José dos Ramos"), 
("São Miguel de Taipu"), ("Sapé"), ("Sobrado");

-- Importando dados a partir de um arquivo - Transferências Constitucionais obrigatórias
-- Arquivo baixado do site do Tesouro Nacional
load data infile '/var/lib/mysql-files/transferencias.csv' into table transferencias
fields terminated by ';' enclosed by '"'
ignore 1 lines
(uf, municipio, ano, mes, transferencia, valor);