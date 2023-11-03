#Final Project ENDG 233
#Ryan Khyrss Obiar (30151002) & Aidan Co (30141875)
 
from matplotlib import lines
import numpy as np
from DataAnalyzer import DataAnalyzer
import matplotlib.pyplot as plt

def line_chart(xaxis, yaxis, xlabel, ylabel, title):
    '''
    Creates a line chart
    arguments: xaxis,yaxis,xlabel,ylabel and title
    returns: none
    '''
    plt.plot(xaxis,yaxis,'y', marker = 'o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(xaxis, rotation = 90)                                                                                
    plt.show()

def bar_chart(xaxis, yaxis, xlabel, ylabel, title):
    '''
    Creates a bar chart
    arguments: xaxis,yaxis,xlabel,ylabel and title
    returns: none
    '''
    plt.bar(xaxis, yaxis, align = "center", alpha = 0.5)
    plt.xticks(rotation = 90)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    

def main(): 
    print('\nWelcome to ENDG 233 Country Analysis Program\n')
    print('From the options below, please select a Region.\n')
    a = DataAnalyzer()                                                                                      #creates a variable to access the class
    for i in a.get_Regions():                                                                               #loops through and prints all the regions in the function
        print(i)
    
    while True:
        Region_Input = input('\n-> ')                                                                       #prompts for first user input
        if Region_Input not in a.get_Regions():                                                             #validates if user input is in the regions function
            print("\nInvalid Region, Please Try Again")
        else:
            break

    userinput = DataAnalyzer(Region_Input)                                                                  #sets a new variable for the valid user input
    print(f'\nPlease select a sub-Region from {Region_Input} below.\n')                                     
    for i in userinput.get_SubRegions():                                                                    #loops through and prints all data in subRegion function
        print(i)
    while True:
        subRegion_Input = input('\n-> ')                                                                    #prompts for a second user input
        if subRegion_Input not in userinput.get_SubRegions():                                               #validates if user input is in the subRegions function
            print("\nInvalid sub-Region, Please Try Again")
        else:
            break
    
    userinput = DataAnalyzer(Region_Input, subRegion_Input)                                                 ##sets a new variable for the valid user input
    print(f'\nFrom the choices below, choose a country from {subRegion_Input} for further analysis.\n')
    for i in userinput.get_Countries():                                                                     #loops through and prints all the data in countries function
        print(i)
    while True:
        Country_Input = input('\n-> ')                                                                      #prompts for a third user input
        if Country_Input not in userinput.get_Countries():                                                  #validates if user input is in the Countries function
            print("\nInvalid Country, Please Try Again")
        else:
            break
    userinput = DataAnalyzer(Region_Input, subRegion_Input, Country_Input)                                  #sets a new variable for the valid user input

    print(f"\nCalculating Data for {Country_Input}...\n")

    print(f"Region : {Region_Input}")                                                                       #prints first input as the region
    print(f"sub-Region : {subRegion_Input}")                                                                #prints second input as the subRegion
    print(f"Country : {Country_Input}\n")                                                                   #prints the third input as the country

    population = userinput.get_CountryPopulationData()[20]                                                  #creates a variable for the current population of the chosen country
    print(f'The current Population of {Country_Input} is : {population}')                                   #prints the current population of the chosen country input

    max_pop = userinput.get_MaxPopulation()                                                                 #gets the max population of the user input
    print(f"The Human Population in which {Country_Input} was at it's higest was {max_pop}")                #prints the max population of chosen country
    min_pop = userinput.get_MinPopulation()                                                                 #gets the min population of the user input
    print(f"The Human Population in which {Country_Input} was at its lowest was {min_pop}")                 #prints the min population of the chosen country
    mean_pop = userinput.get_MeanPopulation()                                                               #gets the mean population of the user input
    print(f"The Mean Population of {Country_Input} is {mean_pop}\n")                                        #prints the mean population of the chosen country

    country_species = userinput.get_CountrySpeciesData()                                                    #gets the user input's species data
    print("Number of Threatened Species:")                                                                  #prints all the info of the country's threatened species
    print(f"Plants : {country_species[0]}")
    print(f"Fish : {country_species[1]}")
    print(f"Birds : {country_species[2]}")
    print(f"Mammals : {country_species[3]}\n")


    print(f"Data for Countries in {subRegion_Input}\n")

    print(f"The Current Population - Square Kilometers for all Countries in {subRegion_Input}:\n")          #prints the current pop to square km for all countries in the subRegion input
    for i in userinput.get_Countries():                                                                     #iterates through the user input's country selection
        Country_Input = [i]
        userinput = DataAnalyzer(Region_Input, subRegion_Input, Country_Input)                              
        print(i, end = " : ")                                                                               #prints every country in get_country function
        print(userinput.get_CountryPopulationData()[20], end = " - ")                                       #prints the current population of the user input
        print(f"{userinput.get_Country_SquareKm()} km^2 ")                                                  #prints the square km of the user input
    print()

    print(f"The Rounded Calculted Population Density for all Countries in {subRegion_Input}:\n")            
    for i in userinput.get_Countries():                                                                     #iterates through the user input's country selection
        Country_Input = [i]
        userinput = DataAnalyzer(Region_Input, subRegion_Input, Country_Input)
        print(i, end = ' : ')                                                                               #prints every country in get_country function
        print(f"{userinput.get_PopDensity()} People / km^2" )                                               #prints the population density of the user input
    print()

    print(f"The Total Amount of Threatened Species for all Countries in {subRegion_Input}:\n")
    total_array = np.array([])                                                                              #creates an empty array
    for i in userinput.get_Countries():                                                                     #iterates through the user input's country selection
        Country_Input = [i]
        userinput = DataAnalyzer(Region_Input, subRegion_Input, Country_Input)
        print(i, end = " : ")                                                                               #prints every country in get_country function
        total_species = ((userinput.get_CountrySpeciesData()).astype(float)).sum()                          #collects the sum of all the threatened species from the user input and makes it into a float
        print(total_species)
        total_array = np.append(total_array,total_species)                                                  #adds the empty array and total species

    bar_chart(userinput.get_Countries(), total_array, "Total Species In Each Country", "Countries", "Number of Threatened Species")         #creates a bar chart from the user's country selection and total threatened species
    p2xaxis = np.array([])                                                                                                                  #creates an empty array
    for i in range(2000,2021):                                                                                                              #iterates through the range of years and adds it into the empty array
        p2xaxis = (np.append(p2xaxis, i))
    line_chart(p2xaxis, (userinput.get_CountryPopulationData()).astype(float), "Population Line graph (2000-2020)", "Year", "Population")   #creates a line chart from the years and the user's country population data  
    
if __name__ == '__main__':
    main()