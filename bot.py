import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Charger toutes les données
data = {
    'Company Name': ['APPLE']*10 + ['MICROSOFT']*10 + ['TESLA']*10,
    'Year': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024] * 3,
    'revenu': [100, 110, 120, 130, 140, 150, 365.817, 394.328, 383.285, 402.449,
               93.76, 96, 105, 115, 130, 160, 168.088, 198.27, 211.915, 224.842,
               4, 7, 11.7, 21.5, 24.5, 31.5, 53.823, 81.462, 96.773, 104.635],
    'cash Flow': [24, 26, 28, 30, 32, 35, 39.789, 35.929, 24.977, 26.125,
                  35.218, 36.5, 40, 43.5, 50, 60, 61.271, 72.738, 72.361, 74.329,
                  1, 1.5, 2, 4, 4.2, 6, 5.644, 12.587, 14.974, 16.922],
    'Total actif': [200, 220, 240, 260, 280, 300, 351.002, 352.755, 352.583, 370.212,
                    250, 255, 270, 290, 310, 320, 333.779, 364.84, 411.976, 441.412,
                    12, 14.5, 20, 30, 35, 45, 62.131, 82.338, 106.618, 120.708],
    'Total passif': [65, 70, 75, 80, 85, 90, 287.912, 302.083, 290.437, 304.958,
                     130, 135, 140, 145, 150, 160, 191.791, 198.298, 205.753, 211.928,
                     8, 10, 12.5, 18, 20, 25, 30.548, 36.44, 43.009, 47.52],
    'taux de croissance du revenu': [None, 10, 9.09, 8.33, 7.69, 7.14, 143.88, 7.79, -2.80, 5.00,
                                     2.39, 3.64, 9.38, 9.52, 13.04, 23.08, 5.06, 17.96, 6.88, 6.10,
                                     None, 75, 67, 84, 14, 29, 71, 51, 19, 8],
    'taux de croissance du cash flow': [None, 8.33, 7.69, 7.14, 6.67, 9.38, 13.68, -9.70, -30.48, 4.60,
                                       3.64, 3.85, 9.59, 8.75, 14.94, 20.00, 2.12, 18.72, -0.52, 2.72,
                                       None, 50, 33, 100, 5, 43, -6, 123, 19, 13],
    'taux de croissance des actifs': [None, 10.00, 9.09, 8.33, 7.69, 7.14, 17.00, 0.50, -0.05, 5.00,
                                     2.00, 3.85, 5.88, 7.41, 6.90, 3.23, 4.31, 9.31, 12.92, 7.15,
                                     None, 21, 38, 50, 17, 29, 38, 33, 29, 13],
    'taux de croissance des passifs': [None, 7.69, 7.14, 6.67, 6.25, 5.88, 219.90, 4.92, -3.86, 5.00,
                                      3.85, 3.45, 3.70, 3.57, 3.45, 6.67, 19.87, 3.39, 3.76, 3.00,
                                      None, 25, 25, 44, 11, 25, 22, 19, 18, 10]
}

df = pd.DataFrame(data)

# Fonction pour obtenir les données pour une année donnée et une entreprise
def get_data_for_year_and_company(year, company, indicator):
    company_data = df[df['Company Name'] == company]
    if indicator == "revenu":
        return company_data[company_data['Year'] == year]['revenu'].values[0]
    elif indicator == "cash flow":
        return company_data[company_data['Year'] == year]['cash Flow'].values[0]
    elif indicator == "actif":
        return company_data[company_data['Year'] == year]['Total actif'].values[0]
    elif indicator == "passif":
        return company_data[company_data['Year'] == year]['Total passif'].values[0]
    elif indicator == "croissance revenu":
        return company_data[company_data['Year'] == year]['taux de croissance du revenu'].values[0]
    elif indicator == "croissance cash flow":
        return company_data[company_data['Year'] == year]['taux de croissance du cash flow'].values[0]
    elif indicator == "croissance actif":
        return company_data[company_data['Year'] == year]['taux de croissance des actifs'].values[0]
    elif indicator == "croissance passif":
        return company_data[company_data['Year'] == year]['taux de croissance des passifs'].values[0]
    else:
        return None

# Fonction pour générer des graphiques
def plot_company_graph(company, indicator):
    company_data = df[df['Company Name'] == company]
    plt.figure(figsize=(10, 6))
    if indicator == "revenu":
        plt.plot(company_data['Year'], company_data['revenu'], marker='o', label='Revenus')
        plt.title(f'Évolution des Revenus de {company}')
        plt.ylabel('Revenus (millions de dollars)')
    elif indicator == "cash flow":
        plt.plot(company_data['Year'], company_data['cash Flow'], marker='o', label='Flux de trésorerie')
        plt.title(f'Évolution des Flux de Trésorerie de {company}')
        plt.ylabel('Flux de Trésorerie (millions de dollars)')
    elif indicator == "actif":
        plt.plot(company_data['Year'], company_data['Total actif'], marker='o', label='Total Actifs')
        plt.title(f'Évolution des Actifs de {company}')
        plt.ylabel('Actifs Totaux (millions de dollars)')
    elif indicator == "passif":
        plt.plot(company_data['Year'], company_data['Total passif'], marker='o', label='Total Passifs')
        plt.title(f'Évolution des Passifs de {company}')
        plt.ylabel('Passifs Totaux (millions de dollars)')
    elif indicator == "croissance revenu":
        plt.plot(company_data['Year'], company_data['taux de croissance du revenu'], marker='o', label='Croissance des Revenus')
        plt.title(f'Taux de Croissance des Revenus de {company}')
        plt.ylabel('Croissance (%)')
    elif indicator == "croissance cash flow":
        plt.plot(company_data['Year'], company_data['taux de croissance du cash flow'], marker='o', label='Croissance des Flux de Trésorerie')
        plt.title(f'Taux de Croissance des Flux de Trésorerie de {company}')
        plt.ylabel('Croissance (%)')
    elif indicator == "croissance actif":
        plt.plot(company_data['Year'], company_data['taux de croissance des actifs'], marker='o', label='Croissance des Actifs')
        plt.title(f'Taux de Croissance des Actifs de {company}')
        plt.ylabel('Croissance (%)')
    elif indicator == "croissance passif":
        plt.plot(company_data['Year'], company_data['taux de croissance des passifs'], marker='o', label='Croissance des Passifs')
        plt.title(f'Taux de Croissance des Passifs de {company}')
        plt.ylabel('Croissance (%)')
    plt.xlabel('Année')
    plt.grid(True)
    plt.legend()
    st.pyplot()

# Interface Streamlit
st.title("Chatbot d'Analyse Financière")

company = st.selectbox("Sélectionnez une entreprise:", ['APPLE', 'MICROSOFT', 'TESLA'])
indicator = st.selectbox("Sélectionnez un indicateur:", ['revenu', 'cash flow', 'actif', 'passif', 'croissance revenu', 'croissance cash flow', 'croissance actif', 'croissance passif'])

year = st.number_input("Entrez l'année (2015-2024):", min_value=2015, max_value=2024)

# Afficher les données pour une année, entreprise et indicateur donnés
if st.button('Obtenir les données'):
    value = get_data_for_year_and_company(year, company, indicator)
    st.write(f"La valeur de {indicator} pour {company} en {year} est: {value}")
    
    plot_company_graph(company, indicator)
