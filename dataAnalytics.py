# import needed packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# load data
housingData = pd.read_csv("kc_house_data.csv")
pd.DataFrame.head(housingData)