/*FPM-MRSAPE*/

create database fpmmrsape /*nome do banco*/;

-- Selecionar o banco de dados 
use fpmmrsape;

-- Criar tabelas
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

-- Importando dados a partir de um arquivo
/*Arquivo baixado do site do Tesouro Nacional*/

load data infile 'aquivo.csv' into table transferencias
fields terminated by ';' enclosed by '"'
ignore 1 lines
(uf, municipios, ano, mes, transferencia, valar);