import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Charger les données
url = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(url)

# Mapper les noms des régions correctement
region_mapping = {
    ' US.': 'US',
    ' Europe.': 'Europe',
    ' Japan.': 'Japan'
}
df['continent'] = df['continent'].map(region_mapping)

# Titre de l'application
st.title("📊 Analyse des Voitures par Région")

# Sélection de la région avec des boutons radio
selected_region = st.radio("Choisissez une région :", ['US', 'Europe', 'Japan'])

# Filtrer les données en fonction de la région sélectionnée
filtered_df = df[df['continent'] == selected_region]

# Affichage des premières lignes des données filtrées
st.write("### Données filtrées :", filtered_df.head())

# Exclude non-numeric columns before correlation
numeric_df = filtered_df.select_dtypes(include=['number'])

# Affichage de la matrice de corrélation
st.write("### Matrice de Corrélation")
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

# Histogrammes des distributions
st.write("###  Distribution des Variables Clés")
variables = ['mpg', 'hp', 'weightlbs']
for var in variables:
    fig, ax = plt.subplots()
    sns.histplot(filtered_df[var], kde=True, bins=20, ax=ax)
    st.pyplot(fig)

# Commentaires sur l'analyse
st.write("##  Analyse des Résultats")
st.write("-  La matrice de corrélation montre les relations entre les caractéristiques des voitures.")
st.write("-  Les histogrammes permettent d'analyser la distribution des variables importantes comme la consommation (mpg), la puissance (hp) et le poids des voitures.")

st.write(" Développé avec par un passionné de Data")
