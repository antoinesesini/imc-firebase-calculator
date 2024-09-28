# imc-firebase-calculator
Projet universitaire de découverte des produits Firebase avec une application de calcul d'IMC.

## Présentation
L'application, développée en Python, est présentée sous la forme d'un Jupyter Notebook. Il suffit d'exécuter la première cellule pour générer une interface graphique permettant d'interagir avec une base de données en temps réel sur Firebase.  

L'application permet de saisir le nom, le poids et la taille d'une personne, puis calcule son indice de masse corporelle (IMC). Ces informations sont ensuite stockées dans le cloud via la base de données. L'application offre également la possibilité de rechercher des profils dans la base de données en utilisant le nom de la personne afin de récupérer ses informations.

## Comment lancer l'application
Afin de lancer l'application, il est d'abord nécessaire d'installer les librairies présentes dans le fichier *requirements.txt*.

Pour se connecter à la base de données, vous devez également disposer du fichier *credentials.json*, fourni avec le rendu du projet. Si vous n'avez pas ce fichier, vous devrez vous connecter à votre propre base de données Firebase. Pour cela, générez votre propre *credentials.json* que vous ajouterez au projet et ajustez l'URL de votre base de données à la ligne suivante du fichier *imc.ipynb* :

```python
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your_url.firebaseio.com/'
})
```

Une fois l'application lancée, il ne reste plus qu'à entrer ses informations pour obtenir son IMC et envoyer les données à la base de données, ou bien rechercher un nom pour retrouver l'IMC de la personne dans la base de données.

## Fonctionnement
### Connexion à Firebase

### Calcul de l'IMC et écriture dans la BDD

### Recherche par nom (Lecture dans la BDD)
