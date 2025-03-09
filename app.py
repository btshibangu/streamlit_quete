import streamlit as st
st.title("Bienvenue sur le site de Barthélémy")

ville = st.selectbox("Indiquez votre ville",
['Paris', 'Marseille', 'Orléans'])

st.write('Tu as choisi Paris')

# Dictionnaire des images associées aux villes
images = {
    "Paris": "paris.jpg",
    "Marseille": "marseille.jpg",
    "Orléans": "orleans.jpg"
}

if ville in images:
    st.image(images[ville], caption=ville, use_column_width=True)
