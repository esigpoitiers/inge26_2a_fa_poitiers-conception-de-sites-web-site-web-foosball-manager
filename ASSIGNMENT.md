# Spécifications du Projet

Ce projet consiste en une application web de gestion de parties de baby-foot. L'application permet aux utilisateurs de créer, rejoindre et gérer des parties tout en suivant leurs scores et statistiques.

## Fonctionnalités Requises

Ces fonctionnalités constituent le cœur de l'application et doivent être implémentées en priorité.

### Authentification
Les utilisateurs doivent pouvoir créer un compte et se connecter de manière sécurisée.
- Login/Logout avec sessions
- Inscription de nouveaux utilisateurs
- Profils utilisateurs basiques
- Images de profil personnalisées
- Support des comptes administrateurs

### Gestion des Parties
Le système de gestion des parties permet d'organiser et de suivre les matchs en temps réel.
- Création d'une nouvelle partie
- Rejoindre une partie via:
  - un code à 6 chiffres généré aléatoirement
  - un QR code généré côté serveur
- 2 équipes par partie
- Système de score basique
  - Chaque joueur peut marquer un but
- Quitter une partie
- Démarrage/Fin de partie

### États de Jeu
Chaque partie passe par différents états qui définissent son cycle de vie.
- En attente de joueurs supplémentaires (WAITING)
- En cours (IN_PROGRESS)
- Terminé (FINISHED)

### Interface Administrative
Une interface dédiée aux administrateurs pour la gestion et la supervision de l'application.
- Vue de tous les utilisateurs
- Vue de toutes les parties
- Panneau d'administration

## Compétences Techniques à Démontrer

Durant ce projet, vous devrez démontrer votre maîtrise des composants suivants :

### HTML/Formulaires
- Création de formulaires statiques HTML (login, inscription, création de partie)
- Validation native des champs (required, pattern, etc.)
- Structure sémantique des pages

### JavaScript/Interactivité
- Création de formulaires dynamiques
- Mise à jour en temps réel des données (score, état du jeu)
- Manipulation du DOM pour l'interface utilisateur
- Requêtes AJAX pour les interactions avec l'API

### Python/Flask
- Gestion des routes et des contrôleurs
- Manipulation des sessions utilisateur
- Création d'API RESTful
- Intégration avec la base de données
- Protection des routes avec des décorateurs

### Base de Données
- Conception du schéma relationnel
- Création des tables et relations
- Requêtes SQL pour la manipulation des données
- Gestion des transactions

## Fonctionnalités Facultatives

Ces fonctionnalités permettent d'enrichir l'expérience utilisateur mais ne sont pas essentielles au fonctionnement de base.

### Améliorations Authentification
Fonctionnalités additionnelles pour personnaliser l'expérience utilisateur.
- Statistiques détaillées des joueurs (winrate, historique)
- Profils privés/publics

### Améliorations Gameplay
Ajouts qui rendent le jeu plus dynamique et interactif.
- Changement d'équipe dynamique
- Système de buts en temps réel
- Historique des actions de jeu

### API
Points d'accès pour l'intégration avec d'autres services ou applications.
- Endpoints REST pour les données de jeu
- Mises à jour en temps réel
- API administrative

### Statistiques Avancées
Analyse approfondie des performances des joueurs et des équipes.
- Classements
- Graphiques de performance
- Statistiques d'équipe
