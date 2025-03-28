import streamlit as st

st.markdown("""
    <style>
    /* Masque les informations de déploiement */
    .stDeploymentInfo {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ====================
# ARBRE DÉCISIONNEL COMPLET
# ====================
ARBRE = {
    ######### BRANCHE MAIRE
    # Scénario : Maire d'Écoville
    "maire": {
    "début": {
        "texte": "Vous êtes élu maire d'Écoville (100 000 hab.) avec 52% des voix. La pollution atmosphérique dépasse les seuils critiques. Votre mandat : 6 ans.",
        "choix": {
            "Plan vélo ambitieux (20M€)": "plan_velo",
            "Nouvelle autoroute (150M€)": "autoroute",
            "Rénovation thermique des écoles": "renovation_ecoles",
            "Ville 100% énergies renouvelables": "energies_vertes",
            "Péage urbain écologique": "peage_urbain"
        }
    },

    # BRANCHE VÉLO (complète avec fins)
    "plan_velo": {
        "texte": "Vous annoncez 200km de pistes cyclables. Les écologistes sont ravis mais les commerçants manifestent.",
        "conséquences": {"Environnement": +20, "Budget": -30, "Social": +15, "Popularité": +10},
        "choix": {
            "Créer un vélo-partage électrique": "velo_partage",
            "Supprimer des places de parking (protestations garanties)": "fin_velo_conflit",
            "Organiser un référendum (risque de blocage)": "fin_referendum_bloque"
        }
    },
    "fin_velo_conflit": {
        "texte": "La suppression brutale des places parking crée un tollé. Les commerçants obtiennent gain de cause en justice. Votre projet est annulé.",
        "conséquences": {"Environnement": -10, "Budget": -15, "Social": -30, "Popularité": -25},
        "fin": "Échec politique cuisant"
    },
    "fin_referendum_bloque": {
        "texte": "Le référendum divise la ville (52% contre). Vous passez pour un maire indécis. Aucun projet d'envergure ne sera lancé ce mandat.",
        "conséquences": {"Environnement": 0, "Budget": -5, "Social": -15, "Popularité": -20},
        "fin": "Immobilisme politique"
    },
    "velo_partage": {
        "texte": "500 vélos électriques en libre-service sont déployés. 10 000 abonnés en 3 mois !",
        "conséquences": {"Environnement": +25, "Budget": -15, "Social": +20, "Popularité": +15},
        "choix": {
            "Étendre aux quartiers populaires": "extension_quartiers",
            "Sponsoring par des entreprises": "fin_sponsoring_reussi",
            "Intégrer des vélos-cargos (coût +30%)": "fin_velo_cargo"
        }
    },
    "fin_sponsoring_reussi": {
        "texte": "3 grandes entreprises financent le système à 80%. Le service devient très rentable mais perd son âme citoyenne.",
        "conséquences": {"Environnement": +15, "Budget": +40, "Social": -10, "Popularité": +5},
        "fin": "Succès économique, échec social"
    },
    "fin_velo_cargo": {
        "texte": "Les 50 vélos-cargos sont un succès auprès des familles. Votre ville devient une référence nationale !",
        "conséquences": {"Environnement": +40, "Budget": -20, "Social": +35, "Popularité": +30},
        "fin": "Visionnaire des mobilités douces"
    },
    "extension_quartiers": {
        "texte": "L'extension crée 50 emplois locaux mais révèle des tensions sociales.",
        "conséquences": {"Environnement": +30, "Budget": -10, "Social": -5, "Popularité": +20},
        "fin": "Réussite écologique mais fractures sociales"
    },

    # BRANCHE AUTOROUTE (complète avec fins)
    "autoroute": {
        "texte": "Le projet A118 divise la ville. 2 000 emplois promis mais destruction de 50ha de terres agricoles.",
        "conséquences": {"Environnement": -40, "Budget": -80, "Social": -30, "Popularité": -20},
        "choix": {
            "Forcer le passage en justice (risque élevé)": "fin_autoroute_forcee",
            "Négocier avec les opposants": "negocier_autoroute",
            "Organiser un débat public (aléatoire)": "fin_debat_chaotique"
        }
    },
    "fin_autoroute_forcee": {
        "texte": "Votre forcing juridique crée un scandale national. L'État reprend le dossier et vous marginalise.",
        "conséquences": {"Environnement": -20, "Budget": -50, "Social": -50, "Popularité": -40},
        "fin": "Mise à l'écart politique"
    },
    "fin_debat_chaotique": {
        "texte": "Le débat public tourne au chaos. 5 ans de procédures s'ensuivent. Le projet est enterré.",
        "conséquences": {"Environnement": 0, "Budget": -30, "Social": -20, "Popularité": -15},
        "fin": "Gaspillage d'énergie publique"
    },
    "negocier_autoroute": {
        "texte": "Vous proposez un tunnel sous les terres agricoles. Coût supplémentaire : 70M€.",
        "conséquences": {"Environnement": -15, "Budget": -150, "Social": +5, "Popularité": -5},
        "choix": {
            "Trouver un financement européen": "financement_eu",
            "Annuler le tunnel (perte de crédibilité)": "fin_abandon_tunnel",
            "Lancer un emprunt municipal (risqué)": "fin_emprunt_couteux"
        }
    },
    "fin_abandon_tunnel": {
        "texte": "Votre revirement vous discrédite totalement. L'opposition demande votre démission.",
        "conséquences": {"Environnement": -25, "Budget": -60, "Social": -30, "Popularité": -35},
        "fin": "Crise politique irrémédiable"
    },
    "fin_emprunt_couteux": {
        "texte": "L'emprunt alourdit la dette municipale pour 20 ans. La ville perd son AAA financier.",
        "conséquences": {"Environnement": -10, "Budget": -200, "Social": -10, "Popularité": -25},
        "fin": "Désastre financier"
    },
    "financement_eu": {
        "texte": "L'UE finance 40% du tunnel. L'autoroute est construite avec 2 ans de retard.",
        "conséquences": {"Environnement": -10, "Budget": -90, "Social": +15, "Popularité": +10},
        "fin": "Projet controversé mais accepté"
    },

    # BRANCHE ÉCOLES (complète avec fins)
    "renovation_ecoles": {
        "texte": "Vous engagez la rénovation de 15 écoles (isolation, panneaux solaires). Budget : 25M€.",
        "conséquences": {"Environnement": +30, "Budget": -25, "Social": +25, "Popularité": +20},
        "choix": {
            "Prioriser les écoles défavorisées": "ecoles_defavorisees",
            "Cibler d'abord les plus énergivores": "fin_ecoles_energie",
            "Former les enseignants (coût +5M€)": "fin_formation_enseignants"
        }
    },
    "fin_ecoles_energie": {
        "texte": "Les économies d'énergie dépassent les attentes (+35%). Votre approche technicienne est saluée.",
        "conséquences": {"Environnement": +40, "Budget": +10, "Social": +15, "Popularité": +25},
        "fin": "Expert en efficacité énergétique"
    },
    "fin_formation_enseignants": {
        "texte": "Les 500 enseignants formés deviennent des ambassadeurs écologiques. Un changement générationnel s'amorce !",
        "conséquences": {"Environnement": +25, "Budget": -30, "Social": +40, "Popularité": +35},
        "fin": "Vision éducative transformative"
    },
    "ecoles_defavorisees": {
        "texte": "Les travaux dans les quartiers pauvres réduisent les inégalités. Votre popularité explose !",
        "conséquences": {"Environnement": +20, "Budget": -10, "Social": +40, "Popularité": +30},
        "fin": "Double victoire sociale et écologique"
    },

    # BRANCHE ÉNERGIES VERTES (complète avec fins)
    "energies_vertes": {
        "texte": "Objectif : 100% d'énergies renouvelables d'ici 2030. Par où commencer ? Budget initial : 50M€",
        "conséquences": {"Environnement": +15, "Budget": -20, "Social": +10, "Popularité": +15},
        "choix": {
            "Parc éolien municipal": "eolien",
            "Centrale biomasse": "fin_biomasse_controversee",
            "Géothermie profonde": "fin_geothermie_risquee"
        }
    },
    "fin_biomasse_controversee": {
        "texte": "La centrale brûle des déchets verts locaux. Des riverains dénoncent des nuisances olfactives. Procès en vue.",
        "conséquences": {"Environnement": +10, "Budget": -25, "Social": -20, "Popularité": -15},
        "fin": "Goodwill écologique perdu"
    },
    "fin_geothermie_risquee": {
        "texte": "Le forage provoque un mini-tremblement de terre (2.4 sur Richter). Panique générale et abandon du projet.",
        "conséquences": {"Environnement": -5, "Budget": -40, "Social": -30, "Popularité": -35},
        "fin": "Fiasco technologique"
    },
    "eolien": {
        "texte": "5 éoliennes prévues mais des riverains protestent contre les nuisances.",
        "conséquences": {"Environnement": +25, "Budget": -40, "Social": -15, "Popularité": -10},
        "choix": {
            "Organiser une concertation": "concertation_eolien",
            "Imposer le projet (risque électoral)": "fin_eolien_impose",
            "Réduire le nombre d'éoliennes": "fin_eolien_reduit"
        }
    },
    "fin_eolien_impose": {
        "texte": "Votre autoritarisme vous aliène l'électorat écologiste. Les éoliennes tournent... sous surveillance policière.",
        "conséquences": {"Environnement": +15, "Budget": -35, "Social": -25, "Popularité": -20},
        "fin": "Victoire à la Pyrrhus"
    },
    "fin_eolien_reduit": {
        "texte": "3 éoliennes au lieu de 5. Le projet perd 60% de son potentiel mais les tensions s'apaisent.",
        "conséquences": {"Environnement": +10, "Budget": -25, "Social": +5, "Popularité": +5},
        "fin": "Compromis décevant"
    },
    "concertation_eolien": {
        "texte": "Vous proposez une participation financière aux riverains. Le projet est accepté à 68%.",
        "conséquences": {"Environnement": +20, "Budget": -35, "Social": +20, "Popularité": +25},
        "fin": "Démocratie participative réussie"
    },

    # BRANCHE PÉAGE URBAIN (complète avec fins)
    "peage_urbain": {
        "texte": "Vous instaurez un péage pour les véhicules polluants en centre-ville. Tollé général.",
        "conséquences": {"Environnement": +40, "Budget": +15, "Social": -35, "Popularité": -25},
        "choix": {
            "Exempter les habitants (perte de revenus)": "fin_exemption_locaux",
            "Investir les recettes dans les transports": "reinvestissement",
            "Abandonner face aux pressions": "fin_abandon_peage"
        }
    },
    "fin_exemption_locaux": {
        "texte": "Seuls 30% des automobilistes paient. Les recettes sont insuffisantes pour financer les alternatives.",
        "conséquences": {"Environnement": +15, "Budget": -10, "Social": -15, "Popularité": -10},
        "fin": "Mesure symbolique inefficace"
    },
    "fin_abandon_peage": {
        "texte": "Votre recul est perçu comme une faiblesse. Vous perdez toute crédibilité environnementale.",
        "conséquences": {"Environnement": -20, "Budget": -5, "Social": -25, "Popularité": -30},
        "fin": "Occasion historique ratée"
    },
    "reinvestissement": {
        "texte": "Les 8M€ annuels financent des bus gratuits. La pollution baisse de 25% en 2 ans.",
        "conséquences": {"Environnement": +50, "Budget": +5, "Social": +30, "Popularité": +40},
        "fin": "Courage politique récompensé"
    }
},

    ######### BRANCHE CITOYEN
    # Scénario : Citoyen d'Écoville
    "citoyen": {
    "début": {
        "texte": "Vous êtes un habitant d'Écoville, parent de 2 enfants. Votre objectif : réduire votre empreinte carbone de 50% en 1 an.",
        "choix": {
            "Révolutionner mes transports": "transport",
            "Transformer mon alimentation": "alimentation",
            "Éco-rénover ma maison": "logement",
            "M'engager dans la communauté": "engagement",
            "Changer ma consommation": "consommation"
        }
    },

    # BRANCHE TRANSPORT (complète avec fins)
    "transport": {
        "texte": "Votre voiture (12L/100km) représente 45% de votre empreinte. Quelle alternative choisir ?",
        "conséquences": {"Budget": +5, "CO2": -15, "Temps": -10, "Bien-être": +10},
        "choix": {
            "Acheter un vélo électrique (2 000€)": "velo_elec",
            "Passer aux transports en commun": "fin_transports_galere",
            "Essayer le covoiturage dynamique": "fin_covoiturage_decept",
            "Télétravailler 4j/semaine": "fin_teletravail_isolement"
        }
    },
    "fin_transports_galere": {
        "texte": "Les bus sont souvent en retard et bondés. Vous craquez et reprenez la voiture après 3 mois.",
        "conséquences": {"Budget": -5, "CO2": +5, "Temps": -20, "Bien-être": -15},
        "fin": "Retour à la case départ"
    },
    "fin_covoiturage_decept": {
        "texte": "Les trajets ne correspondent jamais à vos horaires. Vous abandonnez par manque de fiabilité.",
        "conséquences": {"Budget": 0, "CO2": -5, "Temps": -25, "Bien-être": -10},
        "fin": "Bonne volonté non récompensée"
    },
    "fin_teletravail_isolement": {
        "texte": "Votre employeur accepte mais vous souffrez d'isolement. Votre productivité baisse de 30%.",
        "conséquences": {"Budget": +10, "CO2": -20, "Temps": +5, "Bien-être": -25},
        "fin": "Gain écologique, perte sociale"
    },
    "velo_elec": {
        "texte": "Vous parcourez 50km/semaine en vélo. Vos enfants adorent mais les jours de pluie sont difficiles.",
        "conséquences": {"Budget": -15, "CO2": -30, "Temps": +5, "Bien-être": +25},
        "choix": {
            "Acheter un vélo cargo familial (5 000€)": "fin_velo_cargo_reussi",
            "S'abonner à un service d'autopartage": "fin_autopartage_cher",
            "Installer un abri vélo sécurisé": "fin_abri_volé"
        }
    },
    "fin_velo_cargo_reussi": {
        "texte": "Le vélo cargo remplace votre 2ème voiture. Vous devenez une célébrité locale !",
        "conséquences": {"Budget": -25, "CO2": -50, "Temps": 0, "Bien-être": +40},
        "fin": "Famille zéro-carbone"
    },
    "fin_autopartage_cher": {
        "texte": "Les tarifs explosent après 6 mois. Vous devez renoncer à ce service trop coûteux.",
        "conséquences": {"Budget": -30, "CO2": -15, "Temps": -10, "Bien-être": -5},
        "fin": "Solution temporaire"
    },
    "fin_abri_volé": {
        "texte": "Votre vélo est volé après 2 mois malgré l'abri. Vous retournez à la voiture, découragé.",
        "conséquences": {"Budget": -35, "CO2": +20, "Temps": -15, "Bien-être": -30},
        "fin": "Expérience amère"
    },

    # BRANCHE ALIMENTATION (complète avec fins)
    "alimentation": {
        "texte": "Votre famille mange de la viande 10x/semaine. Le frigo a 15 ans. Par quoi commencer ?",
        "conséquences": {"Budget": 0, "CO2": -5, "Santé": +10, "Plaisir": -5},
        "choix": {
            "Devenir flexitarien (viande 2x/semaine)": "flexitarien",
            "Acheter un frigo A+++ (1 200€)": "fin_frigo_efficace",
            "Rejoindre une AMAP locale": "fin_amap_contraignante",
            "Cultiver un potager": "fin_potager_echec"
        }
    },
    "fin_frigo_efficace": {
        "texte": "Votre nouvelle appliance réduit la facture de 25%. Mais vos habitudes alimentaires ne changent pas.",
        "conséquences": {"Budget": -10, "CO2": -15, "Santé": +5, "Plaisir": 0},
        "fin": "Progrès technique seul"
    },
    "fin_amap_contraignante": {
        "texte": "Les paniers imposent trop de légumes inconnus. Toute la famille râle. Vous abandonnez après 2 mois.",
        "conséquences": {"Budget": -5, "CO2": -10, "Santé": +5, "Plaisir": -20},
        "fin": "Bonne intention mal adaptée"
    },
    "fin_potager_echec": {
        "texte": "Malgré vos efforts, les récoltes sont maigres. Les limaces ont tout dévoré. Déception générale.",
        "conséquences": {"Budget": -8, "CO2": -3, "Santé": +2, "Plaisir": -15},
        "fin": "Apprentissage par l'échec"
    },
    "flexitarien": {
        "texte": "Vous découvrez les protéines végétales. Économie : 200€/mois mais votre ado râle.",
        "conséquences": {"Budget": +20, "CO2": -25, "Santé": +15, "Plaisir": -10},
        "choix": {
            "Prendre des cours de cuisine végétale": "fin_cuisine_revelation",
            "Acheter de la viande labellisée 1x/semaine": "fin_viande_qualite",
            "Installer un poulailler familial": "fin_poulailler_reussi"
        }
    },
    "fin_cuisine_revelation": {
        "texte": "Vos plats végétaux deviennent délicieux. Toute la famille est conquise !",
        "conséquences": {"Budget": +25, "CO2": -35, "Santé": +25, "Plaisir": +20},
        "fin": "Conversion réussie"
    },
    "fin_viande_qualite": {
        "texte": "La viande premium à 50€/kg devient un luxe occasionnel. Votre empreinte carbone baisse drastiquement.",
        "conséquences": {"Budget": -5, "CO2": -30, "Santé": +20, "Plaisir": +15},
        "fin": "Qualité plutôt que quantité"
    },
    "fin_poulailler_reussi": {
        "texte": "4 poules vous fournissent 20 œufs/semaine. Vos voisins adorent le concept !",
        "conséquences": {"Budget": +10, "CO2": -15, "Santé": +5, "Plaisir": +20},
        "fin": "Autonomie alimentaire partielle"
    },

    # BRANCHE LOGEMENT (complète avec fins)
    "logement": {
        "texte": "Votre maison (120m²) consomme 18 000kWh/an. Quel chantier prioritaire ? Budget max : 15 000€",
        "conséquences": {"Budget": -10, "CO2": -10, "Confort": +5, "Valeur": +5},
        "choix": {
            "Isolation des combles (8 000€)": "isolation_combles",
            "Chaudière à granulés (12 000€)": "fin_chaudiere_granules",
            "Panneaux solaires (15 000€)": "fin_solaire_problemes",
            "Récupérateur d'eau + jardin sec": "fin_jardin_sec"
        }
    },
    "fin_chaudiere_granules": {
        "texte": "La chaudière réduit vos émissions de 40%. Mais le prix des granulés triple avec la crise énergétique.",
        "conséquences": {"Budget": -30, "CO2": -25, "Confort": +10, "Valeur": +15},
        "fin": "Solution dépendante aux aléas"
    },
    "fin_solaire_problemes": {
        "texte": "Des problèmes d'installation causent des fuites. Vous passez 6 mois en litige avec l'installateur.",
        "conséquences": {"Budget": -25, "CO2": -5, "Confort": -15, "Valeur": -10},
        "fin": "Mauvaise expérience"
    },
    "fin_jardin_sec": {
        "texte": "Votre jardin résilient survit à la canicule. Mais les voisins critiquent son aspect 'désertique'.",
        "conséquences": {"Budget": +5, "CO2": -20, "Confort": -5, "Valeur": -5},
        "fin": "Choix écologique incompris"
    },
    "isolation_combles": {
        "texte": "L'isolation réduit votre facture de 30%. L'été devient cependant plus chaud sous les toits.",
        "conséquences": {"Budget": +15, "CO2": -25, "Confort": -5, "Valeur": +15},
        "choix": {
            "Ajouter une ventilation double flux (4 000€)": "fin_ventilation_parfaite",
            "Planter des arbres pour l'ombre": "fin_arbres_matures",
            "Installer un store extérieur (1 500€)": "fin_store_efficace"
        }
    },
    "fin_ventilation_parfaite": {
        "texte": "Le système régule parfaitement la température toute l'année. Votre maison devient un modèle !",
        "conséquences": {"Budget": +10, "CO2": -35, "Confort": +25, "Valeur": +30},
        "fin": "Éco-habitat optimisé"
    },
    "fin_arbres_matures": {
        "texte": "Il faudra 10 ans pour que les arbres fassent de l'ombre. Solution durable mais pas immédiate...",
        "conséquences": {"Budget": +5, "CO2": -15, "Confort": +5, "Valeur": +20},
        "fin": "Investissement pour les générations futures"
    },
    "fin_store_efficace": {
        "texte": "Le store supprime les surchauffes estivales. Simple et efficace pour un confort immédiat !",
        "conséquences": {"Budget": +8, "CO2": -10, "Confort": +15, "Valeur": +10},
        "fin": "Solution pragmatique"
    },

    # BRANCHE ENGAGEMENT (complète avec fins)
    "engagement": {
        "texte": "Vous avez 5h/semaine à consacrer à l'écologie. Quelle action choisir ?",
        "conséquences": {"Budget": 0, "CO2": -5, "Réseau": +15, "Épanouissement": +10},
        "choix": {
            "Devenir bénévole dans une recyclerie": "fin_recyclerie_epuisant",
            "Créer un compost de quartier": "compost_quartier",
            "Organiser des clean walks": "fin_clean_walk_mediatique",
            "Militer pour une école durable": "fin_ecole_durable_bloquee"
        }
    },
    "fin_recyclerie_epuisant": {
        "texte": "Le travail physique est épuisant. Vous abandonnez après 3 mois, frustré par le manque d'impact.",
        "conséquences": {"Budget": -5, "CO2": -2, "Réseau": +5, "Épanouissement": -10},
        "fin": "Désillusion bénévole"
    },
    "fin_clean_walk_mediatique": {
        "texte": "Votre action est médiatisée. La mairie prend le relais mais vous vole la vedette.",
        "conséquences": {"Budget": 0, "CO2": -15, "Réseau": +25, "Épanouissement": +5},
        "fin": "Impact réel mais reconnaissance volée"
    },
    "fin_ecole_durable_bloquee": {
        "texte": "L'administration bloque vos initiatives. Après 1 an de combat, vous baissez les bras.",
        "conséquences": {"Budget": -3, "CO2": -5, "Réseau": +10, "Épanouissement": -15},
        "fin": "Résistance bureaucratique"
    },
    "compost_quartier": {
        "texte": "20 familles participent à votre compost. La mairie vous propose de l'étendre à tout le quartier.",
        "conséquences": {"Budget": +5, "CO2": -20, "Réseau": +30, "Épanouissement": +25},
        "choix": {
            "Accepter avec un budget municipal": "fin_compost_officiel",
            "Former des référents bénévoles": "fin_referents_impliques",
            "Créer une association": "fin_association_leader"
        }
    },
    "fin_compost_officiel": {
        "texte": "Le projet devient municipal mais perd son âme citoyenne. Vous êtes mis à l'écart.",
        "conséquences": {"Budget": +10, "CO2": -15, "Réseau": +5, "Épanouissement": -5},
        "fin": "Institutionnalisation décevante"
    },
    "fin_referents_impliques": {
        "texte": "Votre réseau de 15 bénévoles autonomes fait des émules dans d'autres quartiers !",
        "conséquences": {"Budget": +5, "CO2": -25, "Réseau": +50, "Épanouissement": +40},
        "fin": "Démultiplication réussie"
    },
    "fin_association_leader": {
        "texte": "Votre association 'Verts Ensemble' compte 50 membres. Vous obtenez un local municipal !",
        "conséquences": {"Budget": +10, "CO2": -15, "Réseau": +50, "Épanouissement": +40},
        "fin": "Leader écologique local"
    },

    # BRANCHE CONSOMMATION (complète avec fins)
    "consommation": {
        "texte": "Votre famille génère 30kg de déchets/semaine. Quelle nouvelle habitude adopter ?",
        "conséquences": {"Budget": +5, "CO2": -10, "Pratique": -5, "Exemplarité": +10},
        "choix": {
            "Passer au vrac uniquement": "fin_vrac_contraignant",
            "Acheter d'occasion systématiquement": "fin_occasion_limite",
            "Lancer un défi zéro déchet": "zero_dechet",
            "Fabriquer ses produits ménagers": "fin_produits_maison_risque"
        }
    },
    "fin_vrac_contraignant": {
        "texte": "La logistique devient infernale. Après 2 mois, vous gardez seulement quelques basiques en vrac.",
        "conséquences": {"Budget": +10, "CO2": -15, "Pratique": -20, "Exemplarité": +5},
        "fin": "Changement partiel"
    },
    "fin_occasion_limite": {
        "texte": "Vous trouvez 70% de vos besoins. Pour le reste, vous faites des exceptions qui grèvent votre bilan.",
        "conséquences": {"Budget": +15, "CO2": -20, "Pratique": -10, "Exemplarité": +15},
        "fin": "Réussite mitigée"
    },
    "fin_produits_maison_risque": {
        "texte": "Une mauvaise recette abîme votre lave-linge. Réparation coûteuse : l'économie est annulée.",
        "conséquences": {"Budget": -25, "CO2": -5, "Pratique": -15, "Exemplarité": +5},
        "fin": "Apprentissage coûteux"
    },
    "zero_dechet": {
        "texte": "En 6 mois, vous passez à 5kg/semaine. Votre blog inspire 1 000 abonnés !",
        "conséquences": {"Budget": +30, "CO2": -25, "Pratique": +10, "Exemplarité": +40},
        "choix": {
            "Donner des conférences": "fin_conferences_inspirantes",
            "Ouvrir une épicerie collaborative": "fin_epicerie_communautaire",
            "Écrire un guide pratique": "fin_guide_reference"
        }
    },
    "fin_conferences_inspirantes": {
        "texte": "Votre TEDx est vu 500 000 fois. Vous devenez consultant pour des entreprises !",
        "conséquences": {"Budget": +50, "CO2": -30, "Pratique": +25, "Exemplarité": +60},
        "fin": "Influenceur écolo"
    },
    "fin_epicerie_communautaire": {
        "texte": "Votre épicerie 'La Boîte Verte' emploie 3 personnes. Vous êtes interviewé dans le journal local !",
        "conséquences": {"Budget": +50, "CO2": -40, "Pratique": +30, "Exemplarité": +60},
        "fin": "Entrepreneur écologique"
    },
    "fin_guide_reference": {
        "texte": "Votre livre devient un best-seller. 20 000 familles adoptent vos méthodes !",
        "conséquences": {"Budget": +40, "CO2": -50, "Pratique": +20, "Exemplarité": +70},
        "fin": "Auteur à impact"
    }
},

    ####### BRANCHE ENTREPRENEUR
    # Scénario : Entrepreneur d'Écoville
    "entrepreneur": {
    "début": {
        "texte": "Vous dirigez GreenTech, une PME de 50 employés spécialisée en conseil IT. Votre objectif : concilier croissance et neutralité carbone d'ici 2027.",
        "choix": {
            "Lancer une stratégie RSE ambitieuse": "strategie_rse",
            "Optimiser l'énergie des bureaux": "optimisation_energie",
            "Revolutionner la mobilité des employés": "mobilite_employes",
            "Transformer la chaine logistique": "logistique_durable",
            "Innover via l'économie circulaire": "economie_circulaire"
        }
    },

    # BRANCHE STRATÉGIE RSE (complète avec fins)
    "strategie_rse": {
        "texte": "Vous embauchez un responsable RSE. Quel axe prioriser en premier ? Budget : 200k€/an",
        "conséquences": {"Environnement": +15, "Finances": -20, "Image": +25, "Employés": +10},
        "choix": {
            "Certification B Corp": "certification_bcorp",
            "Bilan carbone complet": "fin_bilan_perturbant",
            "Formation tous les employés": "fin_formation_superficielle",
            "Politique d'achats responsables": "fin_achats_couteux"
        }
    },
    "fin_bilan_perturbant": {
        "texte": "Les résultats catastrophiques (120t CO2/an) démoralisent les équipes. Aucune action concrète ne suit.",
        "conséquences": {"Environnement": 0, "Finances": -25, "Image": -15, "Employés": -20},
        "fin": "Prise de conscience stérile"
    },
    "fin_formation_superficielle": {
        "texte": "Les formations obligatoires sont bâclées. Les employés perçoivent ça comme du greenwashing.",
        "conséquences": {"Environnement": +5, "Finances": -15, "Image": -10, "Employés": -25},
        "fin": "Effet contre-productif"
    },
    "fin_achats_couteux": {
        "texte": "Vos nouveaux fournisseurs 'verts' sont 30% plus chers. La trésorerie souffre sans gain visible.",
        "conséquences": {"Environnement": +10, "Finances": -40, "Image": +5, "Employés": 0},
        "fin": "Surcoût non maîtrisé"
    },
    "certification_bcorp": {
        "texte": "Le processus prend 18 mois et coûte 50k€. Vos valeurs attirent de nouveaux talents !",
        "conséquences": {"Environnement": +10, "Finances": -15, "Image": +40, "Employés": +25},
        "choix": {
            "Communiquer largement": "fin_com_bcorp_reussie",
            "Cibler les clients éthiques": "fin_clients_ethiques_limités",
            "Créer un comité de suivi": "fin_comite_bureaucratique"
        }
    },
    "fin_com_bcorp_reussie": {
        "texte": "Votre campagne 'Tech for Good' génère 15 leads qualifiés et une couverture médiatique !",
        "conséquences": {"Environnement": +5, "Finances": +30, "Image": +50, "Employés": +20},
        "fin": "Succès business et éthique"
    },
    "fin_clients_ethiques_limités": {
        "texte": "Le marché reste niche. Vos revenus stagnent malgré la notoriété.",
        "conséquences": {"Environnement": +15, "Finances": -10, "Image": +30, "Employés": +15},
        "fin": "Positionnement courageux mais difficile"
    },
    "fin_comite_bureaucratique": {
        "texte": "Les réunions interminables tuent l'innovation. La certification devient une coquille vide.",
        "conséquences": {"Environnement": +5, "Finances": -20, "Image": +15, "Employés": -10},
        "fin": "Usine à gaz interne"
    },

    # BRANCHE OPTIMISATION ÉNERGIE (complète avec fins)
    "optimisation_energie": {
        "texte": "Vos bureaux consomment 80 000 kWh/an. Quel investissement prioritaire ? Budget max : 150k€",
        "conséquences": {"Environnement": +20, "Finances": -25, "Image": +15, "Employés": +5},
        "choix": {
            "Panneaux solaires (120k€)": "solaire",
            "Isolation complète (80k€)": "fin_isolation_partielle",
            "Capteurs intelligents (30k€)": "fin_capteurs_illusoires",
            "Chaudière biomasse (100k€)": "fin_biomasse_problemes"
        }
    },
    "fin_isolation_partielle": {
        "texte": "Seuls 60% des défauts sont corrigés. Les économies réelles sont décevantes (-15% seulement).",
        "conséquences": {"Environnement": +10, "Finances": -5, "Image": +5, "Employés": +5},
        "fin": "Demi-succès frustrant"
    },
    "fin_capteurs_illusoires": {
        "texte": "Les données affluent mais personne ne les utilise. L'effet est nul sur la consommation réelle.",
        "conséquences": {"Environnement": +2, "Finances": -10, "Image": +3, "Employés": 0},
        "fin": "Technologie sans usage"
    },
    "fin_biomasse_problemes": {
        "texte": "La chaudière tombe en panne 3 fois en 6 mois. Les employés se plaignent du froid en hiver.",
        "conséquences": {"Environnement": +5, "Finances": -35, "Image": -10, "Employés": -20},
        "fin": "Mauvaise solution technique"
    },
    "solaire": {
        "texte": "Votre toiture produit 60% de vos besoins. Le surplus est revendu à EDF.",
        "conséquences": {"Environnement": +35, "Finances": +5, "Image": +25, "Employés": +15},
        "choix": {
            "Stockage sur batteries (50k€)": "fin_batteries_autonomie",
            "Revoir les plages horaires de travail": "fin_horaires_inadaptés",
            "Créer une coopérative énergétique": "fin_cooperative_lourde"
        }
    },
    "fin_batteries_autonomie": {
        "texte": "Votre autonomie atteint 85%. Vous survivez à une panne de réseau de 3 jours !",
        "conséquences": {"Environnement": +45, "Finances": +15, "Image": +40, "Employés": +30},
        "fin": "Indépendance énergétique"
    },
    "fin_horaires_inadaptés": {
        "texte": "Adapter les horaires aux pics solaires perturbe les clients. Vous revenez au modèle standard.",
        "conséquences": {"Environnement": +20, "Finances": -10, "Image": -5, "Employés": -15},
        "fin": "Expérience abandonnée"
    },
    "fin_cooperative_lourde": {
        "texte": "La gestion collective prend trop de temps. Vous vous retirez au bout d'un an.",
        "conséquences": {"Environnement": +25, "Finances": -20, "Image": +15, "Employés": -5},
        "fin": "Belle idée, réalité complexe"
    },

    # BRANCHE MOBILITÉ (complète avec fins)
    "mobilite_employes": {
        "texte": "Les trajets domicile-travail représentent 60% de votre empreinte carbone. Solution ?",
        "conséquences": {"Environnement": +25, "Finances": -10, "Image": +20, "Employés": -5},
        "choix": {
            "Prime transport vert (500€/an)": "fin_prime_peu_utilisée",
            "Flotte de vélos électriques": "fin_velos_sous_utilisés",
            "Télétravail obligatoire 3j/semaine": "teletravail",
            "Déménager près d'une gare": "fin_demenagement_raté"
        }
    },
    "fin_prime_peu_utilisée": {
        "texte": "Seuls 15% des employés en profitent. L'impact global est négligeable.",
        "conséquences": {"Environnement": +5, "Finances": -8, "Image": +5, "Employés": +5},
        "fin": "Mesure cosmétique"
    },
    "fin_velos_sous_utilisés": {
        "texte": "Les 10 vélos achetés servent surtout l'été. 80% du temps au garage.",
        "conséquences": {"Environnement": +8, "Finances": -15, "Image": +10, "Employés": +3},
        "fin": "Équipement peu efficace"
    },
    "fin_demenagement_raté": {
        "texte": "Le nouveau local est mal desservi. 5 démissions clés suivent le déménagement.",
        "conséquences": {"Environnement": +15, "Finances": -50, "Image": -20, "Employés": -40},
        "fin": "Erreur stratégique"
    },
    "teletravail": {
        "texte": "Productivité +12% mais certains employés s'isolent. Vous perdez 3 talents clés.",
        "conséquences": {"Environnement": +40, "Finances": +20, "Image": +10, "Employés": -25},
        "choix": {
            "Améliorer les outils digitaux": "fin_outils_collab",
            "Créer des espaces de coworking": "fin_coworking_reussi",
            "Instaurer des semaines thématiques": "fin_semaines_inutiles"
        }
    },
    "fin_outils_collab": {
        "texte": "L'investissement dans Slack et Zoom redynamise les échanges. La productivité remonte !",
        "conséquences": {"Environnement": +35, "Finances": +15, "Image": +20, "Employés": +25},
        "fin": "Transition numérique réussie"
    },
    "fin_coworking_reussi": {
        "texte": "3 espaces partagés en ville réduisent l'isolement. 85% de satisfaction employés !",
        "conséquences": {"Environnement": +30, "Finances": -15, "Image": +35, "Employés": +40},
        "fin": "Flexibilité réussie"
    },
    "fin_semaines_inutiles": {
        "texte": "Les employés jugent ces réunions obligatoires inutiles. Morale en baisse.",
        "conséquences": {"Environnement": +25, "Finances": -5, "Image": -5, "Employés": -15},
        "fin": "Fausse bonne idée"
    },

    # BRANCHE LOGISTIQUE (complète avec fins)
    "logistique_durable": {
        "texte": "Votre supply chain émet 120 tonnes CO2/an. Par où commencer ? Budget : 80k€",
        "conséquences": {"Environnement": +30, "Finances": -20, "Image": +25, "Employés": +5},
        "choix": {
            "Optimiser les tournées": "fin_tournees_gains_faibles",
            "Passer aux véhicules électriques": "flotte_electrique",
            "Localiser chez fournisseurs verts": "fin_fournisseurs_chers",
            "Compenser les émissions": "fin_compensation_controversee"
        }
    },
    "fin_tournees_gains_faibles": {
        "texte": "Les gains sont marginaux (-8% CO2) et perturbent les délais clients.",
        "conséquences": {"Environnement": +5, "Finances": -5, "Image": +5, "Employés": -10},
        "fin": "Optimisation limitée"
    },
    "fin_fournisseurs_chers": {
        "texte": "Les coûts augmentent de 25% pour -15% CO2. Votre marge souffre.",
        "conséquences": {"Environnement": +10, "Finances": -35, "Image": +15, "Employés": 0},
        "fin": "Équation économique difficile"
    },
    "fin_compensation_controversee": {
        "texte": "Un journal révèle que vos crédits carbone sont fictifs. Scandale médiatique !",
        "conséquences": {"Environnement": -20, "Finances": -15, "Image": -40, "Employés": -25},
        "fin": "Greenwashing exposé"
    },
    "flotte_electrique": {
        "texte": "5 utilitaires électriques achetés. Autonomie insuffisante pour les longues distances.",
        "conséquences": {"Environnement": +45, "Finances": -30, "Image": +35, "Employés": +15},
        "choix": {
            "Installer des bornes rapides": "fin_bornes_entreprise",
            "Sous-traiter les longs trajets": "fin_sous_traitance_couteuse",
            "Négocier des batteries de rechange": "fin_batteries_introuvables"
        }
    },
    "fin_bornes_entreprise": {
        "texte": "Vos bornes alimentées au solaire deviennent un argument commercial !",
        "conséquences": {"Environnement": +60, "Finances": +10, "Image": +50, "Employés": +25},
        "fin": "Logistique décarbonée"
    },
    "fin_sous_traitance_couteuse": {
        "texte": "Les sous-traitants thermiques annulent vos gains écologiques. Coût +40%.",
        "conséquences": {"Environnement": +10, "Finances": -50, "Image": -5, "Employés": -10},
        "fin": "Fausse solution"
    },
    "fin_batteries_introuvables": {
        "texte": "La pénurie mondiale rend les batteries indisponibles. Vos véhicules sont inutilisables 30% du temps.",
        "conséquences": {"Environnement": +20, "Finances": -40, "Image": -15, "Employés": -20},
        "fin": "Dépendance technologique"
    },

    # BRANCHE ÉCONOMIE CIRCULAIRE (complète avec fins)
    "economie_circulaire": {
        "texte": "Comment donner une seconde vie à vos 200 équipements IT ? Budget initial : 50k€",
        "conséquences": {"Environnement": +40, "Finances": +5, "Image": +30, "Employés": +20},
        "choix": {
            "Créer un atelier de reconditionnement": "reconditionnement",
            "Lancer un programme de location": "fin_location_echec",
            "Participer à un écosystème d'échange": "fin_ecosysteme_limite",
            "Transformer les déchets en ressources": "fin_upcycling_niche"
        }
    },
    "fin_location_echec": {
        "texte": "Les clients préfèrent acheter. Taux d'adoption : 12%. Vous liquidatez le stock à perte.",
        "conséquences": {"Environnement": +15, "Finances": -30, "Image": +10, "Employés": -5},
        "fin": "Modèle non viable"
    },
    "fin_ecosysteme_limite": {
        "texte": "Peu d'entreprises participent. Vous échangez 5% de vos équipements seulement.",
        "conséquences": {"Environnement": +20, "Finances": -10, "Image": +15, "Employés": +5},
        "fin": "Réseau insuffisant"
    },
    "fin_upcycling_niche": {
        "texte": "Vos créations artistiques à base de déchets électroniques trouvent peu d'acheteurs.",
        "conséquences": {"Environnement": +25, "Finances": -20, "Image": +20, "Employés": +10},
        "fin": "Marché trop étroit"
    },
    "reconditionnement": {
        "texte": "Votre atelier emploie 3 techniciens et génère 30k€/an de revenus !",
        "conséquences": {"Environnement": +50, "Finances": +25, "Image": +45, "Employés": +35},
        "choix": {
            "Former des publics fragiles": "fin_insertion_remarquable",
            "Développer une marque propre": "fin_marque_propre_renommee",
            "Ouvrir un repair café public": "fin_repair_cafe_emblematique"
        }
    },
    "fin_insertion_remarquable": {
        "texte": "Votre programme forme 12 personnes éloignées de l'emploi par an. La région vous subventionne !",
        "conséquences": {"Environnement": +45, "Finances": +20, "Image": +60, "Employés": +50},
        "fin": "Impact social maximal"
    },
    "fin_marque_propre_renommee": {
        "texte": "GreenTech Renew devient leader régional du reconditionné. Chiffre d'affaires +25% !",
        "conséquences": {"Environnement": +55, "Finances": +40, "Image": +50, "Employés": +30},
        "fin": "Success-story économique"
    },
    "fin_repair_cafe_emblematique": {
        "texte": "Votre espace devient un lieu emblématique. La mairie vous décerne un prix !",
        "conséquences": {"Environnement": +70, "Finances": +15, "Image": +75, "Employés": +50},
        "fin": "Modèle économique circulaire"
    }
}
}

# ====================
# INSTRUCTIONS
# ====================
INSTRUCTIONS = """
## 📚 Comment jouer ?

1. **Choisissez un rôle** : Maire, citoyen ou entrepreneur
2. **Prenez des décisions** : À chaque étape, sélectionnez une option
3. **Observez les conséquences** : Votre score écologique évolue
4. **Explorez tous les chemins** : Rejouez pour découvrir des fins alternatives

💡 Conseil : Certains choix mènent à des surprises !
"""

# ====================
# FONCTION PRINCIPALE
# ====================
def main():
    st.set_page_config(page_title="EcoStory", page_icon="🌍")
    
    # Section instructions
    if "vu_instructions" not in st.session_state:
        st.markdown(INSTRUCTIONS)
        if st.button("Commencer le jeu"):
            st.session_state.vu_instructions = True
            st.rerun()
        return
    
    # Initialisation session
    if "scenario" not in st.session_state:
        st.session_state.scenario = None
        st.session_state.etape = "début"
        st.session_state.scores = {"Écologie": 50, "Économie": 50, "Social": 50}
    
    # Sélection scénario
    if not st.session_state.scenario:
        st.title("🌍 EcoStory - Choisissez votre rôle")
        scenario = st.selectbox("", list(ARBRE.keys()))
        if st.button("Valider"):
            st.session_state.scenario = scenario
            st.rerun()
        return
    
    # Déroulement du jeu
    st.title(f"🌱 EcoStory - {st.session_state.scenario.capitalize()}")
    
    # Affichage scores
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Écologie", st.session_state.scores["Écologie"])
    with col2:
        st.metric("Économie", st.session_state.scores["Économie"])
    with col3:
        st.metric("Social", st.session_state.scores["Social"])
    
    # Récupération données étape
    etape_data = ARBRE[st.session_state.scenario][st.session_state.etape]
    
    # Affichage texte
    st.markdown(f"### {etape_data['texte']}")
    
    # Mise à jour scores
    if "conséquences" in etape_data:
        for k, v in etape_data["conséquences"].items():
            if k in st.session_state.scores:
                st.session_state.scores[k] += v
    
    # Affichage conséquences
    if "conséquences" in etape_data:
        with st.expander("📊 Conséquences de votre décision"):
            st.json(etape_data["conséquences"])
    
    # Gestion choix
    if "choix" in etape_data:
        choix = st.radio("Votre décision :", list(etape_data["choix"].keys()))
        if st.button("Valider"):
            st.session_state.etape = etape_data["choix"][choix]
            st.rerun()
    elif etape_data.get("fin"):
        st.balloons()
        st.success("🎉 Fin de cette aventure !")
        if st.button("Rejouer"):
            st.session_state.clear()
            st.rerun()

if __name__ == "__main__":
    main()