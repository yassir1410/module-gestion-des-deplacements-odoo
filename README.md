# 🚗 Employee Travel - Module Odoo 18

## 📋 Description
Module complet de gestion des demandes de déplacement professionnel pour Odoo 18 avec workflow de validation à deux niveaux (Manager → DAF).

## ✨ Fonctionnalités Principales
- ✅ **Demandes de déplacement** avec workflow automatisé
- ✅ **Calcul automatique** des montants (700 DH national, 1500 DH international)
- ✅ **Validation hiérarchique** (Manager → DAF)
- ✅ **Règles métier** configurables (avion obligatoire >500km, etc.)
- ✅ **Gestion des véhicules** de service
- ✅ **Notifications automatiques** 
- ✅ **Sécurité avancée** par groupes d'utilisateurs
- ✅ **Interface responsive** et intuitive

## 🚀 Installation Rapide

### Prérequis
- Odoo 18.0+
- Modules : `base`, `hr`, `mail`

### Installation
1. Copier le module dans `/addons/` ou `/custom_addons/`
2. Redémarrer Odoo
3. Aller dans **Apps** → Rechercher "Employee Travel"
4. Cliquer sur **Installer**

## ⚙️ Configuration

### Groupes d'Utilisateurs
Après installation, configurer les utilisateurs :

**Paramètres → Utilisateurs → [Utilisateur] → Droits d'accès**

- **👨‍💼 Travel Manager** : Managers/Superviseurs (validation étape 1)
- **🏛️ Travel DAF** : Direction Administrative (validation finale)
- **👤 Employé** : Aucun groupe spécial (création de demandes uniquement)

## 🔄 Workflow

```
👤 Employé → 📝 Créer → ✅ Soumettre → 👨‍💼 Manager → ✅ Valider → 🏛️ DAF → ✅ Approuver → ✅ Terminé
```

## 💰 Règles de Calcul

### Montants Automatiques
- **National** : 700 DH/jour
- **International** : 1500 DH/jour

### Règles de Transport
- **< 500 km** : Transport terrestre
- **≥ 500 km** : Avion obligatoire
- **≥ 6000 km** : Classe business automatique

## 📚 Documentation

- **[📖 Documentation Complète](DOCUMENTATION_COMPLETE.md)** - Guide technique détaillé
- **[👤 Guide Utilisateur](GUIDE_UTILISATEUR.md)** - Mode d'emploi pour les utilisateurs

## 🎯 Utilisation

### Pour les Employés
```
Menu Déplacements → Mes Demandes → [+ Créer]
```

### Pour les Managers  
```
Menu Déplacements → À Valider
```

### Pour la DAF
```
Menu Déplacements → Traitement DAF
```

## 🛡️ Sécurité

- **Accès par rôle** : Chaque utilisateur ne voit que ce qui le concerne
- **Validation hiérarchique** : Workflow à 2 niveaux obligatoire
- **Traçabilité complète** : Historique de toutes les actions
- **Contrôles d'intégrité** : Validation des données métier

## 📊 Structure du Module

```
employee_travel/
├── __manifest__.py          # Configuration du module
├── __init__.py             # Initialisation Python
├── models/                 # Modèles de données
│   ├── travel_request.py   # Demandes de déplacement
│   └── vehicle.py          # Véhicules de service
├── views/                  # Interfaces utilisateur
│   └── travel_views.xml    # Vues et menus
├── security/               # Sécurité et permissions
│   ├── groups.xml          # Groupes d'utilisateurs
│   ├── ir.model.access.csv # Droits d'accès
│   └── ir_rule.xml         # Règles de sécurité
└── data/                   # Données de base
    └── sequence.xml        # Numérotation automatique
```

## 🏆 Version

- **Version** : 18.0.1.0.0
- **Compatibilité** : Odoo 18.0+
- **Licence** : LGPL-3
- **Auteur** : Yassir
- **Date** : Novembre 2025

## 📞 Support

Pour toute question ou support :
- 📧 Consulter la documentation complète
- 🔧 Vérifier les logs Odoo en cas d'erreur
- 🔄 Redémarrer Odoo après modifications

---

**🎯 Module prêt pour la production - Installation et utilisation immédiate !** 🚀
# module-gestion-des-deplacements-odoo
