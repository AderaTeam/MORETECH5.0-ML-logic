import pickle
import dill
import numpy as np
from requests import get, Response, Request

with open('./functions/XXX.pkl', 'rb') as f:
    get_ambit_of_place = dill.load(f)
    print(get_ambit_of_place(
    text='остановка',
    api_key='246f9164-7a6e-417b-8cc5-91fbf58767c6',
    place_x=str(73.368859), 
    place_y=str(54.991594),
    ambit_x=str(0.552069),
    ambit_y=str(0.400552),
).content)