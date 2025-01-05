import pandas as pd
#import matplotlib.pyplot as plt

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
    "écrans",
    "fauteuils",
    "entrées 2022",
    "entrées 2021",
    "évolution entrées"
]

cinemas_filtered_columns = get_interesting_colums(cinemas, cinemas_columns)
statistiques = pd.DataFrame(cinemas_filtered_columns)

print("cinemas infos")
print(statistiques.head())

