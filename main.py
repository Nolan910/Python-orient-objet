import pandas as pd
#import matplotlib.pyplot as plt

#------------------#Exercice 1------------------

def get_clean_file(file_path):
    return (pd.read_csv(file_path, sep=';', encoding='utf-8')
            .drop_duplicates())
            #Pas des valeurs manquantes à remplir

def get_interesting_colums(df, columns):
    missing_columns = [col for col in columns if col not in df.columns]
    if missing_columns:
        print(f"Columns missing")
        return pd.DataFrame()
    return df[columns]


cinemas= get_clean_file("./data/cinemas.csv")
cinemas_columns = [
    #On garde les valeurs utiles à la réalisation de l'exercice*
    "commune",
    "région administrative",
    "écrans",
    "fauteuils",
    "entrées 2022",
    "entrées 2021",
    "évolution entrées"
]

cinemas_filtered_columns = get_interesting_colums(cinemas, cinemas_columns)
statistiques = pd.DataFrame(cinemas_filtered_columns)

# print("cinemas infos")
# print(statistiques.head())


#------------------#Exercice 2------------------

cinemas['entrées par fauteuil 2022'] = cinemas["entrées 2022"] / cinemas["fauteuils"]
entrée_moyenne_par_région = cinemas.groupby('région administrative')['entrées par fauteuil 2022'].mean()

#print(entrée_moyenne_par_région)

meilleures_régions = entrée_moyenne_par_région.sort_values(ascending=False)
print("Les 3 régions ayant les meilleurs résultats")
print(meilleures_régions.head(3))

pires_régions = entrée_moyenne_par_région.sort_values(ascending=True)
print("Les 3 régions ayant les pires résultats")
print(pires_régions.head(3))