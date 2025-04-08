# Cahier des charges - Application Rafistoler

## 1. Présentation générale
**Nom du projet :** Rafistoler

**Objectif :** Développer une application web/mobile de mise en relation entre clients et couturiers ambulants appelés "Toclos". L’application s’inspire fortement du modèle de Yango (sans les fonctionnalités de livraison, restauration ou vente), en se concentrant sur la géolocalisation, la réservation, le paiement et la gestion des prestations de couture à domicile ou en déplacement.

**Cible :** Grand public ivoirien (particuliers) recherchant un service de couture rapide et personnalisé, ainsi que des artisans couturiers souhaitant étendre leur clientèle.

---

## 2. Acteurs du système

- **Client :**
  - Cherche un toclo autour de lui
  - Réserve une prestation
  - Suit son toclo en temps réel
  - Effectue le paiement
  - Laisse un avis et une note

- **Toclo (couturier ambulant) :**
  - Reçoit des demandes de prestation
  - Accepte ou refuse une mission
  - Se géolocalise
  - Met à jour son planning
  - Suit ses revenus
  - Souscrit à un abonnement mensuel ou annuel

- **Administrateur système :**
  - Gère les comptes utilisateurs (clients et toclos)
  - Valide les inscriptions toclos
  - Supervise les transactions
  - Gère les abonnements
  - Modère les avis

---

## 3. Fonctionnalités principales

### Pour le client :
- Création de compte / Connexion (email, téléphone)
- Géolocalisation automatique
- Consultation des toclos disponibles sur une carte interactive
- Fiche détaillée des toclos (photo, note, services, expérience)
- Réservation d’un service (choix du service, adresse, date, heure)
- Paiement en ligne sécurisé (MoMo, carte bancaire, etc.)
- Suivi en temps réel du toclo
- Historique des prestations
- Notation et avis post-prestation

### Pour le toclo :
- Inscription et validation de profil
- Géolocalisation et activation du statut “disponible”
- Consultation des demandes clients
- Acceptation ou refus d’une mission
- Gestion de son planning
- Historique des missions réalisées
- Suivi des paiements et revenus
- Accès à un tableau de bord personnalisé
- Paiement d’un abonnement mensuel ou annuel pour apparaître sur la plateforme (intégration d’un système de gestion d’abonnements)

### Pour l’administrateur :
- Tableau de bord global
- Gestion des utilisateurs
- Gestion des abonnements
- Statistiques d’utilisation
- Supervision des transactions
- Modération des contenus (avis, profils)

---

## 4. Architecture technique

- **Frontend :** HTML, CSS, JavaScript (framework possible : React / Vue.js)
- **Backend :** Node.js / Express ou Django / Laravel (selon préférence)
- **Base de données :** PostgreSQL ou MongoDB
- **API de géolocalisation :** Google Maps API / OpenStreetMap
- **Paiement :** Intégration MTN MoMo, Orange Money, Wave, Stripe, etc.
- **Abonnements :** Stripe, Flutterwave ou solution de gestion récurrente personnalisée
- **Authentification :** JWT + OTP par SMS (API SMS locale)
- **Stockage cloud :** Firebase Storage / Cloudinary (pour images)

---

## 5. Design UX/UI (inspiration Yango)

- Navigation fluide et intuitive
- Interface mobile-first
- Carte interactive sur la page d’accueil
- Icônes et visuels illustrant chaque type de service
- Thème aux couleurs chaudes et locales (jaune, orange, noir)
- Système de notifications push (confirmation, arrivée du toclo, rappel...)

---

## 6. Évolutions futures possibles

- Intégration d’une IA pour recommander les toclos selon le style préféré du client
- Application mobile native (Flutter / React Native)
- Système de fidélité (points, réductions)
- Mode hors ligne pour les toclos (prise de rdv sans data)
- Multilingue (français, dioula, baoulé, anglais...)
- Portefeuille virtuel interne à l’app

---

## 7. Contraintes

- Accessibilité sur mobile avant tout (public africain souvent mobile-first)
- Légèreté de l’appli (connexion souvent faible)
- Interface simple pour utilisateurs non technophiles
- Sécurité des données personnelles et financières
- Paiement fiable et traçable pour abonnements et prestations ponctuelles

---

## 8. Planning prévisionnel

| Étape | Durée | Responsable |
|-------|-------|-------------|
| Conception UI/UX | 2 semaines | Designer |
| Développement frontend | 3 semaines | Dev Front |
| Développement backend | 4 semaines | Dev Back |
| Intégration API + paiement + abonnement | 3 semaines | Fullstack |
| Tests / Validation | 2 semaines | QA |
| Lancement bêta | 1 semaine | Chef projet |
| Mise en production | 1 semaine | Admin infra |

---

## 9. Budget prévisionnel (indicatif)

| Élément | Coût estimé |
|---------|-------------|
| Hébergement & Nom de domaine | 100$ / an |
| APIs Google / SMS | 50$ / mois |
| Développement initial | 2 500$ |
| Communication & Marketing | 500$ |
| Maintenance mensuelle | 100$ / mois |

---

## 10. Conclusion

Rafistoler ambitionne de professionnaliser les services de couture ambulants en Côte d’Ivoire en leur apportant la puissance du numérique. Grâce à un système de géolocalisation efficace, une interface fluide et un parcours utilisateur optimisé, l’appli veut devenir la référence ivoirienne de la couture mobile, tout comme Yango l’est pour le transport.

La solution s’appuie également sur un modèle économique durable via un système d’abonnement pour les toclos, et un paiement intégré pour les clients.

Le projet peut être décliné dans d'autres pays africains à terme.

**Let's rafistol everything. 👕🚀**

