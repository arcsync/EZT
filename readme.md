# About
Small ui app to ease transaltion between two languages

# Installation:
pip install googletrans==3.1.0a0

# Usage:
To translate from the top texbox pick a source language in the left combobox  and the destionation language in the right combobox and press the translate down button.

Results will appear in the bottom text box. Use the Translate Up button to translate in the opposite direction ie. from the bottom

text box to the top text box and from the destination language to the source language.


Meant to be used as a UI app only. For command line fuctionality refer directly to the googletrans module.

## NOTE: the translation module uses google translate, but is not officially endorsed by google
this fuctionaly may break when google decides to update its APIs 

# Modification:
To add languages: add items to translateableLanguages


For a full list of supported langauages, refer to https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages