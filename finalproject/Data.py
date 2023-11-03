import numpy as np

class Data:
    def __init__(self):
        self.filename1 = "finalproject/Country_Data.csv"
        self.filename2 = "finalproject/Population_Data.csv"
        self.filename3 = "finalproject/Threatened_Species.csv"
        self.country_Data = np.genfromtxt(self.filename1, delimiter = ',', skip_header = True, dtype = str)
        self.population_Data = np.genfromtxt(self.filename2, delimiter = ',', skip_header = True, dtype = str)
        self.species_Data = np.genfromtxt(self.filename3, delimiter = ',', skip_header = True, dtype = str)
