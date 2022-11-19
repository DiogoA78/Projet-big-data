# Mise en place du docker:

Lancez Docker.
Ouvrez un terminal et rendez vous dans le dossier du projet.
Une fois dans le dossier 'Projet-Big-Data', faites un: 

docker-compose up -d

Puis Lancez:

docker exec -it pyspark_notebook bash

Une fois dans le docker faites un cd work puis:

pip install -r requirements.txt

Pour le Streamlit il est préferable de le lancer un local.