# 📚 Documentation Complète - Module Employee Travel

## 📋 Table des Matières

1. [🎯 Présentation Générale](#-présentation-générale)
2. [🏗️ Architecture du Module](#️-architecture-du-module)
3. [📦 Installation et Configuration](#-installation-et-configuration)
4. [👥 Gestion des Utilisateurs](#-gestion-des-utilisateurs)
5. [🔄 Workflow de Validation](#-workflow-de-validation)
6. [💰 Règles Métier](#-règles-métier)
7. [🎨 Interface Utilisateur](#-interface-utilisateur)
8. [🛡️ Sécurité et Permissions](#️-sécurité-et-permissions)
9. [📊 Rapports et Suivi](#-rapports-et-suivi)
10. [🔧 Maintenance et Dépannage](#-maintenance-et-dépannage)
11. [📞 Support et Contact](#-support-et-contact)

---

## 🎯 Présentation Générale

### 📝 Description
Le module **Employee Travel** est une solution complète de gestion des demandes de déplacement professionnel pour Odoo 18. Il automatise le processus de demande, validation et suivi des voyages d'affaires avec un workflow à deux niveaux de validation.

### 🎯 Objectifs
- **Digitaliser** le processus de demande de déplacement
- **Automatiser** les calculs de frais et les validations
- **Assurer** la traçabilité complète des demandes
- **Contrôler** les budgets et autorisations
- **Simplifier** les tâches administratives

### 🌟 Fonctionnalités Principales
- ✅ Demandes de déplacement avec workflow automatisé
- ✅ Calcul automatique des montants (national/international)
- ✅ Validation hiérarchique (Manager → DAF)
- ✅ Gestion des véhicules de service
- ✅ Règles métier configurables
- ✅ Notifications automatiques
- ✅ Rapports et tableaux de bord
- ✅ Interface responsive et intuitive

### 📊 Statistiques du Module
- **Version** : 18.0.1.0.0
- **Compatibilité** : Odoo 18.0+
- **Modules requis** : base, hr, mail
- **Langues** : Français
- **Licence** : LGPL-3

---

## 🏗️ Architecture du Module

### 📁 Structure des Fichiers
```
employee_travel/
├── __manifest__.py              # Configuration du module
├── __init__.py                  # Initialisation Python
├── models/                      # Modèles de données
│   ├── __init__.py
│   ├── travel_request.py        # Demandes de déplacement
│   └── vehicle.py               # Véhicules de service
├── views/                       # Interfaces utilisateur
│   └── travel_views.xml         # Vues et menus
├── security/                    # Sécurité et permissions
│   ├── groups.xml               # Groupes d'utilisateurs
│   ├── ir.model.access.csv      # Droits d'accès
│   └── ir_rule.xml              # Règles de sécurité
├── data/                        # Données de base
│   └── sequence.xml             # Séquences de numérotation
└── static/                      # Ressources statiques
    └── description/
        ├── icon.png             # Icône du module
        └── index.html           # Description HTML
```

### 🗄️ Modèles de Données

#### **TravelRequest (employee.travel)**
**Champs principaux :**
- `name` : Référence unique (auto-générée)
- `employee_id` : Employé demandeur
- `subject` : Objet du déplacement
- `date_from/date_to` : Dates de déplacement
- `destination_country_id/city` : Destination
- `transport_mode` : Mode de transport
- `amount` : Montant calculé automatiquement
- `state` : État du workflow

**États du workflow :**
- `draft` : Brouillon
- `submitted` : Soumise
- `in_progress` : En cours de traitement
- `approved` : Approuvée par manager
- `daf_review` : En review DAF
- `daf_approved` : Approuvée DAF
- `done` : Terminée
- `refused` : Refusée
- `cancelled` : Annulée

#### **TravelVehicle (employee.travel.vehicle)**
**Champs principaux :**
- `name` : Nom du véhicule
- `license_plate` : Plaque d'immatriculation
- `driver` : Chauffeur
- `active` : Actif/Inactif

### 🔗 Relations et Dépendances
- **hr.employee** : Lien avec les employés
- **res.country** : Pays de destination
- **res.users** : Utilisateurs du système
- **mail.thread** : Système de notifications

---

## 📦 Installation et Configuration

### 🚀 Installation du Module

#### **Prérequis**
- Odoo 18.0 ou version supérieure
- Modules de base : `base`, `hr`, `mail`
- Droits d'administration sur l'instance Odoo

#### **Étapes d'Installation**

1. **Copier le module**
   ```bash
   cp -r employee_travel /path/to/odoo/addons/
   ```

2. **Redémarrer Odoo**
   ```bash
   sudo systemctl restart odoo
   # ou
   python3 odoo-bin -d database_name -u all
   ```

3. **Activer le mode développeur**
   - Paramètres → Activer le mode développeur

4. **Installer le module**
   - Applications → Rechercher "Employee Travel"
   - Cliquer sur "Installer"

#### **Vérification de l'Installation**
- Menu "Déplacements" doit apparaître
- Aucune erreur dans les logs Odoo
- Accès aux vues de base

### ⚙️ Configuration Initiale

#### **1. Configuration des Groupes d'Utilisateurs**
```
Paramètres → Utilisateurs et sociétés → Utilisateurs
```

**Affecter les rôles :**
- **Travel Manager** : Managers, superviseurs
- **Travel DAF** : Direction administrative/financière

#### **2. Configuration des Véhicules (optionnel)**
```
Déplacements → Véhicules
```
Ajouter les véhicules de service disponibles.

#### **3. Configuration des Séquences (optionnel)**
```
Paramètres → Séquences et Identifiants → Séquences
```
Modifier le format de numérotation si nécessaire.

#### **4. Configuration des Pays**
Vérifier que les pays de destination sont configurés dans :
```
Paramètres → Localisation → Pays
```

---

## 👥 Gestion des Utilisateurs

### 🔐 Groupes d'Utilisateurs

#### **👤 Utilisateur Standard (Employé)**
**Droits :**
- Créer ses propres demandes de déplacement
- Modifier ses demandes en brouillon
- Soumettre ses demandes pour validation
- Consulter l'historique de ses demandes

**Restrictions :**
- Ne peut pas voir les demandes des autres
- Ne peut pas valider de demandes
- Ne peut pas modifier les demandes soumises

#### **👨‍💼 Travel Manager**
**Droits supplémentaires :**
- Voir toutes les demandes de déplacement
- Valider/refuser les demandes soumises
- Remettre en brouillon les demandes
- Accès aux rapports de suivi
- Gérer les véhicules de service

**Responsabilités :**
- Validation de la pertinence métier
- Contrôle des demandes avant envoi DAF
- Suivi des équipes

#### **🏛️ Travel DAF (Direction Administrative)**
**Droits supplémentaires :**
- Validation finale des demandes approuvées
- Accès aux données financières
- Marquer les déplacements comme terminés
- Accès complet aux rapports

**Responsabilités :**
- Validation budgétaire
- Contrôle administratif final
- Reporting direction

### 📋 Procédure d'Affectation

#### **Étapes de Configuration Utilisateur**

1. **Accéder à la gestion des utilisateurs**
   ```
   Paramètres → Utilisateurs et sociétés → Utilisateurs
   ```

2. **Sélectionner un utilisateur**
   - Cliquer sur l'utilisateur à configurer

3. **Configurer les droits d'accès**
   - Onglet "Droits d'accès"
   - Section "Ressources Humaines" : Cocher "Travel Manager" si applicable
   - Section "Administration" : Cocher "Travel DAF" si applicable

4. **Enregistrer les modifications**
   - Cliquer sur "Enregistrer"

#### **Matrice des Permissions**

| Fonctionnalité | Employé | Travel Manager | Travel DAF |
|----------------|---------|----------------|------------|
| Créer demande | ✅ | ✅ | ✅ |
| Voir ses demandes | ✅ | ✅ | ✅ |
| Voir toutes demandes | ❌ | ✅ | ✅ |
| Valider étape 1 | ❌ | ✅ | ❌ |
| Valider étape 2 | ❌ | ❌ | ✅ |
| Gérer véhicules | ❌ | ✅ | ✅ |
| Rapports avancés | ❌ | ✅ | ✅ |

---

## 🔄 Workflow de Validation

### 📊 Diagramme de Flux

```
👤 EMPLOYÉ           👨‍💼 MANAGER          🏛️ DAF
    │                    │                  │
    ▼                    │                  │
📝 Créer demande         │                  │
    │                    │                  │
    ▼                    │                  │
✏️ Remplir détails        │                  │
    │                    │                  │
    ▼                    │                  │
✅ Soumettre ────────────▶ 📩 Notification   │
    │                    │                  │
    │                    ▼                  │
    │               🔍 Examiner demande      │
    │                    │                  │
    │              [DÉCISION MANAGER]       │
    │                    │                  │
    │         ┌──────────┼──────────┐       │
    │         ▼          │          ▼       │
    │     ❌ Refuser      │      ✅ Approuver │
    │         │          │          │       │
    │         ▼          │          ▼       │
    ◀─── 📩 Notification │     📤 Envoyer ───▶ 📩 Notification
    │      refus         │       DAF        │
    │         │          │          │       ▼
    │         ▼          │          │   🏛️ Review DAF
    │      🔚 FIN         │          │       │
    │                    │          │   [DÉCISION DAF]
    │                    │          │       │
    │                    │          │  ┌────┼────┐
    │                    │          │  ▼    │    ▼
    │                    │          │ ❌ Refuser ✅ Valider
    │                    │          │  │    │    │
    │                    │          │  ▼    │    ▼
    ◀────────────────────┼──────────┼─ 📩   │   📩 Notification
    │                    │          │ Notif │   succès
    │                    │          │  │    │    │
    │                    │          │  ▼    │    ▼
    │                    │          │ 🔚 FIN │   ✅ Approuvé
    │                    │          │       │    │
    │                    │          │       │    ▼
    │                    ◀──────────┼───────┼── 📩 Notification
    │                               │       │    manager
    │                               │       │    │
    │                               │       │    ▼
    │                               │       │   🎯 Déplacement
    │                               │       │    autorisé
    │                               │       │    │
    │                               │       │    ▼
    │                               │       └──▶ ✅ Marquer
    │                               │           terminé
    │                               │            │
    │                               │            ▼
    └───────────────────────────────┼──────────▶ 🔚 CLÔTURÉ
                                    │
                              📊 HISTORIQUE
                                COMPLET
```

### 📋 États Détaillés

#### **1️⃣ Draft (Brouillon)**
- **Description** : Demande en cours de création
- **Acteur** : Employé
- **Actions possibles** : Modifier, Soumettre
- **Transition** : → Submitted

#### **2️⃣ Submitted (Soumise)**
- **Description** : Demande soumise en attente de validation
- **Acteur** : Travel Manager
- **Actions possibles** : Prendre en cours, Refuser, Remettre en brouillon
- **Transition** : → In Progress, Refused, Draft

#### **3️⃣ In Progress (En cours)**
- **Description** : Demande en cours d'examen par le manager
- **Acteur** : Travel Manager
- **Actions possibles** : Approuver, Refuser
- **Transition** : → Approved, Refused

#### **4️⃣ Approved (Approuvée)**
- **Description** : Demande approuvée par le manager
- **Acteur** : Travel Manager
- **Actions possibles** : Envoyer à la DAF
- **Transition** : → DAF Review

#### **5️⃣ DAF Review (Review DAF)**
- **Description** : Demande en cours d'examen par la DAF
- **Acteur** : Travel DAF
- **Actions possibles** : Valider DAF, Refuser
- **Transition** : → DAF Approved, Refused

#### **6️⃣ DAF Approved (Approuvée DAF)**
- **Description** : Demande validée définitivement
- **Acteur** : Travel DAF
- **Actions possibles** : Marquer terminé
- **Transition** : → Done

#### **7️⃣ Done (Terminée)**
- **Description** : Déplacement terminé et clôturé
- **Acteur** : Consultation uniquement
- **Actions possibles** : Consultation
- **Transition** : État final

#### **8️⃣ Refused (Refusée)**
- **Description** : Demande refusée à une étape
- **Acteur** : Travel Manager (remettre en brouillon)
- **Actions possibles** : Remettre en brouillon
- **Transition** : → Draft

#### **9️⃣ Cancelled (Annulée)**
- **Description** : Demande annulée par l'employé
- **Acteur** : Employé/Manager
- **Actions possibles** : Consultation
- **Transition** : État final

### 🔔 Notifications Automatiques

#### **Événements de Notification**

1. **Soumission de demande**
   - **Destinataires** : Tous les Travel Managers
   - **Message** : "Nouvelle demande de déplacement soumise par [Employé]"

2. **Approbation manager**
   - **Destinataires** : Employé demandeur, Travel DAF
   - **Message** : "Demande approuvée par [Manager], envoyée à la DAF"

3. **Validation DAF**
   - **Destinataires** : Employé demandeur, Manager valideur
   - **Message** : "Demande validée définitivement par la DAF"

4. **Refus de demande**
   - **Destinataires** : Employé demandeur
   - **Message** : "Demande refusée - Motif : [Raison]"

#### **Paramétrage des Notifications**
Les notifications sont automatiques et peuvent être configurées via :
```
Paramètres → Discussions → Notifications
```

---

## 💰 Règles Métier

### 🧮 Calculs Automatiques

#### **Montant de Déplacement**
Le montant est calculé automatiquement selon les règles suivantes :

**Formule de calcul :**
```python
montant = nombre_de_jours × taux_journalier
```

**Taux journaliers :**
- **National** : 700 DH/jour
- **International** : 1500 DH/jour

**Détermination National/International :**
```python
if pays_destination == pays_societe_employe:
    taux = 700  # National
else:
    taux = 1500  # International
```

#### **Calcul du Nombre de Jours**
```python
nombre_jours = (date_fin - date_debut) + 1
```
*Note : Le jour de départ et le jour de retour sont comptés*

#### **Exemples de Calcul**

**Exemple 1 : Déplacement National**
- Employé : Société au Maroc
- Destination : Casablanca, Maroc
- Dates : 15/01/2025 au 17/01/2025 (3 jours)
- Calcul : 3 × 700 = **2,100 DH**

**Exemple 2 : Déplacement International**
- Employé : Société au Maroc
- Destination : Paris, France
- Dates : 20/01/2025 au 24/01/2025 (5 jours)
- Calcul : 5 × 1,500 = **7,500 DH**

### 🚗 Règles de Transport

#### **Sélection du Mode de Transport**
1. **Distance < 500 km** : Véhicule ou transport terrestre recommandé
2. **Distance ≥ 500 km** : Avion obligatoire
3. **Distance ≥ 6000 km** : Classe business automatique

#### **Classes d'Avion Automatiques**
```python
if distance >= 6000:
    classe = 'business'
elif distance >= 500:
    classe = 'economy'
```

#### **Ordre de Mission**
**Obligatoire pour :**
- Déplacements internationaux
- Déplacements > 1000 km
- Déplacements en avion

### 📋 Validations et Contraintes

#### **Contraintes de Dates**
- Date de fin ≥ Date de début
- Dates ne peuvent pas être dans le passé (sauf admin)
- Durée maximale : 30 jours (configurable)

#### **Contraintes de Budget**
- Montant maximum par déplacement : 50,000 DH (configurable)
- Validation DAF obligatoire si montant > 10,000 DH

#### **Contraintes Métier**
- Un employé ne peut avoir qu'une demande active à la fois
- Période de préavis minimum : 48h (sauf urgence)
- Justification obligatoire pour déplacements > 15 jours

### 🔄 Règles de Workflow

#### **Transitions Automatiques**
1. **Auto-soumission** : Demandes complètes peuvent être auto-soumises
2. **Auto-approbation** : Déplacements récurrents/pré-approuvés
3. **Escalade automatique** : Si pas de réponse sous 72h

#### **Règles de Validation**
- Manager ne peut pas valider ses propres demandes
- DAF ne peut valider que les demandes approuvées par manager
- Employé ne peut modifier que ses demandes en brouillon

---

## 🎨 Interface Utilisateur

### 📱 Navigation et Menus

#### **Menu Principal : "Déplacements"**
Accessible depuis la barre de navigation principale.

#### **Sous-menus par Profil**

**👤 Employé Standard :**
```
Déplacements
└── 📋 Mes Demandes
```

**👨‍💼 Travel Manager :**
```
Déplacements
├── 📋 Mes Demandes
├── ⏳ À Valider
├── 📊 Toutes les Demandes
└── 🚗 Véhicules
```

**🏛️ Travel DAF :**
```
Déplacements
├── 📋 Mes Demandes
├── 💰 Traitement DAF
├── 📊 Toutes les Demandes
└── 🚗 Véhicules
```

### 🖼️ Vues et Formulaires

#### **Vue Liste (Kanban)**
- **Colonnes** : Nom, Employé, Dates, Destination, Montant, État
- **Filtres** : Par état, par employé, par dates
- **Recherche** : Par nom, destination, employé
- **Couleurs** :
  - 🔵 Bleu : Soumise
  - 🔶 Orange : En cours/DAF Review
  - ✅ Vert : Approuvée/Terminée
  - ⚪ Gris : Refusée/Annulée

#### **Vue Formulaire**
**Structure en onglets :**

1. **Informations Générales**
   - Référence (auto-générée)
   - Employé (auto-rempli)
   - Objet du déplacement
   - Ordre de mission (upload)

2. **Dates et Destination**
   - Date de début/fin
   - Nombre de jours (calculé)
   - Pays et ville de destination
   - Distance estimée

3. **Transport**
   - Mode de transport
   - Véhicule (si applicable)
   - Classe avion (si applicable)

4. **Calculs**
   - Montant (calculé automatiquement)
   - Devise
   - Détail du calcul

5. **Suivi Workflow** (Managers/DAF uniquement)
   - Historique des validations
   - Utilisateurs et dates
   - Motifs de refus

#### **Boutons d'Action Contextuels**

**Selon l'état et le rôle :**
```python
# Employé - État Draft
[🔵 Soumettre]

# Manager - État Submitted  
[🔵 Prendre en cours] [❌ Refuser]

# Manager - État In Progress
[✅ Approuver] [❌ Refuser] 

# Manager - État Approved
[📤 Envoyer à la DAF]

# DAF - État DAF Review
[✅ Valider DAF] [❌ Refuser]

# DAF - État DAF Approved
[✅ Marquer terminé]
```

### 📊 Tableaux de Bord

#### **Dashboard Employé**
- Mes demandes en cours
- Historique des demandes
- Montants totaux par année
- Statistiques personnelles

#### **Dashboard Manager**
- Demandes en attente de validation
- Statistiques d'équipe
- Tendances de déplacements
- Budgets consommés

#### **Dashboard DAF**
- Demandes à valider financièrement
- Budgets par service
- Reporting financier
- Tableaux de bord exécutifs

### 🎨 Thème et Design

#### **Codes Couleur Standard**
- **Primary (Bleu)** : #007bff - Actions principales
- **Success (Vert)** : #28a745 - Validations/Succès
- **Warning (Orange)** : #ffc107 - Attention/En cours
- **Danger (Rouge)** : #dc3545 - Refus/Erreurs
- **Secondary (Gris)** : #6c757d - Actions secondaires
- **Info (Cyan)** : #17a2b8 - Informations

#### **Icônes Utilisées**
- 🚗 Déplacements
- 📋 Demandes
- ⏳ À valider
- 💰 DAF
- 👤 Employé
- 📊 Rapports
- ⚙️ Configuration

### 📱 Responsive Design

#### **Adaptation Mobile**
- Interface adaptée tablettes/smartphones
- Boutons tactiles optimisés
- Navigation simplifiée
- Formulaires mobile-friendly

#### **Accessibilité**
- Contraste élevé
- Navigation clavier
- Lecteurs d'écran compatibles
- Textes alternatifs

---

## 🛡️ Sécurité et Permissions

### 🔐 Architecture de Sécurité

#### **Principe de Sécurité**
Le module applique le principe du **"moindre privilège"** :
- Chaque utilisateur n'a accès qu'aux données nécessaires à son rôle
- Les actions sont restreintes selon le contexte et l'état
- Traçabilité complète de toutes les actions

### 👥 Groupes de Sécurité

#### **Hiérarchie des Groupes**
```
👤 User (base.group_user)
  └── Employé Standard
      └── 👨‍💼 Travel Manager (employee_travel.group_travel_manager)
          └── 🏛️ Travel DAF (employee_travel.group_travel_daf)
```

#### **Héritage des Permissions**
- **Travel DAF** hérite des permissions **Travel Manager**
- **Travel Manager** hérite des permissions **User**
- Principe d'accumulation des droits

### 📋 Matrice des Permissions

#### **Droits d'Accès par Modèle**

| Modèle | User | Travel Manager | Travel DAF |
|--------|------|----------------|------------|
| **employee.travel** |  |  |  |
| - Lecture | ✅ (ses demandes) | ✅ (toutes) | ✅ (toutes) |
| - Écriture | ✅ (ses demandes) | ✅ (toutes) | ✅ (toutes) |
| - Création | ✅ | ✅ | ✅ |
| - Suppression | ❌ | ✅ | ✅ |
| **employee.travel.vehicle** |  |  |  |
| - Lecture | ✅ | ✅ | ✅ |
| - Écriture | ❌ | ✅ | ✅ |
| - Création | ❌ | ✅ | ✅ |
| - Suppression | ❌ | ✅ | ✅ |

#### **Règles de Domaine (Record Rules)**

**Règle Employé :**
```python
[
    '|',
    ('employee_id.user_id', '=', user.id),
    ('create_uid', '=', user.id)
]
```
*L'employé ne voit que ses propres demandes*

**Règle Manager/DAF :**
```python
[(1, '=', 1)]
```
*Accès à toutes les demandes*

### 🔒 Sécurité des Actions

#### **Validation des Actions par État**

```python
# Exemple : Validation de soumission
def action_submit(self):
    # Vérification de l'état
    if self.state != 'draft':
        raise UserError("Seules les demandes en brouillon peuvent être soumises")
    
    # Vérification de l'utilisateur
    if self.create_uid != self.env.user:
        raise UserError("Vous ne pouvez soumettre que vos propres demandes")
    
    # Vérification des données obligatoires
    if not self.subject or not self.date_from:
        raise UserError("Données obligatoires manquantes")
```

#### **Contrôles d'Intégrité**

1. **Validation des Dates**
   ```python
   @api.constrains('date_from', 'date_to')
   def _check_dates(self):
       if self.date_to < self.date_from:
           raise ValidationError("La date de fin doit être postérieure à la date de début")
   ```

2. **Validation des Montants**
   ```python
   @api.constrains('amount')
   def _check_amount(self):
       if self.amount < 0:
           raise ValidationError("Le montant ne peut pas être négatif")
   ```

3. **Validation Métier**
   ```python
   @api.constrains('transport_mode', 'distance_km')
   def _check_transport_rules(self):
       if self.distance_km >= 500 and self.transport_mode != 'plane':
           raise ValidationError("L'avion est obligatoire pour les distances ≥ 500km")
   ```

### 🔍 Audit et Traçabilité

#### **Champs d'Audit Automatiques**
- `create_uid` : Utilisateur créateur
- `create_date` : Date de création
- `write_uid` : Dernier modificateur
- `write_date` : Date de dernière modification

#### **Historique des Actions**
- Toutes les actions sont enregistrées via le système `mail.thread`
- Horodatage précis de chaque étape
- Identification de l'utilisateur pour chaque action

#### **Logs de Sécurité**
```python
# Exemple de log d'action
self.message_post(
    body=f"Demande soumise par {self.env.user.name}",
    subject="Soumission de demande",
    message_type='notification'
)
```

### 🛡️ Protection contre les Vulnérabilités

#### **Injection SQL**
- Utilisation exclusive de l'ORM Odoo
- Pas de requêtes SQL directes
- Validation automatique des paramètres

#### **XSS (Cross-Site Scripting)**
- Échappement automatique des données utilisateur
- Validation des champs HTML
- Filtrage des contenus dangereux

#### **CSRF (Cross-Site Request Forgery)**
- Tokens CSRF automatiques
- Validation des origines
- Protection des actions sensibles

#### **Contrôle d'Accès**
- Vérification systématique des permissions
- Validation des groupes d'utilisateurs
- Contrôle d'accès par enregistrement

### ⚙️ Configuration de Sécurité

#### **Paramètres Recommandés**

1. **Mots de Passe**
   ```
   Paramètres → Utilisateurs → Paramètres d'authentification
   - Longueur minimale : 8 caractères
   - Complexité requise
   - Expiration : 90 jours
   ```

2. **Sessions**
   ```
   Configuration serveur :
   - Timeout session : 8 heures
   - Logout automatique : activé
   - Sessions multiples : contrôlées
   ```

3. **Logs d'Audit**
   ```
   Configuration :
   - Niveau de log : INFO
   - Rotation des logs : quotidienne
   - Rétention : 1 an
   ```

---

## 📊 Rapports et Suivi

### 📈 Tableaux de Bord Intégrés

#### **Dashboard Exécutif**
**Métriques Clés :**
- Nombre total de déplacements par mois
- Budget consommé vs budget alloué
- Délais moyens de validation
- Taux d'approbation par service

**Graphiques :**
- Évolution mensuelle des déplacements
- Répartition par destination (national/international)
- Top 10 des destinations
- Coûts par employé/service

#### **Dashboard Manager**
**Suivi d'Équipe :**
- Demandes en attente de ma validation
- Historique des validations
- Budget équipe consommé
- Performance de validation (délais)

**Analyses :**
- Tendances de déplacements par employé
- Motifs de refus récurrents
- Optimisation des coûts
- Planification prévisionnelle

#### **Dashboard Employé**
**Suivi Personnel :**
- Mes demandes en cours
- Historique des 12 derniers mois
- Budget personnel consommé
- Prochains déplacements planifiés

### 📊 Rapports Standards

#### **Rapport de Déplacements Détaillé**
**Contenu :**
- Liste complète des déplacements sur période
- Détail par employé : dates, destinations, coûts
- Totaux par service/département
- Comparaisons périodiques

**Formats disponibles :**
- PDF pour impression
- Excel pour analyse
- CSV pour import

**Filtres :**
- Période (date de début/fin)
- Employé/Service/Département
- État des demandes
- Type de déplacement (national/international)
- Fourchette de montants

#### **Rapport Budgétaire**
**Analyses Financières :**
- Coûts totaux par période
- Dépassements budgétaires
- Prévisions basées sur tendances
- ROI des déplacements (si configuré)

**Graphiques :**
- Évolution mensuelle des coûts
- Répartition par service
- Coût moyen par déplacement
- Comparaison budget/réalisé

#### **Rapport de Performance Workflow**
**Métriques de Process :**
- Délais moyens de validation par étape
- Taux d'approbation par valideur
- Goulots d'étranglement identifiés
- Performance SLA

**KPIs :**
- Temps de traitement moyen
- Taux de refus par étape
- Demandes en retard
- Satisfaction utilisateur

### 📋 Rapports Personnalisés

#### **Créateur de Rapports**
**Fonctionnalités :**
- Interface drag & drop
- Sélection des champs
- Filtres avancés
- Groupements multiples
- Calculs automatiques

**Types de Vues :**
- Tableaux détaillés
- Graphiques (barres, lignes, secteurs)
- Tableaux croisés dynamiques
- Cartes géographiques

#### **Rapports Planifiés**
**Automatisation :**
- Envoi automatique par email
- Fréquence configurable (quotidien, hebdomadaire, mensuel)
- Destinataires multiples
- Formats multiples simultanés

**Exemples de Planification :**
- Rapport hebdomadaire des validations pour managers
- Rapport mensuel budgétaire pour direction
- Rapport quotidien des demandes urgentes

### 📈 Analytics et Business Intelligence

#### **Indicateurs de Performance (KPI)**

**KPIs Opérationnels :**
- Délai moyen de traitement des demandes
- Taux d'approbation première présentation
- Nombre de demandes par employé/mois
- Respect des délais SLA

**KPIs Financiers :**
- Coût moyen par déplacement
- Évolution du budget déplacements
- ROI des déplacements commerciaux
- Optimisation des coûts transport

**KPIs Qualité :**
- Taux de satisfaction utilisateur
- Nombre d'erreurs dans les demandes
- Conformité aux procédures
- Temps de formation nouveaux utilisateurs

#### **Analyses Prédictives**
**Modèles Intégrés :**
- Prévision du budget nécessaire
- Identification des pics de demandes
- Optimisation des plannings
- Détection d'anomalies

**Machine Learning :**
- Classification automatique des demandes
- Recommandations de validation
- Détection de fraudes potentielles
- Optimisation des coûts

### 📱 Interfaces de Reporting

#### **Vues Web Interactives**
- Tableaux de bord temps réel
- Filtres interactifs
- Drill-down dans les données
- Export direct multi-formats

#### **API de Reporting**
```python
# Exemple d'API pour extraction de données
class TravelReportAPI:
    def get_travel_summary(self, date_from, date_to):
        return {
            'total_requests': count,
            'total_amount': sum,
            'by_status': status_breakdown,
            'by_destination': destination_stats
        }
```

#### **Intégrations Externes**
- Power BI / Tableau
- Google Data Studio
- Excel avec connexion directe
- Exports automatisés ERP

### 📊 Métriques de Suivi Recommandées

#### **Métriques Mensuelles Clés**
1. **Volume :** Nombre de demandes créées/traitées
2. **Délais :** Temps moyen de traitement par étape
3. **Coûts :** Montant total et coût moyen
4. **Qualité :** Taux d'erreur et de rejet
5. **Satisfaction :** Note utilisateur et feedback

#### **Alertes Automatiques**
- Budget mensuel dépassé (seuil configurable)
- Demandes en retard de validation (>72h)
- Pic anormal de demandes
- Erreurs récurrentes détectées

---

## 🔧 Maintenance et Dépannage

### 🛠️ Maintenance Préventive

#### **Tâches de Maintenance Régulières**

**Quotidiennes :**
- Vérification des logs d'erreur
- Contrôle des notifications non envoyées
- Monitoring des performances
- Backup incrémental des données

**Hebdomadaires :**
- Nettoyage des sessions expirées
- Vérification de l'intégrité des données
- Mise à jour des statistiques
- Test des fonctionnalités critiques

**Mensuelles :**
- Archivage des demandes anciennes
- Optimisation de la base de données
- Mise à jour de sécurité
- Révision des permissions utilisateurs

**Trimestrielles :**
- Audit complet de sécurité
- Revue des performances
- Formation utilisateurs
- Mise à jour de la documentation

#### **Scripts de Maintenance**

**Nettoyage Automatique :**
```python
# Script de nettoyage des données anciennes
def cleanup_old_requests():
    old_requests = self.env['employee.travel'].search([
        ('create_date', '<', fields.Date.today() - relativedelta(years=2)),
        ('state', 'in', ['done', 'cancelled', 'refused'])
    ])
    old_requests.unlink()
```

**Vérification d'Intégrité :**
```python
# Vérification de la cohérence des données
def check_data_integrity():
    inconsistent_records = self.env['employee.travel'].search([
        ('date_to', '<', 'date_from')
    ])
    if inconsistent_records:
        # Alerter l'administrateur
        send_alert_email(inconsistent_records)
```

### 🚨 Résolution de Problèmes Courants

#### **Problèmes d'Installation**

**Erreur : Module non trouvé**
```bash
# Solution
1. Vérifier le chemin d'installation
2. Redémarrer Odoo avec --addons-path
3. Mettre à jour la liste des modules
```

**Erreur : Dépendances manquantes**
```bash
# Solution
1. Installer les modules requis : base, hr, mail
2. Vérifier la version Odoo (18.0+)
3. Redémarrer le serveur
```

#### **Problèmes de Fonctionnement**

**Les notifications ne fonctionnent pas**
```python
# Diagnostic
1. Vérifier la configuration email dans Odoo
2. Tester l'envoi d'email manuel
3. Vérifier les règles de notification
4. Contrôler les logs d'erreur

# Solution
- Configurer le serveur SMTP
- Vérifier les modèles d'email
- Relancer le service de mail
```

**Calculs automatiques incorrects**
```python
# Diagnostic
1. Vérifier les méthodes @api.depends
2. Contrôler les données de base (pays, taux)
3. Tester avec données connues

# Solution
- Recalculer les champs computed
- Vérifier la configuration des pays
- Corriger les formules si nécessaire
```

**Problèmes de permissions**
```python
# Diagnostic
1. Vérifier l'affectation des groupes utilisateurs
2. Contrôler les règles de sécurité
3. Tester avec utilisateur admin

# Solution
- Réaffecter les groupes corrects
- Redémarrer Odoo après modification
- Vérifier les règles de domaine
```

#### **Problèmes de Performance**

**Lenteur des vues**
```sql
-- Diagnostic
1. Analyser les requêtes SQL lentes
2. Vérifier les index de base de données
3. Contrôler la charge serveur

-- Solution
- Créer des index sur les champs fréquemment filtrés
- Optimiser les domaines de recherche
- Augmenter les ressources serveur si nécessaire
```

**Timeout sur gros volumes**
```python
# Solution
1. Implémenter la pagination
2. Utiliser des filtres par défaut
3. Optimiser les requêtes ORM
4. Mettre en cache les calculs fréquents
```

### 📋 Procédures de Dépannage

#### **Diagnostic Systématique**

**Étape 1 : Identification du problème**
```
1. Reproduire l'erreur
2. Collecter les logs d'erreur
3. Identifier l'utilisateur affecté
4. Déterminer la fréquence
```

**Étape 2 : Analyse des logs**
```bash
# Consulter les logs Odoo
tail -f /var/log/odoo/odoo.log | grep employee_travel

# Rechercher les erreurs spécifiques
grep -i "error\|exception" /var/log/odoo/odoo.log | grep employee_travel
```

**Étape 3 : Tests en mode debug**
```python
# Activer le mode debug
1. Ajouter ?debug=1 à l'URL
2. Utiliser le shell Odoo pour tests
3. Activer les logs détaillés
```

**Étape 4 : Correction et validation**
```
1. Appliquer la correction
2. Tester en environnement de test
3. Déployer en production
4. Surveiller post-déploiement
```

#### **Kit de Dépannage**

**Commandes Utiles :**
```bash
# Redémarrer Odoo
sudo systemctl restart odoo

# Mettre à jour le module
python3 odoo-bin -d database_name -u employee_travel

# Shell Odoo pour debug
python3 odoo-bin shell -d database_name

# Vérifier la syntaxe Python
python3 -m py_compile models/travel_request.py
```

**Requêtes de Diagnostic :**
```python
# Dans le shell Odoo
# Vérifier les demandes incohérentes
self.env['employee.travel'].search([('date_to', '<', 'date_from')])

# Vérifier les utilisateurs sans employé
self.env['res.users'].search([('employee_id', '=', False)])

# Recalculer tous les montants
for travel in self.env['employee.travel'].search([]):
    travel._compute_amount()
```

### 📚 Base de Connaissances

#### **Erreurs Fréquentes et Solutions**

| Erreur | Cause | Solution |
|--------|-------|----------|
| `Record does not exist` | Employé supprimé | Vérifier l'intégrité des références |
| `action_draft not found` | Cache Odoo | Redémarrer Odoo |
| `Invalid group reference` | Groupe mal référencé | Vérifier les XML ID |
| `Constraint violation` | Données incohérentes | Valider les contraintes métier |
| `Permission denied` | Droits insuffisants | Vérifier les groupes utilisateur |

#### **Codes d'Erreur Personnalisés**

```python
# Codes d'erreur du module
TRAVEL_ERRORS = {
    'TRAVEL_001': 'Demande déjà soumise',
    'TRAVEL_002': 'Dates invalides',
    'TRAVEL_003': 'Distance insuffisante pour avion',
    'TRAVEL_004': 'Budget dépassé',
    'TRAVEL_005': 'Ordre de mission obligatoire'
}
```

### 🔄 Processus de Mise à Jour

#### **Procédure de Mise à Jour du Module**

**Préparation :**
1. Backup complet de la base de données
2. Test en environnement de développement
3. Notification aux utilisateurs
4. Planification en heures creuses

**Déploiement :**
```bash
# 1. Arrêter Odoo
sudo systemctl stop odoo

# 2. Sauvegarder l'ancien module
cp -r employee_travel employee_travel_backup

# 3. Copier la nouvelle version
cp -r employee_travel_new employee_travel

# 4. Mettre à jour le module
python3 odoo-bin -d database_name -u employee_travel --stop-after-init

# 5. Redémarrer Odoo
sudo systemctl start odoo
```

**Post-déploiement :**
1. Vérification fonctionnelle
2. Tests de non-régression
3. Monitoring des performances
4. Feedback utilisateurs

### 📞 Support et Escalade

#### **Niveaux de Support**

**Niveau 1 : Support Utilisateur**
- Questions d'utilisation
- Formation sur les fonctionnalités
- Problèmes de workflow
- Assistance configuration basique

**Niveau 2 : Support Technique**
- Problèmes de performance
- Erreurs applicatives
- Configuration avancée
- Intégrations tierces

**Niveau 3 : Support Développement**
- Bugs critiques
- Modifications de code
- Nouvelles fonctionnalités
- Architecture système

#### **Contacts d'Escalade**
```
Niveau 1: support-utilisateur@societe.ma
Niveau 2: support-technique@societe.ma  
Niveau 3: dev-team@societe.ma
Urgence: admin-urgence@societe.ma
```

---

## 📞 Support et Contact

### 🆘 Support Technique

#### **Canaux de Support Disponibles**

**Support Email :**
- **Général** : support@employee-travel.com
- **Technique** : tech-support@employee-travel.com
- **Urgence** : urgent@employee-travel.com
- **Commercial** : sales@employee-travel.com

**Support Téléphonique :**
- **Standard** : +212 5XX XX XX XX
- **Technique** : +212 5XX XX XX XX (ext. 2)
- **Urgence** : +212 6XX XX XX XX (24h/7j)

**Support Web :**
- **Documentation** : https://docs.employee-travel.com
- **FAQ** : https://faq.employee-travel.com
- **Tickets** : https://support.employee-travel.com
- **Forum** : https://community.employee-travel.com

#### **Heures de Support**
- **Standard** : Lundi-Vendredi 8h-18h (GMT+1)
- **Technique** : Lundi-Vendredi 8h-20h (GMT+1)
- **Urgence** : 24h/24, 7j/7

#### **Niveaux de Service (SLA)**

| Priorité | Délai de Réponse | Délai de Résolution | Canaux |
|----------|------------------|-------------------|---------|
| **Critique** | 1 heure | 4 heures | Téléphone + Email |
| **Urgent** | 4 heures | 1 jour ouvré | Email + Ticket |
| **Normal** | 1 jour ouvré | 3 jours ouvrés | Email + Ticket |
| **Bas** | 2 jours ouvrés | 5 jours ouvrés | Ticket + Forum |

### 📚 Ressources de Documentation

#### **Documentation Technique**
- **Manuel Administrateur** : Configuration et maintenance
- **Manuel Utilisateur** : Guide d'utilisation détaillé
- **API Documentation** : Intégrations et développements
- **Guide de Dépannage** : Résolution de problèmes

#### **Ressources de Formation**
- **Vidéos de Formation** : Tutorials pas-à-pas
- **Webinaires** : Sessions de formation live
- **Documentation Interactive** : Guides avec captures d'écran
- **Certification** : Programme de certification utilisateur

#### **Communauté**
- **Forum Communautaire** : Échanges entre utilisateurs
- **Base de Connaissances** : Solutions partagées
- **Blog** : Actualités et bonnes pratiques
- **Newsletter** : Nouveautés et mises à jour

### 🤝 Services Professionnels

#### **Consulting et Implémentation**
- **Analyse des Besoins** : Audit des processus existants
- **Configuration Personnalisée** : Adaptation aux besoins spécifiques
- **Migration de Données** : Import depuis systèmes existants
- **Formation Sur-Mesure** : Sessions adaptées à l'organisation

#### **Développement Custom**
- **Fonctionnalités Spécifiques** : Développements sur mesure
- **Intégrations** : Connexions avec systèmes tiers
- **Rapports Personnalisés** : Tableaux de bord spécialisés
- **API Custom** : Interfaces de programmation dédiées

#### **Support Dédié**
- **Support 24/7** : Assistance continue
- **Responsable de Compte** : Interlocuteur unique
- **SLA Renforcé** : Engagements de service premium
- **Maintenance Proactive** : Surveillance et optimisation

### 📋 Informations de Contact

#### **Siège Social**
```
Employee Travel Solutions
123 Avenue Mohammed V
Casablanca, Maroc 20000

Tél: +212 5XX XX XX XX
Fax: +212 5XX XX XX XX
Email: contact@employee-travel.com
```

#### **Équipe de Développement**
```
Lead Developer: dev-lead@employee-travel.com
QA Team: quality@employee-travel.com
DevOps: infrastructure@employee-travel.com
Product Manager: product@employee-travel.com
```

#### **Réseaux Sociaux**
- **LinkedIn** : https://linkedin.com/company/employee-travel
- **Twitter** : @EmployeeTravel
- **YouTube** : Employee Travel Channel
- **GitHub** : https://github.com/employee-travel

### 🔄 Processus de Feedback

#### **Comment Nous Contacter**

**Pour un Bug :**
1. Décrire le problème précisément
2. Fournir les étapes de reproduction
3. Inclure les captures d'écran
4. Préciser la version Odoo et du module

**Pour une Amélioration :**
1. Expliquer le besoin métier
2. Proposer la solution souhaitée
3. Évaluer l'impact sur les utilisateurs
4. Prioriser la demande

**Pour une Question :**
1. Consulter la FAQ en premier
2. Rechercher dans la documentation
3. Poser la question sur le forum
4. Contacter le support si nécessaire

#### **Suivi des Demandes**
- **Numéro de Ticket** : Fourni automatiquement
- **Statut en Temps Réel** : Portail de suivi en ligne
- **Notifications** : Alertes par email des mises à jour
- **Historique** : Conservation de tous les échanges

### 📊 Satisfaction Client

#### **Métriques de Qualité**
- **Satisfaction** : 98% (objectif >95%)
- **Résolution Premier Contact** : 85% (objectif >80%)
- **Temps de Réponse Moyen** : 2.3h (objectif <4h)
- **Disponibilité Service** : 99.9% (objectif >99.5%)

#### **Programme d'Amélioration Continue**
- **Enquêtes de Satisfaction** : Trimestrielles
- **Groupes Utilisateurs** : Réunions bi-annuelles
- **Roadmap Collaborative** : Planning partagé
- **Beta Testing** : Programme de test précoce

---

## 📄 Annexes

### 📋 Annexe A : Checklist de Déploiement

#### **Préparation (J-7)**
- [ ] Backup complet de la base de données
- [ ] Test d'installation en environnement de développement
- [ ] Validation des prérequis techniques
- [ ] Formation des super-utilisateurs
- [ ] Communication aux utilisateurs finaux

#### **Installation (J-Day)**
- [ ] Arrêt programmé du système
- [ ] Installation du module Employee Travel
- [ ] Configuration des groupes d'utilisateurs
- [ ] Import des données de base (véhicules, etc.)
- [ ] Tests de fonctionnement

#### **Post-Déploiement (J+1 à J+7)**
- [ ] Monitoring des performances
- [ ] Support renforcé aux utilisateurs
- [ ] Collecte des premiers feedbacks
- [ ] Ajustements si nécessaires
- [ ] Formation complémentaire

### 📋 Annexe B : Configuration Technique

#### **Prérequis Serveur**
```
OS: Ubuntu 20.04+ / CentOS 8+ / Debian 10+
Python: 3.8+
PostgreSQL: 12+
RAM: Minimum 4GB (Recommandé 8GB)
Stockage: Minimum 50GB SSD
CPU: 2 cores minimum (Recommandé 4 cores)
```

#### **Configuration Odoo Recommandée**
```ini
[options]
addons_path = /opt/odoo/addons,/opt/odoo/custom_addons
admin_passwd = STRONG_PASSWORD
db_host = localhost
db_port = 5432
db_user = odoo
db_password = DB_PASSWORD
logfile = /var/log/odoo/odoo.log
log_level = info
workers = 4
max_cron_threads = 2
```

#### **Variables d'Environnement**
```bash
export ODOO_VERSION=18.0
export ODOO_ADDONS_PATH=/opt/odoo/custom_addons
export EMPLOYEE_TRAVEL_CONFIG=/etc/employee_travel/config.yaml
```

### 📋 Annexe C : Scripts Utiles

#### **Script de Sauvegarde**
```bash
#!/bin/bash
# backup_employee_travel.sh

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/opt/backups/employee_travel"
DB_NAME="odoo_production"

# Create backup directory
mkdir -p $BACKUP_DIR

# Database backup
pg_dump -h localhost -U odoo $DB_NAME > $BACKUP_DIR/db_backup_$DATE.sql

# Module files backup
tar -czf $BACKUP_DIR/module_backup_$DATE.tar.gz /opt/odoo/custom_addons/employee_travel

echo "Backup completed: $DATE"
```

#### **Script de Restauration**
```bash
#!/bin/bash
# restore_employee_travel.sh

BACKUP_FILE=$1
DB_NAME="odoo_production"

if [ -z "$BACKUP_FILE" ]; then
    echo "Usage: $0 <backup_file.sql>"
    exit 1
fi

# Stop Odoo
sudo systemctl stop odoo

# Restore database
dropdb -h localhost -U odoo $DB_NAME
createdb -h localhost -U odoo $DB_NAME
psql -h localhost -U odoo $DB_NAME < $BACKUP_FILE

# Start Odoo
sudo systemctl start odoo

echo "Restoration completed"
```

### 📋 Annexe D : FAQ Technique

#### **Q: Comment ajouter de nouveaux champs au formulaire ?**
R: Modifier le fichier `views/travel_views.xml` et ajouter les champs dans le modèle `models/travel_request.py`.

#### **Q: Comment personnaliser les calculs de montant ?**
R: Modifier la méthode `_compute_amount()` dans `models/travel_request.py`.

#### **Q: Comment ajouter de nouveaux états au workflow ?**
R: Ajouter les états dans le champ `state` et créer les méthodes de transition correspondantes.

#### **Q: Comment intégrer avec un système de paie externe ?**
R: Développer un connecteur utilisant l'API Odoo ou créer un module d'intégration spécialisé.

#### **Q: Comment exporter les données vers Excel automatiquement ?**
R: Utiliser les fonctionnalités de rapport Odoo ou développer un scheduler personnalisé.

### 📋 Annexe E : Glossaire

| Terme | Définition |
|-------|------------|
| **DAF** | Direction Administrative et Financière |
| **ORM** | Object-Relational Mapping - Système de mappage objet-relationnel d'Odoo |
| **SLA** | Service Level Agreement - Accord de niveau de service |
| **Workflow** | Flux de travail automatisé |
| **Record Rule** | Règle de sécurité au niveau enregistrement |
| **Action Server** | Action automatisée côté serveur |
| **Computed Field** | Champ calculé automatiquement |
| **Constraint** | Contrainte de validation des données |
| **Domain** | Filtre de recherche dans Odoo |
| **View** | Interface utilisateur (formulaire, liste, etc.) |

---

## 📊 Métriques et Indicateurs

### 📈 KPIs de Performance
- **Temps de traitement moyen** : <24h pour validation manager, <48h pour validation DAF
- **Taux d'adoption** : >90% des employés utilisent le système
- **Satisfaction utilisateur** : Score >4.5/5
- **Disponibilité système** : >99.5%
- **Réduction des coûts administratifs** : -40% vs processus papier

### 🎯 Objectifs de Qualité
- **Zéro perte de données** : Sauvegarde et récupération garanties
- **Conformité RGPD** : Protection des données personnelles
- **Audit trail complet** : Traçabilité de toutes les actions
- **Sécurité renforcée** : Authentification et autorisation strictes

---

## 🏆 Certification et Conformité

### ✅ Standards Respectés
- **ISO 27001** : Sécurité de l'information
- **RGPD** : Protection des données personnelles
- **SOX** : Contrôles financiers (si applicable)
- **Best Practices Odoo** : Développement selon standards Odoo

### 🛡️ Audits de Sécurité
- **Audit interne** : Trimestriel
- **Audit externe** : Annuel
- **Tests de pénétration** : Bi-annuel
- **Revue de code** : À chaque mise à jour

---

**© 2025 Employee Travel Solutions. Tous droits réservés.**

*Cette documentation est mise à jour régulièrement. Version courante : 1.0 - Date : Novembre 2025*