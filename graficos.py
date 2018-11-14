import pymysql
import numpy as np 
import matplotlib.pyplot as plt

#Conexão com o banco de dados
try:
    link = pymysql.connect(host="127.0.0.1", user="", password="", db="fpmmrsape")

except:
    print("Conexão não estabelecida com a base de dados.")

#Executar as consultas
try:
    with link.cursor() as c:
        
        sql = "select sum(valor) from transferencias group by ano order by ano"
        c.execute(sql)
        valor = c.fetchall()

        sqlano = "select distinct ano from transferencias"
        c.execute(sqlano)
        ano = c.fetchall()

        sql1 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (1))
        ces = c.fetchall()
            
        sql2 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (2))
        jpr = c.fetchall()
        
        sql3 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (3))
        mri = c.fetchall()

        sql4 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (4))
        plr = c.fetchall()

        sql5 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (5))
        rip = c.fetchall()

        sql6 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (6))
        sjr = c.fetchall()

        sql7 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (7))
        smt = c.fetchall()

        sql8 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (8))
        spe = c.fetchall()

        sql9 = "select sum(valor) from transferencias where municipio = %s group by ano order by ano"
        c.execute(sql1, (9))
        sbd = c.fetchall()
except:
    print("Erro de consulta.")

#Montando os gráficos
try:
    fig = plt.figure()
    ax1 = fig.add_subplot(2,1,1)
    ax1 = plt.plot(ano, valor)

    ax2 = fig.add_subplot(2,1,2)
    ax2 = plt.plot(ano, ces, label = 'Cruz E. Santo')
    ax2 = plt.plot(ano, jpr, label = 'Juripianga')
    ax2 = plt.plot(ano, mri, label = 'Mari')
    ax2 = plt.plot(ano, plr, label = 'Pilar')
    ax2 = plt.plot(ano, rip, label = 'R. do Poço')
    ax2 = plt.plot(ano, sjr, label = 'São J. Ramos')
    ax2 = plt.plot(ano, smt, label = 'São M. Taipu')
    ax2 = plt.plot(ano, spe, label = 'Sapé')
    ax2 = plt.plot(ano, sbd, label = 'Sobrado')

    plt.legend()
    plt.show()
    
except:
    print("Erro na criação dos gráficos")

finally:
    link.close()
    print("Saindo...")
