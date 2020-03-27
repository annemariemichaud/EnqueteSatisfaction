#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:31:15 2020

@author: Anne-Marie Michaud
"""
#import modules
import pandas as pd

#loading datas
df_resultats = pd.read_excel('Tableau_resultats_enquete_satisfaction_20182019.xlsx', sheet_name='resultats')

#renommer les colonnes
df_resultats.rename(columns={"Qui est à l'initiative de votre participation à cette formation ?":'initiative',
                             'les objectifs à atteindre ?':'objectifs', 
                            'Dans quel cadre vous êtes vous inscrit à ce dispositif ?':'cadre',
                            'les contenus ?':'contenus',
                            'les méthodes pédagogiques ?':'methodes',
                            "l'animation ?":'animation',
                            'la qualité des supports pédagogiques ?':'qualite_support',
                            'les échanges avec les autres stagiaires, la cohésion du groupe ?':'echanges',
                            'Que pensez-vous de la durée de la formation ?':'duree',
                            'Une partie du s ... elle été proposée sur la plateforme de formation M@gistère ?':'magistere',
                            "Si oui, qu'avez vous pensé de ce prolongement de formation à distance ?":'avis_magistere',
                            'Quels acquis avez-vous tirés de la formation ?':'acquis',
                            'En liaison avec ... , quels nouveaux besoins de formation avez-vous identifiés ?':'besoins'},inplace=True)

#compter le nombre de réponses par stage
df_resultats['nb_reponses'] = df_resultats.groupby(['numero_dispositif','numero_module','groupe','date_derniere_session'])['objectifs'].transform('count')

#calculer les moyennes sur les variables quantitatives
df_synthese=df_resultats.groupby(['numero_dispositif','numero_module','groupe','date_derniere_session']).mean()