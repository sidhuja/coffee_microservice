import json 
import urllib.request
import time 
import csv 
from csv import DictWriter

def add_coffee_to_csv(coffee_dict, header_list):
    """ Adds coffee dictionary to csv file called "output.csv" """
    # Open CSV file in append mode
    with open('output.csv', 'a') as file_obj:
        dc_obj = DictWriter(file_obj, fieldnames=header_list, extrasaction='ignore')
        
        # Pass the dictionary as an argument to the Writerow()
        dc_obj.writerow(coffee_dict)
                    
        # Close the file object
        file_obj.close() 

def get_coffee_based_on_sweetness(coffee):
    """Takes a coffee dictionary as a parameter and calculates sugar level for each """
    ingredients_list = coffee["ingredients"]

    #initialize sugary items to 0. (0=low 1= medium 2=high)
    sugar_level = 0 

    # iterate over the ingredients
    for ingredient in ingredients_list:
        #print(ingredient)
        if ingredient == "Sugar*" or ingredient == "Sugar":
            sugar_level += 1 
        if ingredient == "Cream*" or ingredient == "Cream":
            sugar_level +=1 
        if ingredient =="Whip*" or ingredient =="Whip":
            sugar_level += 2
        if ingredient =="Ice cream":
            sugar_level += 2
        if ingredient =="Chocolate":
            sugar_level += 1
        if ingredient =="Sweet":
            sugar_level +=1

    return sugar_level 
            
while True:
    time.sleep(1)
    #open the text file for reading
    recipe_file = open("recipe.txt", "r")
    #read line in file 
    recipe_text = recipe_file.readline().strip()
    recipe_file.close()

    if recipe_text =="run":
        # delete previous data on json file 
        csv_file = open("output.csv", "w+")
        csv_file.truncate()
        csv_file.close()

        # add in headers on csv file 
        with open('output.csv', 'a') as f_object:
            header_list =["title", "description", "ingredients", "image"]
            dw = csv.DictWriter(f_object, fieldnames=header_list)
            dw.writeheader()
        
        type_file = open("type.txt", "r")
        temp = type_file.readline().strip()
        type_file.close()

        sweetness_file = open("sweetness.txt", "r")
        sweetness = sweetness_file.readline().strip()
        sweetness_file.close()

            
        print("Getting a coffee based off of temp and sweetness ")
        url = 'https://api.sampleapis.com/coffee/'

        if temp == "iced":
            # get data from api 
            url = url + "iced"
            json_obj = urllib.request.urlopen(url)

            # json obj 
            data = json.load(json_obj)
            
            
            for coffee_dict in data:
                # skip irelivant data 
                if coffee_dict["title"] == "Banana2" or coffee_dict["title"] == "Iced Apple":
                    continue 
            
                sugar_level = get_coffee_based_on_sweetness(coffee_dict)

                if sweetness == "low" and sugar_level == 0:
                    add_coffee_to_csv(coffee_dict, header_list)
                if sweetness =="medium" and sugar_level == 1:
                    add_coffee_to_csv(coffee_dict, header_list)
                if sweetness == "high" and sugar_level >= 2 :
                    add_coffee_to_csv(coffee_dict, header_list)

                # reset sugar level for next coffee 
                sugar_level = 0       

        if temp == "hot":
             # get data from api 
            url = url + "hot"
            json_obj = urllib.request.urlopen(url)

            # json obj 
            data = json.load(json_obj)

            # for each coffee in the data 
            for coffee_dict in data:
                # skip irelivant data 
                if coffee_dict["title"] == "Banana2" or coffee_dict["title"] == "Iced Apple":
                    continue 
                
                #calculate the sugar level 
                sugar_level = get_coffee_based_on_sweetness(coffee_dict)
               
                if sweetness == "low" and sugar_level == 0:
                    add_coffee_to_csv(coffee_dict, header_list)
                if sweetness =="medium" and sugar_level == 1:
                    add_coffee_to_csv(coffee_dict, header_list)
                if sweetness == "high" and sugar_level >= 2 :
                    add_coffee_to_csv(coffee_dict, header_list)

                # reset sugar level for next coffee 
                sugar_level = 0
        
        # clear the text in recipe.txt file 
        recipe_file = open("recipe.txt", "w").close()
        # clear the text in the type.txt file 
        type_file = open("type.txt", "w").close()  
        # clear the text in the sweetness.txt file 
        sweetness_file = open("sweetness.txt", "w").close()

