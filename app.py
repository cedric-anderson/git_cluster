## importation des librairies
import pycaret
from pycaret.clustering import *
import streamlit as st
import pandas as pd
from PIL import Image  

## Chargement de Kmeans model
model = load_model('Final Kmeans Model')

## Fonction de prediction
def predict(model, input_df):
    predictions_df = predict_model(model, data=input_df)
    predictions = predictions_df['Cluster'][0]
    return predictions

## Catching de la fonction load_data (garde en memoir tout fichier deja telecharger)
@st.cache_data
def load_data(file_upload):
    data = pd.read_csv(file_upload)
    return data

## Definition de la fonction
def run():
    
    
    ## ajouter le titre de l'application streamlit
    st.title("Application de segmentation de la clientèle")
    
    ## Chargement de l'image
    image = Image.open('trophé.jpg')
    
    
    ## Contact du concepteur de l'application
    st.sidebar.write('Auteur : Cedric Anderson')
    ## Image dans la sidebar
    st.sidebar.success("Contact : \tcedric.badolo@etu.u-pec.fr \n")
    
    
     ## ajouter des informations sur le fonctionnement de l'application à la barre latérale
    st.sidebar.markdown(
        "**Cette application est crée pour segmenter les clients en fonction de leur caracteristiques**: \n"
        "1. Telechargez votre DataSet sous fichier **CSV** (batch),/ ou predisez pour un individu (on line); \n"
        "2. Cliquez sur le bouton **Browse_files** pour telecharger votre DataSet; \n "
        "3. Cliquez sur le bouton **Profile DataSet** pour voir la prediction par lot; \n "
        "4. Cliquez sur le bouton **Predict** pour voir la prediction par individu"
    )

    ## boîte de sélection faisant un choix entre deux broadways pour prédire de nouveaux points de données
    add_selectbox = st.sidebar.selectbox(
    "Comment aimeriez-vous prédire ?",
    ("Online", "Batch"))
      
    
    ## Image dans la sidebar
    st.sidebar.image('./voiture.jpg')

        
    ## ajouter des étapes à suivre si l'utilisateur sélectionne le mode de prédiction en ligne
    if add_selectbox == 'Online':
        
        ## Zone de saisie categoriel pour obtenir la valeur gender
        Gender = st.selectbox("Gender", ("Male", "Female"))
        
        ## Zone de saisie categoriel pour obtenir la valeur Ever_Married
        Ever_Married = st.selectbox("Ever_Married", ("Yes", "No"))
            
        ## Zone de saisie numérique pour obtenir la valeur d'âge
        Age = st.number_input('Age', min_value=18, max_value=89, value=30)
        
        ## Zone de saisie categoriel pour obtenir la valeur Graduated
        Graduated = st.selectbox("Graduated", ("Yes", "No"))
           
            
        ## Zone de saisie categoriel pour obtenir la valeur Profession
        Profession = st.selectbox("Profession", ['Entertainment', 'Healthcare', 'Artist', 'Doctor', 'Homemaker',
       'Engineer', 'Lawyer', 'Executive', 'Marketing'])

        ## Zone de saisie numérique pour obtenir la valeur de  Work_Experience
        Work_Experience = st.number_input('Work_Experience', min_value=0, max_value=14, value=5)
        
        ## Zone de saisie categoriel pour obtenir la valeur Spending_Score
        Spending_Score = st.selectbox("Spending_Score", ['Low', 'Average', 'High'])

        ## Zone de saisie numérique pour obtenir la valeur de Family_Size
        Family_Size = st.number_input('Family_Size', min_value=1 , max_value=9, value=3)
        
        ## Zone de saisie categoriel pour obtenir la valeur Var_1
        Var_1 = st.selectbox("Var_1", ['Cat_4', 'Cat_6', 'Cat_2', 'Cat_3', 'Cat_1', 'Cat_5', 'Cat_7'])
        
        ## Zone de saisie categoriel pour obtenir la valeur Spending_Score
        Segmentation = st.selectbox("Segmentation", ['D', 'A', 'C', 'B'])
        

        ## définir la variable de sortie 
        output=""

        ## création d'un dictionnaire d'entrée avec toutes les fonctionnalités d'entrée
        input_dict = {'Gender':Gender, 'Ever_Married':Ever_Married ,'Age':Age, 'Graduated':Graduated, 'Profession':Profession, 'Work_Experience':Work_Experience, 'Spending_Score':Spending_Score,'Family_Size':Family_Size, "Var_1":Var_1, "Segmentation":Segmentation }

        ## convertir le dictionnaire d'entrée en une trame de données pandas
        input_df = pd.DataFrame([input_dict])

        ## ajout d'un bouton pour faire des prédictions lorsqu'il est cliqué par l'utilisateur
        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            output =  str(output)

        ## afficher la sortie après une prédiction réussie
        st.success('Resultat : {}'.format(output))
        
       

    ## ajouter des étapes à suivre si l'utilisateur sélectionne le mode de prédiction par lots
    if add_selectbox == 'Batch':

        ## adding a file uploader button for the user to upload the csv file containing data points
        file_upload = st.file_uploader("Veuillez téléchargez le fichier csv pour les prédictions", type=["csv"])

        ## bloc de code à exécuter une fois qu'un fichier csv est téléchargé par l'utilisateur
        if file_upload is not None:
                

            ## reading the csv file using pandas
            #data = pd.read_csv(file_upload)
            data = load_data(file_upload)
            
            ## Afficher les information du DataSet Telecharger
            st.dataframe(data.head())

            
            # Création du bouton de prediction
            if st.button('Profile DataSet'):
                predictions = predict_model(model,data=data)
                
                ## afficher la sortie après une prédiction réussie
                st.success("Prediction Successful !")
                
                ## Afficher la prediction predicitons
                st.dataframe(predictions)

    
            

## calling the main function
if __name__ == '__main__':
    run()