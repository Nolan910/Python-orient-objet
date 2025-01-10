import pandas as pd
import matplotlib.pyplot as plt
import math

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
# print("Les 3 régions ayant les meilleurs résultats")
# print(meilleures_régions.head(3))

pires_régions = entrée_moyenne_par_région.sort_values(ascending=True)
# print("Les 3 régions ayant les pires résultats")
# print(pires_régions.head(3))

#Graphique à barres des moyennes par régions
entrée_moyenne_par_région.sort_values().plot(kind="bar", figsize=(12, 6))
plt.title('Entrées moyennes par fauteuil pour les 10 régions')
plt.xlabel('Régions')
plt.ylabel('Entrées par fauteuil')
plt.xticks(rotation=45)
plt.tight_layout()
# plt.show()


#------------------#Exercice 3------------------

écrans = cinemas['écrans']
fauteuils = cinemas['fauteuils']
entrées_2022 = cinemas['entrées 2022']

#Corrélation fauteils/entrées
#1 Multipliez chaque paire de valeurs correspondantes des deux variables.
f_produits = fauteuils * entrées_2022

#2 Additionnez tous ces produits.
f_somme_produits = f_produits.sum()

#3 Multipliez le nombre total de valeurs par la somme des carrés de chaque variable.
f_somme_carre_fauteuils = (fauteuils ** 2).sum()
f_somme_carre_entrees = (entrées_2022 ** 2).sum()

f_nombre_total_de_valeurs = len(fauteuils)

f_multiplication = f_nombre_total_de_valeurs * (f_somme_carre_fauteuils + f_somme_carre_entrees)

#4 Soustrayez le produit des sommes des deux variables.
f_somme_fauteuils = fauteuils.sum()
f_somme_entrees = entrées_2022.sum()

f_produit_sommes = f_somme_fauteuils * f_somme_entrees

f_soustraction = f_multiplication - f_produit_sommes

#5Divisez le résultat par la racine carrée du produit des variances des deux variables.
f_valeur_a_diviser = math.sqrt((f_nombre_total_de_valeurs * f_somme_carre_fauteuils - f_somme_fauteuils ** 2) * (f_nombre_total_de_valeurs * f_somme_carre_entrees - f_somme_entrees ** 2))

f_correlation = f_soustraction / f_valeur_a_diviser

print("Corrélation entre le nombre de fauteuils et les entrées de 2022")
print(f_correlation)


#Corrélation écrans/entrées
#1 Multipliez chaque paire de valeurs correspondantes des deux variables.
e_produits = écrans * entrées_2022

#2 Additionnez tous ces produits.
e_somme_produits = e_produits.sum()

#3 Multipliez le nombre total de valeurs par la somme des carrés de chaque variable.
e_somme_carre_écrans = (écrans ** 2).sum()
e_somme_carre_entrees = (entrées_2022 ** 2).sum()

e_nombre_total_de_valeurs = len(écrans)

e_multiplication = e_nombre_total_de_valeurs * (e_somme_carre_écrans + e_somme_carre_entrees)

#4 Soustrayez le produit des sommes des deux variables.
e_somme_écrans = écrans.sum()
e_somme_entrees = entrées_2022.sum()

e_produit_sommes = e_somme_écrans * e_somme_entrees

e_soustraction = e_multiplication - e_produit_sommes

#5Divisez le résultat par la racine carrée du produit des variances des deux variables.
e_valeur_a_diviser = math.sqrt((e_nombre_total_de_valeurs * e_somme_carre_écrans - e_somme_écrans ** 2) * (e_nombre_total_de_valeurs * e_somme_carre_entrees - e_somme_entrees ** 2))

e_correlation = e_soustraction / e_valeur_a_diviser

print("Corrélation entre le nombre d'écrans et les entrées de 2022")
print(e_correlation)