import random as rd
import pandas as pd



def DataLoad():
    data = pd.read_csv('HansotMenu.csv')
    title_list = data['Menu'].values.tolist()
    return title_list


def PriceLoad(menuName):
    data = pd.read_csv('HansotMenu.csv')
    priceDF = data[data['Menu'] == menuName]
    price = priceDF['Price'].values.tolist()
    return price[0]



PriceLoad('참치마요')
