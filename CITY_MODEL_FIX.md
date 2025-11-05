# 🔧 Guide de Résolution - Problème model_travel_city

## ❌ **Erreur rencontrée**
```
No matching record found for external id 'model_travel_city' in field 'Model'
```

## 🔍 **Cause du problème**
Odoo essaie de charger les droits d'accès avant que le modèle soit créé.

## ✅ **Solutions appliquées**

### 📋 **Solution 1 : Ordre de chargement modifié**
```python
'data': [
    'data/ir_sequence.xml',
    'security/groups.xml',
    'security/ir.model.access.csv',      # Droits de base (sans city)
    'security/ir_rule.xml',
    'views/travel_views.xml',            # Crée le modèle travel
    'views/city_views.xml',              # Crée le modèle city
    'security/city_access.csv',          # Droits pour city (après création)
    'data/city_data.xml',                # Données de ville
],
```

### 📋 **Solution 2 : Fichiers séparés**
- **ir.model.access.csv** : Droits pour les modèles de base
- **city_access.csv** : Droits pour le modèle city (chargé après)

## 🚀 **Instructions de déploiement**

### **Étape 1 : Désinstaller l'ancien module (si nécessaire)**
```
Apps → Employee Travel → Désinstaller
```

### **Étape 2 : Redémarrer Odoo**
```bash
sudo systemctl restart odoo
```

### **Étape 3 : Installer le nouveau module**
```
Apps → Mettre à jour liste → Rechercher "Employee Travel" → Installer
```

### **Étape 4 : Vérifier le fonctionnement**
1. Menu "Déplacements" doit apparaître
2. Sous-menu "Villes" doit être visible
3. Création de demande avec sélecteur de ville

## 🎯 **Fonctionnalités du nouveau modèle Ville**

### **Champs disponibles :**
- ✅ Nom de la ville
- ✅ Code postal
- ✅ Pays (avec filtre automatique)
- ✅ Actif/Inactif

### **Intégration avec déplacements :**
- ✅ Sélecteur de ville filtré par pays
- ✅ Champ texte libre en fallback
- ✅ Recherche intelligente
- ✅ Affichage "Ville, Pays (Code postal)"

### **Données pré-installées :**
- 🇲🇦 **Maroc** : Casablanca, Rabat, Marrakech, Fès
- 🇫🇷 **France** : Paris, Lyon, Marseille
- 🇪🇸 **Espagne** : Madrid, Barcelona
- 🇬🇧 **UK** : London
- 🇦🇪 **UAE** : Dubai

---

**🎉 Le module est maintenant prêt avec le système de villes intégré !**