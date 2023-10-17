import streamlit as st

# Créez un formulaire pour saisir les informations de l'utilisateur
st.title("Formulaire d'Informations Client")

# Informations personnelles
id_client = st.text_input("ID Client")
genre = st.radio("Genre", ["Homme", "Femme", "Inconnu"])
age = st.number_input("Âge")
segment_client = st.text_input("Segment Client")

# Informations sur l'espace client web
espace_client_web = st.radio("Espace Client Web", ["Oui", "Non", "Inconnu"])

# Informations sur l'assurance vie
assurance_vie = st.radio("Assurance Vie", ["Oui", "Non", "Inconnu"])

# Informations sur le banque principale
banque_principale = st.text_input("Banque Principale")

# Informations sur l'ancienneté en mois
anciennete_mois = st.number_input("Ancienneté en mois")

# Informations sur le compte d'épargne
compte_epargne = st.radio("Compte Épargne", ["Oui", "Non", "Inconnu"])

# Informations sur les crédits
credit_autres = st.radio("Crédit Autres", ["Oui", "Non", "Inconnu"])
credit_immo = st.radio("Crédit Immobilier", ["Oui", "Non", "Inconnu"])

# Informations sur les cartes bancaires
cartes_bancaires = st.checkbox("Cartes Bancaires")

# Informations sur le compte courant
compte_courant = st.radio("Compte Courant", ["Oui", "Non", "Inconnu"])

# Informations sur l'espace client
espace_client = st.radio("Espace Client", ["Oui", "Non", "Inconnu"])

# Informations sur le PEA (Plan d'Épargne en Actions)
PEA = st.radio("PEA", ["Oui", "Non", "Inconnu"])

# Informations sur l'assurance auto
assurance_auto = st.radio("Assurance Auto", ["Oui", "Non", "Inconnu"])

# Informations sur l'assurance habitation
assurance_habitation = st.radio("Assurance Habitation", ["Oui", "Non", "Inconnu"])

# Informations sur le compte titres
compte_titres = st.radio("Compte Titres", ["Oui", "Non", "Inconnu"])

# Informations sur la méthode de contact
methode_contact = st.selectbox(
    "Méthode de Contact", ["Téléphone", "Email", "Courrier", "Inconnu"]
)

# Informations sur les agios sur 6 mois
agios_6mois = st.number_input("Agios sur 6 Mois")

# Informations sur les intérêts du compte d'épargne total
interet_compte_epargne_total = st.number_input("Intérêt du Compte d'Épargne Total")

# Informations sur les variables supplémentaires
var_0 = st.number_input("Var 0")
var_1 = st.number_input("Var 1")
# ... Répétez cette étape pour toutes les variables supplémentaires

# Informations sur la branche
branche = st.text_input("Branche")

# Informations sur le churn
churn = st.radio("Churn", ["Oui", "Non", "Inconnu"])

# Bouton pour soumettre le formulaire
submit_button = st.button("Soumettre")

# Affichez les informations soumises si le bouton est cliqué
if submit_button:
    st.subheader("Informations soumises:")
    st.write(f"ID Client: {id_client}")
    st.write(f"Genre: {genre}")
    st.write(f"Âge: {age}")
    st.write(f"Segment Client: {segment_client}")
    st.write(f"Espace Client Web: {espace_client_web}")
    st.write(f"Assurance Vie: {assurance_vie}")
    st.write(f"Banque Principale: {banque_principale}")
    st.write(f"Ancienneté en mois: {anciennete_mois}")
    st.write(f"Compte Épargne: {compte_epargne}")
    st.write(f"Crédit Autres: {credit_autres}")
    st.write(f"Crédit Immobilier: {credit_immo}")
    st.write(f"Cartes Bancaires: {cartes_bancaires}")
    st.write(f"Compte Courant: {compte_courant}")
    st.write(f"Espace Client: {espace_client}")
    st.write(f"PEA: {PEA}")
    st.write(f"Assurance Auto: {assurance_auto}")
    st.write(f"Assurance Habitation: {assurance_habitation}")
    st.write(f"Compte Titres: {compte_titres}")
    st.write(f"Méthode de Contact: {methode_contact}")
    st.write(f"Agios sur 6 Mois: {agios_6mois}")
    st.write(f"Intérêt du Compte d'Épargne Total: {interet_compte_epargne_total}")
    st.write(f"Branche: {branche}")
    st.write(f"Churn: {churn}")
    # Ajoutez des lignes pour afficher les autres variables supplémentaires
