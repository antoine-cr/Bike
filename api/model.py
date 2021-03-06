# Imporatation des librairies
from pydantic import BaseModel, BaseConfig
from typing import List
from enum import Enum
#from model import pylance

# Définition de l'énumération class WeathersitEnum
class WeathersitEnum(str, Enum):
    ''' cette classe permet de définir des choix au nombre de 4 au total '''
    clear = 'clear'
    snowy = 'snowy'
    rainy = 'rainy'
    cloudy = 'cloudy'

class BikeHourData(BaseModel):
    ''' cette classe permet de définir le format des données à envoyer à BikeData '''
    dteday : str
    hr : int
    weathersit : WeathersitEnum
    hum : float
    windspeed : float
    temp : float
    atemp : float
    cnt : int

    class Config(BaseConfig):
        extra = "forbid"

# On recoit les 24 BikeHourData
BikeData = List[BikeHourData]
