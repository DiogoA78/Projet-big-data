# Mise en place du docker:

Lancez Docker.
Ouvrez un terminal et rendez vous dans le dossier du projet.
Lorsque vous êtes dans le dossier 'Projet_Big_Data', faites un: 

docker-compose up -d

Ouvrez un autre terminal (qui sera le terminal de votre docker), rendez vous dans le dossier du projet et lancez un:

docker exec -it pyspark_notebook bash
