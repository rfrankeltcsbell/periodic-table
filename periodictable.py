import csv 
import os
#import allows us to access a pre written module of code.
#simliar to checking out a book in a library 
#csv stands for comma separated values. It's a file extension that has rows and columns like a excel spreadsheet
# Function to create the structure of the csv files if they don't exist
def create_csv_files():
  #Check if periodic_table_.csv exist, if not create it
  if not os.path exist('periodic_table.csv'):
    with open ('periodic_table.csv','w',newline='')as file:
      writer= csv.DicWriter(file,fieldnames=['Symbol','Name','Atomic Number','Atomic Weight'])
      writer.writerheader()
      #Optinonally add some default elements
      writer.writerow({'Symbol':'H','Name':'Hydrogen','Atomic Number'1,'Atomic Weight':1.008})
      Writer.writerow({'Symbol':'O','Name':'Oxygen','Atomic Number'8,'Atomic Weight':15.999})
      Writer.wrtierow({'Symbol':'C','Name':'Carbon','Atomic Number':6,'Atomic Weight':12.011})
      
      print("Created Periodic_table.csv")
      
      # a file path is location on your computer
      # writer allows us to write into our file
  if not os.path.exists('compounds.csv'):
    with open('compound.csv','w',newline=')as file:
      writer = csv.DictWriter(file,fieldnames=['Compound Name','Base Elements','Proportions'])
      writer.writerhead()
      # Opionally add a default compound
      writer.writerow(['Compound Name':,'Water','Base Elements':'H20','Proportions':'2 H,1 0'})
      
      print ("Createrd compounds,csv")
      
      # Load periodic table from CSV
def load_elements(file_name):
    elements= {}
    with open(file_name,'r')as file:
        reader = csv.DictReader(file)
        for row in reader:
            elements[row['Symbol']]={
              'name':row['Name'],
              'atomic_number': int(row['Atomic Number']),
              'atomic_weight': float(row['Atomic Weight'])
            }
    return elements
            
def load_compounds(file_name):
        compounds ={}
        with open (file_name,'r')as file:
            reader = csv.Dictreader(file) 
            for row in reader: 
                compounds.append({
                'name':row['Compound Name'],
                'elements':row['Base Elements'],
                'proportion':row['Proportions']
                })
        return compounds
                
            
    
        #View periodic table
def view_periodic_table(elements):
    for symbol,details in elements.items():
    print(f"{symbol}: {details['name']}(Atomic Number):{details['atomic_number']},Atomic Weight:{details['atomic_weight']})    ")

# Save new compound to CSV
def save_compound(compound,file_name):
    with open(file_name,'a',newline='')as file:
        writer = csv.DictWriter(file, fieldnames=['Compound Name','Base Elements','Proportions'])
        writer.wrtierow(compound)

    # Menu System
def menu(elements,compounds_file):
    while True:
        print("\nMenu")
        print("1. View Periodic Table")
        print("2. View Compounds")
        print("3. Create New Compound")
        print("4. Break Down Compound")
        print("5. Exit")

        choice = input("Choose an option")
        if choice =='1':
            view_periodic_table(elements)
        elif choice == '2':
            compounds = load_compounds(compounds_file)
            for compound in compounds:
                print (f"{compound['name']} is made of {compound['elements']} in proportions {compound['proportions']}")