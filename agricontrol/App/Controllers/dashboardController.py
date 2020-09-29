import MySQLdb # para o MySQL
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import pyplot
import matplotlib as mpl
import numpy as np
import pandas as pd


FontSize = 20
def makeGraph():
    # TIRAR ERRO DE RODAR O SERVIDOR TODA HORA.
    plt.switch_backend('agg')
    con = MySQLdb.connect('50.116.112.31', 'tourvi45_aps', 'unip@2020')
    con.select_db('tourvi45_APS')
    cursor = con.cursor()

    cursor.execute("select distinct(farming) from producers")
    labels_farming = cursor.fetchall()

    cursor.execute("select farming, sum(annualamount) from producers group by(farming)")
    culti_qtd = cursor.fetchall()

    cursor.execute("select sum(annualamount) from producers")
    totalCulti = cursor.fetchall()

    cursor.execute("select count(pesticide) from producers")
    totalAgri = cursor.fetchall(),

    # somando todos os produtos de acordo com seu agrotoxico
    cursor.execute('select pesticide, sum(annualamount) from producers group by(pesticide)')
    agro_qtd = cursor.fetchall()

    query = cursor.execute('select distinct(pesticide) from producers')
    labels_pesticide = cursor.fetchall()
# --------------------------------------------------------------------------------------------

    def plot1():
        plot1_cult_qtd = []
        for valor in culti_qtd:
            plot1_cult_qtd.append(valor[1])

        plot1_labels = []
        for valor in labels_farming:
            plot1_labels.append(valor[0])

        plot1_totalCulti = totalCulti[0]

        porcent_culti =[]

        for value in plot1_cult_qtd:
            porcent_culti.append((value / plot1_totalCulti[0]) * 100)
        
        porcent = pd.Series(porcent_culti)
        print(porcent)

        porcent.astype(float).plot(color = 'blue')
        plt.bar(plot1_labels,  porcent_culti, color = '#F2410C')
        # plt.tick_params(labelsize= 11)
        plt.xlabel("Produtos", fontsize = FontSize)
        plt.ylabel("% Porcentagem", fontsize = FontSize)
        plt.savefig("App/Static/images/plot1.png")
        plt.close()
        
    # --------------------------------------------------------------------------------------------


    def plot2():

        plot2_agro_qtd = []
        for valor in agro_qtd:
            plot2_agro_qtd.append(valor[1])

        plot2_labels = []
        for valor in labels_pesticide:
            plot2_labels.append(valor[0])

        porcent = pd.Series(plot2_agro_qtd)

        plt.figure(figsize=(10,8))
        porcent.astype(float).plot(color = 'blue')
        plt.bar(plot2_labels,  plot2_agro_qtd, color = 'red')
        plt.tick_params(labelsize= 15)
        plt.xlabel("Agrotóxicos", fontsize = FontSize)
        plt.ylabel("Quantidade", fontsize = FontSize)
        plt.savefig("App/Static/images/plot2.png")
        plt.close()

# --------------------------------------------------------------------------------------------
    def plot3():
        plot3_cult_qtd = []
        for valor in culti_qtd:
            plot3_cult_qtd.append(valor[1])

        plot3_labels = []
        for valor in labels_farming:
            plot3_labels.append(valor[0])
        
        plot3_totalCulti = totalCulti[0]

        plot3_porcent_culti =[]
        print(plot3_totalCulti[0])
        for value in plot3_cult_qtd:
            plot3_porcent_culti.append((value / plot3_totalCulti[0]) * 100)
        
        plt.pie(plot3_porcent_culti, labels= plot3_labels, autopct="%2.2f%%")
        plt.legend(plot3_labels,bbox_to_anchor = [1, 1])
        plt.savefig("App/Static/images/plot3.png")
        plt.close()

# --------------------------------------------------------------------------------------------
    def plot4():

        plot4_labels = []
        for valor in labels_pesticide:
            plot4_labels.append(valor[0])

        plot4_agro_qtd = []
        for valor in agro_qtd:
            plot4_agro_qtd.append(valor[1])

        plot4_totalagri = totalAgri[0]
        plot4_porcent_agri = []

        for value in plot4_agro_qtd:
            plot4_porcent_agri.append((value / plot4_totalagri[0][0]) * 100)
        
        plt.pie(plot4_porcent_agri, labels= plot4_labels, autopct="%2.2f%%")
        plt.legend(plot4_labels, bbox_to_anchor = [1, 1])
        plt.savefig("App/Static/images/plot4.png")
        plt.close()
        
    plot1()
    plot2()
    plot3()
    plot4()
