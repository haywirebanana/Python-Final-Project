import numpy as np
import matplotlib.pyplot as plt
import math

from Data import Data
 
class DataAnalyzer:                                                                             #class analyzes the data
    def __init__(self, region = None , sub_Region = None, country = None):
        self.region = region
        self.sub_Region = sub_Region
        self.country = country

    def get_Regions(self):
        '''
        This function collects all the regions
        arguments: self
        returns: regions
        '''
        Regions = ['Asia', 'Americas', 'Europe', 'Africa', 'Oceania']
        return Regions

    def get_SubRegions(self):
        '''
        This function collects all the sub-regions
        argumnents: self
        returns: sub_RegionList 
        '''
        point = np.where(self.region == Data().country_Data[:,1])                                   #creates an array of indexes where the region is equal to a point on the second column
        emptyList = []                                                                              #creates an empty list
        for i in point[0]:                                                                          #iterates through the first column of the index
            emptyList.append(Data().country_Data[i,2])                                              #adds the data from country_data at the given index at the third column to the empty list
        sub_RegionList = list(dict.fromkeys(emptyList))                                             #creates a sub-region list from the empty list
        return sub_RegionList

    def get_Countries(self):
        '''
        This functions collects all the countries
        argumnents: self
        returns: countries_List
        '''
        point = np.where(self.sub_Region == Data().country_Data[:,2])                               #creates an array of indexes where the sub-region is equal to a point on the third column 
        emptyList = []                                                                              #creates an empty list
        for i in point[0]:                                                                          #iterates through the first column of the given index
            emptyList.append(Data().country_Data[i,0])                                              #adds the data from country_data at the given index at the first column to the empty list                                      
        countries_List = list(dict.fromkeys(emptyList))
        countries_List = np.array(countries_List)                                                   #creates an array of the list of countries
        return countries_List

    def get_RegionData(self):
        '''
        Returns numpy array with desired region data from Country_Data.csv
        argumnents: self
        returns: Region_Data
        '''
        point = np.where(self.region == Data().country_Data[:,1])                                   #creates an array of indexes where the region is equal to a point on the second column
        Region_Data = np.empty((0,4))                                                               #creates an empty array with 4 columns
        for i in point[0]:                                                                          #iterates through the first column of the given index
            country_Data = np.array([Data().country_Data[i]])                                       #creates an array of row i in country_data
            Region_Data = np.append(Region_Data, country_Data, axis = 0)                            #adds the rows from the country_data to region_data
        return Region_Data

    def get_SubRegionData(self): 
        '''
        Returns numpy array with desired subregion data from Country_Data.csv
        argumnents: self
        returns: subregion_Data
        '''
        point = np.where(self.sub_Region == Data().country_Data[:,2])                               #creates an array of indexes where the sub-region is equal to a point on the third column 
        subRegion_Data = np.empty((0,4))                                                            #creates an empty array with 4 columns
        for i in point[0]:                                                                          ##iterates through the first column of the given index
            country_Data = np.array([Data().country_Data[i]])                                       #creates an array of row i in country_data
            subregion_Data = np.append(subRegion_Data, country_Data, axis = 0)                      #adds the rows from the country_data to subRegion_data
        return subregion_Data

    def get_CountryPopulationData(self): 
        '''
        Returns desired country numpy array from Population_Data.csv
        argumnents: self
        returns:countryPopulationData
        '''
        point = np.where(self.country == Data().population_Data[:,0])[0][0]                         #finds index of country in population_Data
        countryPopulationData = np.array(Data().population_Data[point])[1:22]                       #creates an array of the population_data at the point
        return countryPopulationData

    def get_CountrySpeciesData(self): 
        '''
        Returns desired country numpy array from Population_Data.csv
        argumnents: self
        returns: countrySpeciesData
        '''
        point = np.where(self.country == Data().species_Data[:,0])[0][0]                            #finds index of country in species_Data
        countrySpeciesData = np.array(Data().species_Data[point])[1:5]                              #creates an array of the species_data at the point
        return countrySpeciesData

    def get_Country_SquareKm(self):
        '''
        This function returns the desired array of a country's square km
        argumnents: self
        returns:countrySqureKm
        '''
        point = np.where(self.country == Data().country_Data[:,0])[0][0]                            #finds index of country in country_Data
        countrySquareKm = np.array(Data().country_Data[point])[3]                                   #creates an array of the country_data at the point
        return countrySquareKm

    def get_MeanPopulation(self):
        '''
        This function returns the mean of the population from the desired country
        argumnents: self
        returns:populationMean
        '''
        data = (self.get_CountryPopulationData()).astype(float)                                     #converts the array from get_CountryPopulationData and turns it into a float
        populationMean = data.mean()                                                                #gets the mean from data
        return populationMean

    def get_MaxPopulation(self):
        '''
        This function returns the max population from the desired country
        argumnents: self
        returns: get_MinPopulation
        '''
        data = (self.get_CountryPopulationData()).astype(float)                                     #converts the array from get_CountryPopulationData into a float
        populationMax = data.max()                                                                  #gets the max of the data
        return populationMax

    def get_MinPopulation(self):
        '''
        This function returns the min population from the desired country
        argumnents: self
        returns: populationMin
        '''
        data = (self.get_CountryPopulationData()).astype(float)                                     #converts the array from get_CountryPopulationData into a float
        populationMin = data.min()                                                                  #gets the min of the data
        return populationMin
    
    def get_PopDensity(self):
        '''
        This function returns the population density from the desired country
        argumnents: self
        returns: PopDensity
        '''
        population = (self.get_CountryPopulationData()[20].astype(float))                           #converts the latest comlumn from the array from get_CountryPopulationData into a float
        square_km = (self.get_Country_SquareKm().astype(float))                                     #converts the array from get_Country_SquareKm into a float
        PopDensity = population / square_km                                                         #calculates population density by dividing population to square_km
        return PopDensity  