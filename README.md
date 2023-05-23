Customer Segmentation est un systeme de segmentation de la clientèle, un moyen d’organiser vos prospects, contacts et clients par caractéristiques communes pour leur fournir des informations ciblées, une expérience personnalisée et des produits qui leur parlent.

Dans le cadre de notre projet, on s'interresse à un constructeur automobile qui prévoit de pénétrer de nouveaux marchés avec ses produits existants (P1, P2, P3, P4 et P5). Après une étude de marché intensive, ils en ont déduit que le comportement du nouveau marché est similaire à celui de leur marché existant.

Sur leur marché existant, l’équipe commerciale a classé tous les clients en 4 segments (A, B, C, D). Ensuite, ils ont effectué une sensibilisation et une communication segmentées pour différents segments de clients. Cette stratégie a exceptionnellement bien fonctionné pour eux. Ils prévoient d’utiliser la même stratégie sur de nouveaux marchés et ont identifié 2627 nouveaux clients potentiels.

Notre mission sera d'aider le gestionnaire à prédire le bon groupe de nouveaux clients






Pour chaque critère, la métrique de similarité est calculée. Le synopsis et les similitudes de genre sont obtenus en utilisant la similarité cosinus et BERT. La similitude de la période littéraire est calculée comme une fonction mathématique basée sur les années pendant lesquelles les auteurs étaient actifs. La métrique d’attribution est désignée comme une variable binaire. En fonction des préférences de l’utilisateur, SeREADipidity recommande 10 livres en fonction du score de similarité global. Le score de similarité global est calculé comme une fonction linéaire du synopsis similituy, de la similitude de la période littéraire, de la similitude de genre et de la métrique de récompense.

Plus de détails sur le pipeline peuvent être trouvés ici.

Voici la capture d’écran des recommandations de livre pour L’origine des espèces basées sur un genre et un synopsis similaires.


Conditions préalables
pandas==0.24.2
scikit_learn==0,23,1
streamlit==0.62.1
Pour exécuter l’application localement
Pour obtenir la recommandation de livre localement sur votre ordinateur, téléchargez les fichiers à partir du dossier /SeREADipity/sereadipity. Modifiez le chemin d’accès à l’emplacement correspondant sur votre machine.

Sur le terminal, utilisez la commande pour obtenir une recommandation similaire au livre que vous avez apprécié! :)streamlit run sereadipity.py
