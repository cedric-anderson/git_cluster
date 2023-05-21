SeREADipity est un système de recommandation de livres personnalisé qui permet aux utilisateurs d’évaluer leurs préférences (sur une échelle de 1 à 10) sur différents critères - synopsis, période littéraire, genre et livre d’un auteur primé.

SeREADipity utilise près de 9 000 livres (après nettoyage des données) et les détails des auteurs correspondants de GoodReads et Wikipedia, respectivement.

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
