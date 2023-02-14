# coffee_microservice-
A micro service created using Python that requests data from an API that stores coffee recipes, communicates via text files, and sends info via CSV file. 

1. How to REQUEST data from the microservice 

To request data, you need to first input the sweetness level of the coffee in the sweetness.txt file, 'low' 'medium' OR 'high'. Input the temperature of the coffee, 'hot' OR 'iced' in the type.txt file. Then, to request the data according to these preferences, type 'run' on the recipes.txt file. 

Example call

sweetness_level = input("Enter prefered sweetness level(low, medium, high)") -> f = open("sweetness.txt, "w") -> f.write(sweetness_level) 
type_inputted   = input("Enter prefered type (hot/iced)")                    -> f = open("type.txt, "w") -> f.write(type_inputted) 
                                                                             -> f = open("recipes.txt, "w") -> f.write("run")
                                                        
2. How to RECIEVE data 

To receive data, open and read the output.csv file that is created after data is requested from the microservice. 


![UMG](https://user-images.githubusercontent.com/91393581/218639608-de029ecb-6bab-4a17-bfb8-ed3dfffffad4.png)
