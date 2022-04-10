import pandas as pd
import streamlit as st
import plotly_express as px

df = pd.read_csv("exchange_rates.csv")

st.title("Évolution des taux de change par rapport à l'Euro (€)")
st.markdown('[Data credit : La Banque de France](https://www.banque-france.fr/statistiques/taux-et-cours/les-taux-de-change-salle-des-marches/parites-quotidiennes)')

fig = px.line(df, x="symbol", y="date", hover_name="currency",
        line_shape="spline", render_mode="svg")
fig.show()
