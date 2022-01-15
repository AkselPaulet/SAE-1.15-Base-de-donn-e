import csv
from time import sleep
from math import sqrt
from datetime import datetime




def writer(content,station_name="vmag",mode="w",extension=".txt"):
    """ Met le contenu de la page dans un fichier txt au nom de la station ( si pas de fichier : il le crée )"""


    file_name = "./station_file/"+station_name+extension # trouve le nom de la station puis rajoute l'extention .txt pour le fichier 

    fichier = open(file_name,mode,encoding='utf8') # ouvre le fichier en mode écriture ( si inexistant : création file )

    fichier.write(content)                           # écrit dans le fichier le contenu de la page web

    fichier.close()                                  # ferme proprement le fichier



def csv_file_writer_trie(info_station,csv_existe):
    global mn.csv_existe
    """" écrit dans le fichier stat_vmag.csv les données xml de manière ordonée"""

    time = str(datetime.now())

    with open('stat_vmag.csv', 'a', newline='') as csvfile:      # ouvre un fichier CSV en écriture nommée stat.csv ou le crée si existe pas
        
        fieldnames = ['station_name', 'taken_vmag_space','free_vmag_space','total_vmag_space','year','day&month','hour&min']     # donne les noms de chaque catégorie
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)                 # donne attirbut csv et les sépatateurs a la variable writer

        if mn.csv_existe == False :    # Si le fichier csv est défini dans le main comme non existant ALORS
            writer.writeheader()    # On écrit le titre des catégories +
            mn.csv_existe = True       # On défini dans le main le fichier comme existant 

        for i in range (len(info_station)):   # pour chaque id ( parking ) l'on écrit dans le fichier csv pour chaque catégorie leurs entrées
            writer.writerow({'station_name': info_station[i][0],'taken_vmag_space': info_station[i][1] , 'free_vmag_space': info_station[i][2], 'total_vmag_space': info_station[i][3],  'year': time[0:4],  'day&month': time[5:10],  'hour&min': time[11:16]})   # écrit dans le fichier csv

    print(f"Une donnée a été enregisté dans le fichier stat_vmag.csv le {time[5:10]} à {time[11:16]} prochain relever prévu a {time[11:13]+str(int(time[14:16])+5)}")