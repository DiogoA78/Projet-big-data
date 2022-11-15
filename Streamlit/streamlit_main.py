import streamlit as st
from  PIL import Image
import numpy as np
import pandas as pd
import hydralit_components as hc

st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

#Ucl
df1 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_games.csv", index_col=0)
df2 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_group.csv", index_col=0)
#Ucl C
df3 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_attack.csv", index_col=0)
df4 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_attempt.csv", index_col=0)
df5 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_def.csv", index_col=0)
df6 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_discip.csv", index_col=0)
df7 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_distrib.csv", index_col=0)
df8 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_gk.csv", index_col=0)
df9 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_goals.csv", index_col=0)
df10 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_clubs_key.csv", index_col=0)
#Ucl P
df11 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_attack.csv", index_col=0)
df12 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_attempt.csv", index_col=0)
df13 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_def.csv", index_col=0)
df14 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_discip.csv", index_col=0)
df15 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_distrib.csv", index_col=0)
df16 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_gk.csv", index_col=0)
df17 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_goals.csv", index_col=0)
df18 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/LDC/ucl_players_key.csv", index_col=0)
#El
df19 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_games.csv", index_col=0)
df20 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_group.csv", index_col=0)
#El C
df21 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_attack.csv", index_col=0)
df22 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_attempts.csv", index_col=0)
df23 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_defending.csv", index_col=0)
df24 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_discip.csv", index_col=0)
df25 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_distribution.csv", index_col=0)
df26 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_gk.csv", index_col=0)
df27 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_goals.csv", index_col=0)
df28 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_clubs_key.csv", index_col=0)
#El P
df29 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_player_attack.csv", index_col=0)
df30 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_player_goals.csv", index_col=0)
df31 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_player_key.csv", index_col=0)
df32 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_players_attempts.csv", index_col=0)
df33 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_players_defending.csv", index_col=0)
df34 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_players_discip.csv", index_col=0)
df35 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_players_distribution.csv", index_col=0)
df36 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/EL/el_stats_players_gk.csv", index_col=0)
#Cdm
df37 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/CDM/cdm_group.csv", index_col=0)
df38 = pd.read_csv("C:/Users/diogo/OneDrive/Documents/GitHub/Projet-big-data/dataset/CDM/cdm_games.csv", index_col=0)



menu_data = [
    {'icon': "far fa-futbol",'label':"Home"},
    {'icon': "far fa-futbol",'label':"Champions League"},
    {'icon': "far fa-futbol",'label':"Europa League"},
    {'icon': "far fa-futbol",'label':"World Cup"},
]

menu_id = hc.nav_bar(menu_definition=menu_data)

if menu_id=='Home':
    st.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's \
            standard dummy text ever since the 1500s, when an unknown printer took a galley of type and \
            scrambled it to make a type specimen book. It has survived not only five centuries, but also \
            the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the \
            1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with \
            desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    col1, col2, col3 = st.columns([9,4,9])
    with col2:
        st.image("https://media.tenor.com/NF6ixwAmrTMAAAAd/cristiano-ronaldo-drinking.gif",width=200)
    



if menu_id == 'Champions League':
    if "Club" not in st.session_state:
        st.session_state["Club"] = False
    if "Key stats1" not in st.session_state:
        st.session_state["Key stats1"] = False
    if "Goals1" not in st.session_state:
        st.session_state["Goals1"] = False
    if "Attempt1" not in st.session_state:
        st.session_state["Attempt1"] = False
    if "Distribution1" not in st.session_state:
        st.session_state["Distribution1"] = False
    if "Attacking1" not in st.session_state:
        st.session_state["Attacking1"] = False
    if "Defending1" not in st.session_state:
        st.session_state["Defending1"] = False
    if "Goalkeeping1" not in st.session_state:
        st.session_state["Goalkeeping1"] = False
    if "Disciplinary1" not in st.session_state:
        st.session_state["Disciplinary1"] = False

    if st.sidebar.button("Club"):
        st.session_state["Club"] = not st.session_state["Club"]

    if st.session_state["Club"]:
        if st.sidebar.button("Key Stats"):
            st.session_state["Key stats1"] = not st.session_state["Key stats1"]
        if st.sidebar.button('Goals'):
            st.session_state["Goals1"] = not st.session_state["Goals1"]
        if st.sidebar.button('Attempt'):
            st.session_state["Attempt1"] = not st.session_state["Attempt1"]
        if st.sidebar.button('Distribution'):
            st.session_state["Distribution1"] = not st.session_state["Distribution1"]
        if st.sidebar.button('Attacking'):
            st.session_state["Attacking1"] = not st.session_state["Attacking1"]
        if st.sidebar.button('Defending'):
            st.session_state["Defending1"] = not st.session_state["Defending1"]
        if st.sidebar.button('Goalkeeping'):
            st.session_state["Goalkeeping1"] = not st.session_state["Goalkeeping1"]
        if st.sidebar.button('Disciplinary'):
            st.session_state["Disciplinary1"] = not st.session_state["Disciplinary1"]

    if st.session_state["Key stats1"]:
        st.write(df10.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goals1"]:
        st.write(df9.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attempt1"]:
        st.write(df4.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Distribution1"]:
        st.write(df7.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attacking1"]:
        st.write(df3.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Defending1"]:
        st.write(df5.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goalkeeping1"]:
        st.write(df8.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Disciplinary1"]:
        st.write(df6.to_html(index=False), unsafe_allow_html=True)


    if "Players" not in st.session_state:
        st.session_state["Players"] = False
    if "Key stats2" not in st.session_state:
        st.session_state["Key stats2"] = False
    if "Goals2" not in st.session_state:
        st.session_state["Goals2"] = False
    if "Attempt2" not in st.session_state:
        st.session_state["Attempt2"] = False
    if "Distribution2" not in st.session_state:
        st.session_state["Distribution2"] = False
    if "Attacking2" not in st.session_state:
        st.session_state["Attacking2"] = False
    if "Defending2" not in st.session_state:
        st.session_state["Defending2"] = False
    if "Goalkeeping2" not in st.session_state:
        st.session_state["Goalkeeping2"] = False
    if "Disciplinary2" not in st.session_state:
        st.session_state["Disciplinary2"] = False

    if st.sidebar.button("Players"):
        st.session_state["Players"] = not st.session_state["Players"]

    if st.session_state["Players"]:
        if st.sidebar.button("Key Stats"):
            st.session_state["Key stats2"] = not st.session_state["Key stats2"]
        if st.sidebar.button('Goals'):
            st.session_state["Goals2"] = not st.session_state["Goals2"]
        if st.sidebar.button('Attempt'):
            st.session_state["Attempt2"] = not st.session_state["Attempt2"]
        if st.sidebar.button('Distribution'):
            st.session_state["Distribution2"] = not st.session_state["Distribution2"]
        if st.sidebar.button('Attacking'):
            st.session_state["Attacking2"] = not st.session_state["Attacking2"]
        if st.sidebar.button('Defending'):
            st.session_state["Defending2"] = not st.session_state["Defending2"]
        if st.sidebar.button('Goalkeeping'):
            st.session_state["Goalkeeping2"] = not st.session_state["Goalkeeping2"]
        if st.sidebar.button('Disciplinary'):
            st.session_state["Disciplinary2"] = not st.session_state["Disciplinary2"]

    if st.session_state["Key stats2"]:
        st.write(df18.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goals2"]:
        st.write(df17.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attempt2"]:
        st.write(df12.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Distribution2"]:
        st.write(df15.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attacking2"]:
        st.write(df11.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Defending2"]:
        st.write(df13.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goalkeeping2"]:
        st.write(df16.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Disciplinary2"]:
        st.write(df14.to_html(index=False), unsafe_allow_html=True)
    
    if st.sidebar.button('Games'):
        st.write(df1.to_html(index=False), unsafe_allow_html=True)

    if st.sidebar.button('Group'):
        st.write(df2.to_html(index=False), unsafe_allow_html=True)


if menu_id == 'Europa League':
    if "Club" not in st.session_state:
        st.session_state["Club"] = False
    if "Key stats3" not in st.session_state:
        st.session_state["Key stats3"] = False
    if "Goals3" not in st.session_state:
        st.session_state["Goals3"] = False
    if "Attempt3" not in st.session_state:
        st.session_state["Attempt3"] = False
    if "Distribution3" not in st.session_state:
        st.session_state["Distribution3"] = False
    if "Attacking3" not in st.session_state:
        st.session_state["Attacking3"] = False
    if "Defending3" not in st.session_state:
        st.session_state["Defending3"] = False
    if "Goalkeeping3" not in st.session_state:
        st.session_state["Goalkeeping3"] = False
    if "Disciplinary3" not in st.session_state:
        st.session_state["Disciplinary3"] = False

    if st.sidebar.button("Club"):
        st.session_state["Club"] = not st.session_state["Club"]

    if st.session_state["Club"]:
        if st.sidebar.button("Key Stats"):
            st.session_state["Key stats3"] = not st.session_state["Key stats3"]
        if st.sidebar.button('Goals'):
            st.session_state["Goals3"] = not st.session_state["Goals3"]
        if st.sidebar.button('Attempt'):
            st.session_state["Attempt3"] = not st.session_state["Attempt3"]
        if st.sidebar.button('Distribution'):
            st.session_state["Distribution3"] = not st.session_state["Distribution3"]
        if st.sidebar.button('Attacking'):
            st.session_state["Attacking3"] = not st.session_state["Attacking3"]
        if st.sidebar.button('Defending'):
            st.session_state["Defending3"] = not st.session_state["Defending3"]
        if st.sidebar.button('Goalkeeping'):
            st.session_state["Goalkeeping3"] = not st.session_state["Goalkeeping3"]
        if st.sidebar.button('Disciplinary'):
            st.session_state["Disciplinary3"] = not st.session_state["Disciplinary3"]

    if st.session_state["Key stats3"]:
        st.write(df28.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goals3"]:
        st.write(df27.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attempt3"]:
        st.write(df22.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Distribution3"]:
        st.write(df25.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attacking3"]:
        st.write(df21.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Defending3"]:
        st.write(df23.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goalkeeping3"]:
        st.write(df26.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Disciplinary3"]:
        st.write(df24.to_html(index=False), unsafe_allow_html=True)


    if "Players" not in st.session_state:
        st.session_state["Players"] = False
    if "Key stats4" not in st.session_state:
        st.session_state["Key stats4"] = False
    if "Goals4" not in st.session_state:
        st.session_state["Goals4"] = False
    if "Attempt4" not in st.session_state:
        st.session_state["Attempt4"] = False
    if "Distribution4" not in st.session_state:
        st.session_state["Distribution4"] = False
    if "Attacking4" not in st.session_state:
        st.session_state["Attacking4"] = False
    if "Defending4" not in st.session_state:
        st.session_state["Defending4"] = False
    if "Goalkeeping4" not in st.session_state:
        st.session_state["Goalkeeping4"] = False
    if "Disciplinary4" not in st.session_state:
        st.session_state["Disciplinary4"] = False

    if st.sidebar.button("Players"):
        st.session_state["Players"] = not st.session_state["Players"]

    if st.session_state["Players"]:
        if st.sidebar.button("Key Stats"):
            st.session_state["Key stats4"] = not st.session_state["Key stats4"]
        if st.sidebar.button('Goals'):
            st.session_state["Goals4"] = not st.session_state["Goals4"]
        if st.sidebar.button('Attempt'):
            st.session_state["Attempt4"] = not st.session_state["Attempt4"]
        if st.sidebar.button('Distribution'):
            st.session_state["Distribution4"] = not st.session_state["Distribution4"]
        if st.sidebar.button('Attacking'):
            st.session_state["Attacking4"] = not st.session_state["Attacking4"]
        if st.sidebar.button('Defending'):
            st.session_state["Defending4"] = not st.session_state["Defending4"]
        if st.sidebar.button('Goalkeeping'):
            st.session_state["Goalkeeping4"] = not st.session_state["Goalkeeping4"]
        if st.sidebar.button('Disciplinary'):
            st.session_state["Disciplinary4"] = not st.session_state["Disciplinary4"]

    if st.session_state["Key stats4"]:
        st.write(df31.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goals4"]:
        st.write(df30.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attempt4"]:
        st.write(df32.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Distribution4"]:
        st.write(df35.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Attacking4"]:
        st.write(df29.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Defending4"]:
        st.write(df33.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Goalkeeping4"]:
        st.write(df36.to_html(index=False), unsafe_allow_html=True)
    if st.session_state["Disciplinary4"]:
        st.write(df34.to_html(index=False), unsafe_allow_html=True)
    
    if st.sidebar.button('Games'):
        st.write(df19.to_html(index=False), unsafe_allow_html=True)

    if st.sidebar.button('Group'):
        st.write(df20.to_html(index=False), unsafe_allow_html=True)


if menu_id=='World Cup':
    if st.sidebar.button('Games'):
        st.write(df38.to_html(index=False), unsafe_allow_html=True)

    if st.sidebar.button('Group'):
        st.write(df37.to_html(index=False), unsafe_allow_html=True)