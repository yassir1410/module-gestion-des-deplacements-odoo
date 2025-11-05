# 📖 Guide Utilisateur - Module Employee Travel

## 🚀 Démarrage Rapide

### 👋 Bienvenue dans Employee Travel !

Ce guide vous aidera à maîtriser rapidement l'utilisation du module de gestion des déplacements professionnels.

### 🎯 Première Connexion

1. **Connectez-vous à Odoo** avec vos identifiants
2. **Localisez le menu "Déplacements"** dans la barre de navigation
3. **Cliquez sur "Mes Demandes"** pour accéder à vos demandes

---

## 👤 Guide Employé

### 📝 Créer une Nouvelle Demande

#### **Étape 1 : Accéder au formulaire**
```
Menu Déplacements → Mes Demandes → [+ Créer]
```

#### **Étape 2 : Remplir les informations obligatoires**

**🔹 Informations Générales**
- **Objet** : Décrivez brièvement le motif (ex: "Formation technique", "Réunion client")
- **Employé** : Automatiquement rempli avec votre nom
- **Ordre de mission** : Joindre le document si requis

**🔹 Dates et Destination**
- **Date de début** : Date de départ
- **Date de fin** : Date de retour
- **Pays de destination** : Sélectionner dans la liste
- **Ville de destination** : Préciser la ville
- **Distance estimée** : En kilomètres

**🔹 Transport**
- **Mode de transport** : Véhicule, Avion, Train, Autre
- **Véhicule** : Si transport en véhicule de service
- **Classe avion** : Automatiquement définie selon la distance

#### **Étape 3 : Vérifier les calculs automatiques**
- **Nombre de jours** : Calculé automatiquement
- **Montant** : Calculé selon la destination (700 DH national, 1500 DH international)

#### **Étape 4 : Soumettre la demande**
- Cliquer sur **"Soumettre"**
- Confirmer dans la popup
- Votre demande passe à l'état "Soumise"

### 📊 Suivre vos Demandes

#### **États possibles de vos demandes :**

| État | Description | Action de votre part |
|------|-------------|---------------------|
| 🔵 **Brouillon** | En cours de création | Compléter et soumettre |
| 🔶 **Soumise** | En attente validation manager | Attendre |
| 🔶 **En cours** | En cours d'examen | Attendre |
| ✅ **Approuvée** | Validée par manager, envoyée DAF | Attendre |
| 🔶 **DAF Review** | En cours validation DAF | Attendre |
| ✅ **DAF Approuvée** | Validée définitivement | Préparer voyage |
| ✅ **Terminée** | Déplacement clôturé | Aucune |
| ❌ **Refusée** | Demande refusée | Voir motif, corriger |

#### **Notifications que vous recevrez :**
- ✅ Confirmation de soumission
- ✅ Validation par votre manager
- ✅ Validation finale par la DAF
- ❌ Notification de refus avec motif

### 💡 Conseils Pratiques

#### **Pour une demande acceptée rapidement :**
- ✅ Remplir tous les champs obligatoires
- ✅ Justifier clairement l'objet du déplacement
- ✅ Respecter les délais de préavis (48h minimum)
- ✅ Joindre l'ordre de mission si requis
- ✅ Vérifier la cohérence des dates

#### **Erreurs courantes à éviter :**
- ❌ Dates incohérentes (fin avant début)
- ❌ Distance inexacte (impact sur transport autorisé)
- ❌ Objet trop vague ("Déplacement")
- ❌ Oubli de l'ordre de mission pour international

---

## 👨‍💼 Guide Manager

### 🔍 Accéder aux Demandes à Valider

#### **Menus disponibles :**
```
Déplacements
├── 📋 Mes Demandes (vos propres demandes)
├── ⏳ À Valider (demandes en attente)
├── 📊 Toutes les Demandes (vue d'ensemble)
└── 🚗 Véhicules (gestion des véhicules)
```

### ✅ Processus de Validation

#### **Étape 1 : Examiner la demande**
1. **Ouvrir** la demande depuis "À Valider"
2. **Vérifier** la cohérence des informations
3. **Évaluer** la pertinence métier
4. **Contrôler** le budget et les dates

#### **Étape 2 : Prendre une décision**

**🔵 Pour Prendre en Cours :**
```
Bouton "Prendre en cours" → Demande passe en "En cours"
```

**✅ Pour Approuver :**
```
Bouton "Approuver" → Demande passe en "Approuvée"
Puis "Envoyer à la DAF" → Demande envoyée pour validation finale
```

**❌ Pour Refuser :**
```
Bouton "Refuser" → Saisir motif → Demande passe en "Refusée"
```

**🔄 Pour Remettre en Brouillon :**
```
Bouton "Reprendre en brouillon" → Employé peut modifier
```

### 📊 Suivi et Reporting

#### **Tableau de bord Manager**
- Demandes en attente de votre validation
- Délais de traitement de votre équipe
- Budget consommé par service
- Statistiques de validation

#### **Bonnes Pratiques de Validation**
- ✅ **Délai de réponse** : <24h pour maintenir la fluidité
- ✅ **Justification des refus** : Motif clair et constructif
- ✅ **Cohérence d'équipe** : Critères uniformes
- ✅ **Anticipation budget** : Suivi régulier des dépenses

---

## 🏛️ Guide DAF

### 💰 Validation Financière

#### **Accès aux demandes DAF :**
```
Déplacements → Traitement DAF
```

#### **Critères de validation DAF :**
- **Budget disponible** : Vérifier l'enveloppe budgétaire
- **Conformité financière** : Respect des procédures
- **Justification coût** : Rapport coût/bénéfice
- **Autorisation hiérarchique** : Validation manager préalable

### 🔍 Processus de Validation DAF

#### **Étape 1 : Révision financière**
1. **Analyser** le montant et la justification
2. **Vérifier** la disponibilité budgétaire
3. **Contrôler** la conformité aux procédures
4. **Évaluer** l'impact financier

#### **Étape 2 : Décision finale**

**✅ Pour Valider :**
```
Bouton "Valider DAF" → Demande approuvée définitivement
```

**❌ Pour Refuser :**
```
Bouton "Refuser" → Saisir motif financier → Demande refusée
```

**✅ Pour Clôturer :**
```
Bouton "Marquer terminé" → Déplacement terminé (après réalisation)
```

### 📈 Reporting Financier

#### **Tableaux de bord DAF**
- Budget global des déplacements
- Répartition par service/département
- Évolution mensuelle des coûts
- Prévisions budgétaires

#### **Indicateurs Clés**
- **Coût moyen par déplacement**
- **Budget consommé vs alloué**
- **Tendances par destination**
- **ROI des déplacements commerciaux**

---

## 🎨 Interface et Navigation

### 📱 Vue d'Ensemble de l'Interface

#### **Barre de Navigation**
```
[🏠 Accueil] [💼 Apps] [🚗 Déplacements] [⚙️ Paramètres]
```

#### **Menu Déplacements Détaillé**

**Pour Employé :**
```
🚗 Déplacements
└── 📋 Mes Demandes
    ├── [+ Créer] Nouvelle demande
    ├── 🔍 Filtres (État, Dates, etc.)
    └── 📊 Mes statistiques
```

**Pour Manager :**
```
🚗 Déplacements
├── 📋 Mes Demandes
├── ⏳ À Valider (🔴 Badge si demandes en attente)
├── 📊 Toutes les Demandes
└── 🚗 Véhicules
```

**Pour DAF :**
```
🚗 Déplacements
├── 📋 Mes Demandes
├── 💰 Traitement DAF (🔴 Badge si demandes en attente)
├── 📊 Toutes les Demandes
└── 🚗 Véhicules
```

### 🎨 Codes Couleur

#### **États des Demandes :**
- 🔵 **Bleu** : Soumise (action requise)
- 🔶 **Orange** : En cours, DAF Review (en traitement)
- ✅ **Vert** : Approuvée, DAF Approuvée, Terminée
- ⚪ **Gris** : Refusée, Annulée
- 📝 **Blanc** : Brouillon

#### **Boutons d'Action :**
- 🔵 **Bleu Primary** : Actions principales (Soumettre)
- ✅ **Vert Success** : Validations (Approuver)
- 🔶 **Orange Warning** : Transitions (Envoyer DAF)
- 🔵 **Cyan Info** : Actions de process (Prendre en cours)
- ❌ **Rouge Danger** : Refus
- ⚪ **Gris Secondary** : Actions annexes

### 📋 Filtres et Recherches

#### **Filtres Rapides Disponibles :**
- **Mes demandes en cours**
- **Demandes de ce mois**
- **Demandes internationales**
- **Demandes à valider**
- **Déplacements terminés**

#### **Recherche Avancée :**
```
🔍 Rechercher par :
├── Nom de la demande
├── Nom de l'employé
├── Destination
├── Dates de déplacement
└── Montant
```

#### **Groupements Possibles :**
- Par état
- Par employé
- Par destination
- Par mois
- Par service

---

## 💡 Conseils et Bonnes Pratiques

### 🎯 Pour tous les Utilisateurs

#### **Optimisation de l'Utilisation :**
- ✅ **Marque-pages** : Ajouter "Déplacements" en favori
- ✅ **Notifications** : Activer les notifications email
- ✅ **Filtres personnalisés** : Créer ses propres filtres
- ✅ **Formation régulière** : Participer aux sessions de formation

#### **Sécurité et Bonnes Pratiques :**
- 🔒 **Mot de passe fort** : Changer régulièrement
- 🔐 **Déconnexion** : Se déconnecter après utilisation
- 📝 **Sauvegarde** : Conserver les documents importants
- 🔄 **Mise à jour** : Signaler les bugs ou améliorations

### 📈 Optimisation des Processus

#### **Réduction des Délais :**
- ⚡ **Préparation** : Rassembler tous les documents avant saisie
- ⚡ **Standardisation** : Utiliser des modèles de description
- ⚡ **Anticipation** : Soumettre les demandes dès que possible
- ⚡ **Communication** : Informer en cas d'urgence

#### **Amélioration de la Qualité :**
- 📊 **Suivi régulier** : Consulter les statistiques
- 🎯 **Formation continue** : Améliorer ses pratiques
- 💬 **Feedback** : Participer aux enquêtes d'amélioration
- 🔄 **Processus** : Respecter le workflow établi

---

## 🆘 Aide et Support

### 📞 Contacts Rapides

#### **Support Utilisateur :**
- **Email** : support-user@employee-travel.com
- **Téléphone** : +212 5XX XX XX XX
- **Chat** : Disponible dans l'interface Odoo

#### **Formation et Documentation :**
- **Vidéos tutoriels** : https://tutorials.employee-travel.com
- **FAQ** : https://faq.employee-travel.com
- **Forum** : https://community.employee-travel.com

### 🔧 Résolution de Problèmes Courants

#### **"Je ne peux pas soumettre ma demande"**
**Causes possibles :**
- Champs obligatoires manquants
- Dates incohérentes
- Distance/transport incompatibles

**Solutions :**
1. Vérifier tous les champs marqués (*)
2. Contrôler les dates (fin ≥ début)
3. Adapter le transport à la distance

#### **"Je ne vois pas les demandes de mon équipe"**
**Causes possibles :**
- Droits insuffisants
- Pas de groupe "Travel Manager"

**Solutions :**
1. Contacter l'administrateur système
2. Vérifier votre profil utilisateur

#### **"Le calcul de montant est incorrect"**
**Causes possibles :**
- Pays mal configuré
- Dates incorrectes

**Solutions :**
1. Vérifier le pays de destination
2. Contrôler les dates de début/fin
3. Actualiser la page (F5)

### 📚 Ressources d'Apprentissage

#### **Parcours de Formation Recommandé :**

**Niveau Débutant (30 min) :**
1. 📹 Vidéo : "Première demande de déplacement"
2. 📖 Guide : "Interface et navigation"
3. 🎯 Exercice : Créer sa première demande

**Niveau Intermédiaire (1h) :**
1. 📹 Vidéo : "Optimiser ses demandes"
2. 📖 Guide : "Bonnes pratiques"
3. 🎯 Exercice : Gérer plusieurs demandes

**Niveau Avancé (Manager/DAF - 2h) :**
1. 📹 Vidéo : "Processus de validation"
2. 📖 Guide : "Reporting et suivi"
3. 🎯 Exercice : Tableau de bord personnalisé

#### **Certifications Disponibles :**
- 🏆 **Utilisateur Certifié** : Maîtrise de base
- 🏆 **Manager Certifié** : Validation et suivi
- 🏆 **Expert DAF** : Gestion financière avancée

---

## 📋 Mémo de Référence Rapide

### ⚡ Actions Rapides

| Vous voulez... | Raccourci/Action |
|----------------|------------------|
| **Créer une demande** | Menu Déplacements → Mes Demandes → [+] |
| **Voir mes demandes** | Menu Déplacements → Mes Demandes |
| **Valider des demandes** | Menu Déplacements → À Valider |
| **Voir toutes les demandes** | Menu Déplacements → Toutes les Demandes |
| **Chercher une demande** | 🔍 + nom/destination/employé |
| **Filtrer par état** | Clic sur l'état dans la vue liste |

### 🔄 Workflow en un Coup d'Œil

```
📝 CRÉER → ✅ SOUMETTRE → 👨‍💼 MANAGER → 🏛️ DAF → ✅ TERMINÉ
   ↓           ↓            ↓          ↓         ↓
 Brouillon  Soumise    En cours/   DAF Review  Terminée
                      Approuvée   /Approuvée
```

### 📱 Raccourcis Clavier

| Raccourci | Action |
|-----------|--------|
| **Ctrl + S** | Sauvegarder |
| **Ctrl + E** | Éditer |
| **Ctrl + N** | Nouveau |
| **Échap** | Annuler |
| **F5** | Actualiser |

---

**🎯 Avec ce guide, vous êtes prêt à utiliser efficacement le module Employee Travel !**

*Pour toute question complémentaire, n'hésitez pas à consulter la documentation complète ou contacter le support.*

---

**© 2025 Employee Travel Solutions - Guide Utilisateur v1.0**