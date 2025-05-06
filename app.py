import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Chargement des données
df = pd.read_csv("SampleSuperstore.csv")

# Nettoyage des colonnes
df.columns = df.columns.str.strip()

# Titre
st.title("📊 Tableau de bord des ventes")

# Métriques principales
st.subheader("Vue d'ensemble")
col1, col2, col3 = st.columns(3)
col1.metric("Chiffre d'affaires total", f"${df['Sales'].sum():,.0f}")
col2.metric("Bénéfice total", f"${df['Profit'].sum():,.0f}")
col3.metric("Nombre de commandes", df.shape[0])

# Top produits
st.subheader("🏆 Top 10 produits par ventes")
top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)



# Graphique des profits par État
st.subheader("💰 Profits par État")
profit_by_state = df.groupby("State")["Profit"].sum().sort_values()
fig, ax = plt.subplots(figsize=(10, 8))
profit_by_state.plot(
    kind='barh',
    color=['green' if x > 0 else 'red' for x in profit_by_state],
    ax=ax
)
ax.set_xlabel("Profit")
ax.set_ylabel("État")
ax.set_title("Profit par État")
st.pyplot(fig)

# Filtres interactifs
st.sidebar.header("Filtres")
region_filter = st.sidebar.multiselect("Région", df['Region'].unique(), default=df['Region'].unique())
segment_filter = st.sidebar.multiselect("Segment", df['Segment'].unique(), default=df['Segment'].unique())

filtered_df = df[(df['Region'].isin(region_filter)) & (df['Segment'].isin(segment_filter))]

st.subheader("📌 Données filtrées")
st.dataframe(filtered_df)
