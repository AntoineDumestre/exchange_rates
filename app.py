import pandas as pd
import streamlit as st
import plotly_express as px

# Import et Préparation des données 
df = pd.read_csv("exchange_rates.csv")

all_symbols = df['symbol'].unique().tolist()
all_symbols.sort()

time_period= df['date'].unique().tolist()
time_period.sort(reverse=False)

update_date = df['date'].max()


# Affichage du graphe et des filtres
st.title("Évolution des taux de change par rapport à l'Euro (€)")
st.markdown('Date de mise à jour : ' + update_date)

selected_symbols = st.multiselect('Monnaies à afficher', all_symbols, default=['USD','GBP','CHF','CAD'])
df = df[df['symbol'].isin(selected_symbols)]


selected_period = st.select_slider('Choix de la période affichée', options=time_period, value=[df['date'].min(),df['date'].max()])
df = df[(df['date']>=min(selected_period))&(df['date']<=max(selected_period))]

fig = px.line(df, x="date", y="value", color="currency", hover_name="currency",
        line_shape="spline", render_mode="svg")
st.plotly_chart(fig, use_container_width=True)

container = st.container()
container.text('Sources de données :')
container.markdown('[La Banque de France](https://www.banque-france.fr/statistiques/taux-et-cours/les-taux-de-change-salle-des-marches/parites-quotidiennes)')
container.markdown('[Yahoo Finance (BTC)](https://fr.finance.yahoo.com/quote/BTC-EUR/)')

st.download_button('Télécharger les données (csv)', data=csv, file="exchange_rates.csv")
