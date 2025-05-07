# Rapport détaillé du stage à la Direction interrégionale Antilles-Guyane de l’Insee

## 1. Introduction

Ce rapport présente le contenu et les résultats du stage effectué au sein de la Direction interrégionale Antilles-Guyane de l’Insee, plus précisément au Service Études et Diffusion (SED) situé à Baie-Mahault en Guadeloupe. Le projet se concentre sur l’analyse des performances financières des entreprises dans les départements et régions d’outre-mer (DROM), avec un accent particulier sur la comparaison avec la métropole. Les résultats entendus seront diffusés sous la forme d’une étude publiée dans la série « Insee Analyses » ainsi qu’un article académique destiné à la revue « Économie et Statistique ». Ce travail s’intègre dans une démarche économique et statistique visant à mieux comprendre les spécificités économiques des DROM dans le contexte national français.

À travers ce stage, une méthodologie rigoureuse mêlant analyse de données, traitement statistique et apprentissage automatique a été mise en œuvre pour évaluer la situation financière des entreprises dromiennes, en s’appuyant sur des données issues de bases administratives et statistiques.

---

## 2. Contextualisation du stage

Le stage s’est déroulé au sein de la Direction interrégionale Antilles-Guyane, une institution clé dans la production et la diffusion des statistiques économiques pour les régions ultramarines françaises. Le contexte géographique favorise une approche localisée des problématiques économiques spécifiques à ces territoires, caractérisés par des contraintes structurelles, des dynamiques économiques distinctes et des besoins particuliers en matière d’analyse économique.

Le cadre institutionnel a permis d’accéder à des bases de données riches et fiables, notamment sur les entreprises inscrites comme unités légales, c’est-à-dire les entités juridiques reconnues par l’administration fiscale et statistique. L’objectif central du stage était d’appliquer des méthodes quantitatives avancées pour étudier les performances financières des entreprises dans ces zones sensibles, en tenant compte des particularités liées à l’outre-mer.

---

## 3. Revue de littérature

La revue de littérature souligne le relatif déficit d’analyse économique concernant les performances financières des entreprises dromiennes comparées à celles de la métropole. Les recherches disponibles restent rares et superficielles, comme en témoignent les travaux de Caupin et Savoye (2012) et Dreyer et Savoye (2013), qui abordent la question sans toutefois en approfondir les dimensions statistiques ou économiques.

Cette lacune justifie pleinement la pertinence du stage et des travaux associés, qui visent à combler ce manque en proposant une étude empirique robuste. La littérature existante ne couvre pas suffisamment les spécificités des entreprises ultramarines ni leur contexte concurrentiel, social et économique particulier. Ainsi, ce travail s’inscrit dans une démarche de développement des connaissances économiques spécifiques aux DROM.

---

## 4. Données et Méthodologie

### 4.1 Données

Les données utilisées proviennent des sources administratives de l’Insee, relatives aux entreprises considérées comme unités légales. Cette base inclut des indicateurs financiers et comptables, obtenus via les déclarations fiscales et les bilans déposés par les sociétés. L’échantillon couvre un large panel d’entreprises évoluant dans différents secteurs d’activités au sein des DROM, offrant une représentation fidèle des réalités économiques locales.

L’extraction et la préparation initiale des données ont dû prendre en compte la présence de valeurs manquantes ou aberrantes, ainsi que la diversité des formats et la complexité des données disponibles.

### 4.2 Méthodes

L’analyse s’appuie sur deux modèles d’apprentissage automatique particulièrement performants pour la classification et la prédiction en contexte multidimensionnel : le modèle Random Forest et le modèle XGBoost.

Ces méthodes permettent de modéliser des comportements complexes des données d’entreprise en permettant d’identifier les facteurs déterminants des performances financières via l’exploitation des variables explicatives et de leurs interactions.

### 4.3 Stratégie empirique

#### 4.3.1 Le modèle Random Forest

Le Random Forest est une méthode d’ensemble basée sur l’agrégation de nombreux arbres de décision, chacun construit sur un sous-échantillon aléatoire des données et des variables. Cela permet de réduire le sur-apprentissage (overfitting) tout en maintenant une performance élevée de prédiction.

Le modèle applique ensuite un vote majoritaire des arbres pour classer ou prédire une variable cible, ici relative à la santé financière des entreprises. Les avantages résident dans sa robustesse face aux données bruitées et dans la capacité à gérer des données hétérogènes et à haute dimensionnalité.

La mise en œuvre comprend des phases de tuning des hyperparamètres comme le nombre d’arbres, la profondeur maximale, la taille des sous-échantillons, etc., afin d’optimiser la précision et la généralisation.

#### 4.3.2 Le modèle XGBoost

XGBoost (eXtreme Gradient Boosting) est une autre approche d’ensemble qui construit des arbres de décision de façon itérative en corrigeant les erreurs des arbres précédents via des gradients. Cette technique est reconnue pour sa rapidité d’exécution et ses performances élevées dans les compétitions d’apprentissage supervisé.

Ce modèle est particulièrement adapté aux données complexes et aux problèmes où la relation entre variables n’est pas linéaire. Le tuning rigoureux des paramètres (taux d’apprentissage, nombre d’arbres, régularisation) est également une étape clé pour maximiser les résultats.

Ces deux méthodes ont été appliquées de manière complémentaire pour comparer leurs performances et valider la robustesse des résultats obtenus.

---

## 5. Gestion des données entreprises

### 5.1 Analyse et traitement des valeurs manquantes

Les données brutes présentaient un certain nombre de valeurs manquantes sur plusieurs variables cruciales, notamment les indicateurs financiers et certaines caractéristiques sectorielles.

Une analyse descriptive a permis d’identifier les patterns de non-réponse, distinguant les valeurs manquantes aléatoires (MCAR) de celles dépendantes de certains facteurs (MAR ou MNAR). Selon ces résultats, plusieurs méthodes de traitement ont été envisagées, avec une préférence pour l’imputation multiple afin de limiter les biais et préserver la variance naturelle des données.

Le recours à des algorithmes d’imputation basés sur les k plus proches voisins (KNN) ou sur des modèles prédictifs intégrant les autres variables disponibles a aussi été exploré pour optimiser la qualité des données.

### 5.2 Analyse et traitement des valeurs aberrantes

Les valeurs aberrantes ont été détectées à travers des outils statistiques classiques (boîtes à moustaches, écart interquartile, score z) complétés par des techniques spécifiques d’analyse multivariée.

Plusieurs observations extrêmes ont été identifiées, parfois issues d’erreurs de saisie ou de déclarations exceptionnelles d’entreprises. Ces outliers ont été examinés au cas par cas pour décider soit de leur exclusion soit d’une correction prudente.

L’attention a été portée à ne pas éliminer des données qui pourraient refléter des phénomènes économiques réels et importants, notamment dans un contexte DROM où certaines entreprises peuvent avoir des profils atypiques.

### 5.3 Choix de la méthode de nettoyage de la base de données

Après analyse, une méthode combinée de nettoyage a été retenue, associant un traitement d’imputation pour les valeurs manquantes avec une gestion modérée des valeurs aberrantes. Cette approche vise à concilier la qualité des données et la représentativité des phénomènes économiques.

Des scripts reproductibles ont été développés pour assurer la traçabilité des opérations et permettre une reproduction aisée des traitements lors de futures analyses.

---

## Conclusion et remerciements

Ce stage a permis de développer une approche méthodologique rigoureuse et innovante pour l’étude des performances des entreprises dans les DROM. Les travaux réalisés contribuent à enrichir la connaissance économique de ces territoires et à soutenir la production statistique à l’Insee.

Je tiens à exprimer ma profonde gratitude à toutes les personnes ayant contribué à ce parcours, en particulier mes collègues et encadrants à l’Insee, ainsi que mes amis proches et ma famille dont le soutien moral et affectif a été indispensable.

---

## Annexes et références

Le rapport complet inclut également une bibliographie étoffée, comprenant notamment les publications de Caupin et Savoye (2012) et Dreyer et Savoye (2013), ainsi que diverses annexes détaillant les spécifications techniques des modèles statistiques, les variables utilisées, les résultats des analyses descriptives et les procédures de traitement des données.

---

Ce rapport constitue un exemple d’application concrète de méthodes statistiques avancées au service d’une analyse économique locale, contribuant ainsi aux missions stratégiques de l’Insee en matière de connaissance des territoires ultramarins.