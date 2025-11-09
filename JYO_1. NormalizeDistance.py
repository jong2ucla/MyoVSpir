import os
import pandas as pd

PATH_TO_INPUT_START = "/Users/hannahbailey/Desktop/GLC_Inten/MyoV_WT/20221207_001/Values.csv"
PATH_TO_OUTPUT_START= "/Users/hannahbailey/Desktop/GLC_Inten/MyoV_WT/20221207_001/Values_Normalized.csv"
DataFile = pd.read_csv(PATH_TO_INPUT_START)
DataFile = DataFile.astype(float)
#Checks for calling Data File#
#print()
#print(DataFile.head())
#print(DataFile.tail())
MaxDist = DataFile['Distance_(microns)'].max()
#print(MaxDist)
MaxInten = DataFile['Gray_Value'].max()
MinInten = DataFile['Gray_Value'].min()
#print(MaxInten)
#print(MinInten)
DataFile['Distance_(microns)'] = DataFile['Distance_(microns)']/float(MaxDist)
DataFile['Gray_Value'] = (DataFile['Gray_Value']-float(MinInten))/(float(MaxInten)-float(MinInten))
#Checks for normalization of input data#
#print(DataFile.head())
#print(DataFile.tail())
DataFile.to_csv(PATH_TO_OUTPUT_START, index=False, header=True)