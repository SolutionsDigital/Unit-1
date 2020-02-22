"""
Dictionary Creation and Management
Name : Michael Mathews   Date :  23 /10 / 19
Program Allows a user to maintain a Dictionary
"""
import csv
import os
# initial Data File for Dict
my_dict={'id':'001','Name':'Bob', 'Surname':'Brown', 'age':32}
# declare new_dict as an empty  or Blank Dictionary
new_dict={}
list_dict_data =[]

def WriteDictToCSV(csv_file,csv_columns,list_dict_data): 
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list_dict_data:
                writer.writerow(data)
    except:
        print("Error did not write to file")    

def showOptions():
    # show the users the list of Menu Options for selection
    print("***************************************************************" )
    print(" Press[K]  To Add a Key and Value ")
    print(" Press[A]  To Add a Record (Whole Row) ")
    print(" Press[D]  To Delete a Record (Whole Row) ")
    print(" Press[R]  Report current Dictionary (Key=Value) ")
    print(" Press[X]  to EXIT ")
    print("****************************************************************" )

def new_Dict_KeyValue(csv_file, csv_columns,list_dict_data):
    newKey = input(" What Key would you like to add : Key = ")
    print("---" * 10)
    print(" Is the Value for the new key of ",newKey," - [T]ext or [I]nteger")
    print("---" * 10)
    print("  Text   - PRESS T")
    print(" Integer - PRESS I")
    print("---" * 10)
    
    value_type = input(" Press T for [T]ext or I for [I]nteger : ")
    if value_type in ["T","t"]: 
        newValue= input(" What Text Value would you like to add : ")
    elif value_type in ["I","i"]: 
        newValue= int(input(" What Integer Value would you like to add : "))
    my_dict[newKey]=newValue
    print()
    list_dict_data.append(my_dict)
    WriteDictToCSV(csv_file, csv_columns, list_dict_data)



def addrecord(keysListed,list_dict_data,csv_columns,csv_file):
    print()
    newRecord={}
    for key in keysListed:
        print(key)
        newValue=input("what is the value ")
        newRecord[key]=newValue
        newRecord.update({key:newValue})
    print(" new Record ", newRecord)
    print("Done ! - END of Add Data - Note: dict to CSV info has been sent to File")
    list_dict_data.append(newRecord)
    WriteDictToCSV(csv_file,csv_columns,list_dict_data)


def removeRecord(list_dict_data,csv_columns,csv_file):
    # load lastest list copy from File Names.csv
    if (len(list_dict_data))>0:
        for i in range(len(list_dict_data)):
            print("DataSet",i+1, list_dict_data[i])  
    
    removeThisRecord = int(input("Enter the Number for DataSet to be deleated : "))
    print ("Record data for number ",removeThisRecord, " has been deleted")
    list_dict_data.pop(removeThisRecord-1)
    print("-------------------------------------------------")
    print("")
    if (len(list_dict_data))>0:
        for i in range(len(list_dict_data)):
            print("DataSet",i+1, list_dict_data[i]) 
    print("-------------------------------------------------")
    print("")
    WriteDictToCSV(csv_file,csv_columns,list_dict_data)

def report():
    print()
    for key in my_dict.keys():
        value = my_dict[key]
        print(key, "=" , value)
    print()
 
    
def main():
    # initialise the userSelection Variable 
    userSelection = "y"
    csv_file ="Names.csv"
    
    while userSelection != "X" or "x":
        print("-------" *10)

        keysListed = list(my_dict.keys())
        csv_columns=keysListed
        print(" Keys ", csv_columns)

        datalisted = list(my_dict.values())
        print(" Values ", datalisted)

        data=dict(zip(keysListed,datalisted))
        print(" dataFile ", data)
        print("-------" *10)

        if (len(list_dict_data))>0:
            for i in range(len(list_dict_data)):
                print("DataSet",i+1, list_dict_data[i])  
            
        showOptions()
 
        print()
        userSelection = input("Select your OPTION : ")
        if userSelection in ("K", "k"):
            new_Dict_KeyValue(csv_file, csv_columns,list_dict_data)
        elif userSelection in ("A", "a"):
            addrecord(keysListed,list_dict_data,csv_columns,csv_file)
        elif userSelection in ("R", "r"):
            report()
        elif userSelection in ("D", "d"):
            removeRecord(list_dict_data,csv_columns,csv_file) 
        elif userSelection in ("X", "x"):
            AreYouSure=input("Are You sure you want to quit  Y or N : ")
            if AreYouSure in ("Y", "y"):
                farewell()
                break
            else:
                print("Welcome back")                               
        else:
            print("wrong option ,  Please try again")
    WriteDictToCSV(csv_file,csv_columns,list_dict_data)
    
def farewell():
    print()
    print(" ---   Your Chose X - Exit  and then  Yes!  ---")
    print()
    print(" Aloha, Arrivederci, Sayōnara, Adios,  Chow !")
    print("Au Revoir, Auf Wiedersehen, Do svidaniya ,  Ola ")
    print(" --- See you next time ---")            

if __name__ == "__main__":
    main()
