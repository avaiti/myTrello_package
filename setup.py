#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
# import la lib
import trello_module
 
# appel de fonction. 
setup(
 
    # le nom de votre bibliothèque, tel qu'il apparaitre sur pypi
    name='trello_module',
 
    # la version du code
    version=trello_module.__version__,
 
    # Liste les packages à insérer dans la distribution
    packages=find_packages(),
 
    # auteur
    author="Aurore G. VAITINADAPOULE",
 
    # contact
    author_email="a.vaitinadapoule@gmail.com",
 
    # description 
    description="Module de connection a l'api trello",
 
    # Généralement on dump le README ici
    long_description=open('README.md').read(),
 
    # Active la prise en compte du fichier MANIFEST.in
    include_package_data=True,
 
    # Une url qui pointe vers la page officielle de votre lib
    #url='http://github.com/',
 
    # quelques metadata à propos de sa lib
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
    ],
 
    # C'est un système de plugin, mais on s'en sert presque exclusivement
    # Pour créer des commandes, comme "django-admin".
    # Par exemple, si on veut créer la fabuleuse commande "proclame-sm", on
    # va faire pointer ce nom vers la fonction proclamer(). La commande sera
    # créé automatiquement. 
    # La syntaxe est "nom-de-commande-a-creer = package.module:fonction".
    entry_points = {
        'console_scripts': [
            'trello-cnx = trello_module.mytrello:trelloConnection',
        ],
    },

 
)