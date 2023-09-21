import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt
from ib_insync import *
# util.startLoop()  # uncomment this line when in a notebook

ib = IB()
ib.connect(host='127.0.0.1', port=4002, clientId=1)

contract = Forex('EURUSD')
bars = ib.reqHistoricalData(
    contract, endDateTime='', durationStr='30 D',
    barSizeSetting='1 hour', whatToShow='MIDPOINT', useRTH=True)

# convert to pandas dataframe (pandas needs to be installed):
df = util.df(bars)

# Now we save this data to a csv file
df.to_csv('EURUSD.csv', index=False)