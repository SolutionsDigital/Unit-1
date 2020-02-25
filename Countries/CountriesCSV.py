"""
Project V11     Name : Michael Mathews   Date :  23 /8 / 2020
Program Allows a user to maintain a list of Countries and capitals that
are stored in a File called countries.txt (using pickle)  so that latest
version of the data can be displayed, sorted, added, deleted etc.
option created to export to CSV using pandas and dataframes
Data Sourced and varified  @ http://data.un.org/ 2020
"""
# pickle function used to write and read binary to files
import pickle
import random
from pandas import DataFrame

legal = False

# default/backup list for myCountriesList
myCountriesList = ["demo"]
myCountriesList_backup = []


def export_to_file(myCountriesList):
    # update the lastest list copy to File countries.txt
    filename = "countries.txt"
    file = open(filename, 'wb')
    pickle.dump(myCountriesList, file)


def import_from_file(myCountriesList):
    # load lastest list copy from File countries.txt
    filename = "countries.txt"
    file = open(filename, 'rb')
    myCountriesList[:] = pickle.load(file)


def export_to_file_bu(myCountriesList_backup):
    # update the lastest list copy to File countries.txt
    filename = "countries_bu.txt"
    file = open(filename, 'wb')
    pickle.dump(myCountriesList_backup, file)


def exportTocsv(myCountriesList):
    # Exports the lastest list copy to CSV File => export_dataframe.csv
    if (len(myCountriesList)) >= 2:
        countries, capitals, populations = map(list, zip(*myCountriesList))

    countryData = {'CountryList': countries[:],
                   'CapitalList': capitals[:], 'PopulationList': populations[:]
                   }
    df = DataFrame(countryData, columns=[
                   'CountryList', 'CapitalList', 'PopulationList'])
    export_csv = df.to_csv(
        r'C:\Users\mmathews\OneDrive - All Saints Anglican School\Digital Solutions\Code\Unit-1\Countries\export_dataframe.csv', index=None, header=True)
    print(df)


def import_from_file_bu(myCountriesList):
    # load lastest list copy from File countries.txt
    filename = "countries_bu.txt"
    file = open(filename, 'rb')
    myCountriesList[:] = pickle.load(file)


def restore_file(myCountriesList):
    import_from_file_bu(myCountriesList)
    print("file restored")
    print()
    export_to_file(myCountriesList)


def capital_game(country, capital):

    while True:

        print()
        print("  Hiding \n")
        print("         The  \n")
        print("             List  \n")
        print("                 of  \n")
        print("                    Captials  \n")
        print()
        print()
        print()
        print("  To\n")
        print("      Truley\n ")
        print("             Test \n")
        print("                  Your  \n")
        print("                       Knowledge  \n")
        print("                                of \n")
        print("                                   Captials ")
        print()
        print()
        print("**************************************")
        print()
        print("  What is the capital of  ", country)
        print()
        print("**************************************")
        print()
        guess = input("  The capital is : ")
        if guess != capital:
            print("Sorry Incorrect  Nice Try,(check your spelling and case/Case)  ")
            print("The capital of ", country, "is ", capital)
            break
        elif guess == capital:
            print("You are Correct! Nice job. The capital of ",
                  country, "is ", capital)
            break


def report(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)
    #    print(len(myCountriesList)," Countries successfully loaded from file.",)
    print("*************" * 5)
    print('{:7}{:20s}{:<20s}{:>15}'.format(
        "No#", "Country", "Capital", "Population"))
    print("*************" * 5)
    if (len(myCountriesList)) > 0:
        for i in range(len(myCountriesList)):
            #        print(myCountriesList[i])
            print('{:<7}{:20s}{:<20s}{:>15,d}'.format(i + 1, myCountriesList[i][0], myCountriesList[i][1],
                                                      myCountriesList[i][2]))
    else:
        print("no Data")
        myCountriesList = [["", "", 0]]
        print(myCountriesList[0][2])


def clearList(myCountriesList, myCountriesList_backup):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    myCountriesList_backup = list(myCountriesList)
    export_to_file_bu(myCountriesList_backup)
    myCountriesList.clear()

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)

#    print(populations)


def showOptions():
    # show the users the list of Menu Options for selection
    print("***********************************************************************")
    print(" [A]  To Add a Country         - [B]  Insert Country byIndex")
    print(" [C]  Change Country by index  - [D]  Delete a Country byIndex")
    print(" [E]  Extend by Countries      - [R]  Remove a Country byName")
    print(" [S]  Sort Countries(A-z)      - [U]  Sort Countries(Z-a) ")
    print(" [T]  Sort Capitals (A-z)      - [V]  Sort Capitals (Z-a)")
    print(" [H]  Sort Population (H>l)    - [L]  RevSort Population (L<h)")
    print(" [W]  Clear data from file     - [Z]  Restore from Backup")
    print(" [G]  To Test your knowledge   - [X]  Export to CSV ")
    print()
    print("***************************  or  [Q]  to   Quit  ")


def addCountry(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    newCountry = input("What is the new Country name : ")
    newCaptital = input("What is the new Captial name : ")
    newPopulation = int(input("What is the new Population : "))
    myCountriesList.append([newCountry, newCaptital, newPopulation])

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def extendCountryList(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    newCountries = []
    extras = int(input("How many extra Countries : "))
    count = 1
    while count <= extras:
        print(count)
        Country = input("Extra Country : ")
        Capital = input("Extra Capital : ")
        Population = int(input("Extra Population : "))
        newCountries.append([Country, Capital, Population])
        count = count + 1

    myCountriesList.extend(newCountries)

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def addCountryindex(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)
    newindex = int(input("What is the new Country index Number : "))
    newCountry = input("What is the new Country name : ")
    newCaptital = input("What is the new Captial name : ")
    newPopulation = int(input("What is the new Population : "))
    myCountriesList.insert(
        newindex-1, [newCountry, newCaptital, newPopulation])

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def removeCountry(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    removeThisCountry = input("Type the Name of the Country to remove : ")
    A = myCountriesList
    a = next(i for i, x in enumerate(A) if removeThisCountry in x)
    print(myCountriesList[a], " has been removed")
    # myCountriesList.remove(removeThisCountry)
    myCountriesList.pop(a)
    print("Bye Bye ", removeThisCountry)

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def popCountry(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    popThisCountry = int(input("Type the Number of the Country to deleted : "))
    popThisCountry = popThisCountry - 1
    if popThisCountry < 0:
        print("Selected Number out of range")
    elif popThisCountry > len(myCountriesList):
        print("Selected Number out of range")
    else:
        print(popThisCountry + 1, '-',
              myCountriesList[popThisCountry], "has been Deleted")
        myCountriesList.pop(popThisCountry)

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def sortCountries(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Countries Sorted ( A - Z )  ")
    myCountriesList.sort(key=lambda x: x[0])

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def sortCapitals(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Capitals Sorted ( A - Z )  ")
    myCountriesList.sort(key=lambda x: x[1])

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def sortPopulation(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Capitals Sorted ( Population Highest - Lowest )  ")
    myCountriesList.sort(key=lambda x: x[2])
    myCountriesList[:] = reversed(myCountriesList)

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def reversePopulation(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Capitals Sorted ( Population Lowest - Highest )  ")
    myCountriesList.sort(key=lambda x: x[2])

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def reverseCountries(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Countries Reverse Sorted ( Z - A )  ")
    myCountriesList.sort(key=lambda x: x[0])
    myCountriesList[:] = reversed(myCountriesList)
    # load lastest adjusted list to File countriestxt
    export_to_file(myCountriesList)


def reverseCapitals(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    print(len(myCountriesList), " Capitals Reverse Sorted ( Z - A )  ")
    myCountriesList.sort(key=lambda x: x[1])
    myCountriesList[:] = reversed(myCountriesList)
    # load lastest adjusted list to File countriestxt
    export_to_file(myCountriesList)


def changeCountry(myCountriesList):
    # load lastest list copy from File countries.txt
    import_from_file(myCountriesList)

    updateindex = int(input("What is the number of country to be updated : "))
    Country = input("What is the updated country name : ")
    Capital = input("What is the Capital of the updated country : ")
    Population = int(input("What is the new Population : "))
    updateCountry = ([Country, Capital, Population])
    print()
    print("index -", updateindex, " ",
          myCountriesList[updateindex - 1], "has been updated to ", updateCountry)
    myCountriesList[updateindex - 1] = updateCountry

    # load lastest adjusted list to File countries.txt
    export_to_file(myCountriesList)


def loginform():
    username = input("Enter user name :")
    pwcount = 1
    while pwcount < 4:
        password = input("Enter your password :")
        if password != "p":
            print(pwcount, " Error")
            pwcount += 1

        elif password == "p":
            legal = True
            print("Access confirmed for", username,
                  " - Data sourced @ http://data.un.org/")
            break

    else:
        print("Your account is locked")
        legal = False


def farewell():
    print()
    print(" ---   Your Chose X - Exit  and then  Yes!  ---")
    print()
    print(" Aloha, Arrivederci, Sayōnara, Adios,  Chow !")
    print("Au Revoir, Auf Wiedersehen, Do svidaniya ,  Ola ")
    print(" --- See you next time ---")


def main():
    # initialise the userSelection Variable
    userSelection = "y"
    # security login check variable of Binary legal
    legal = False
    loginform()
    while userSelection != "X" or "x":
        import_from_file(myCountriesList)
        report(myCountriesList)
        if (len(myCountriesList)) >= 2:
            countries, capitals, populations = map(list, zip(*myCountriesList))
            question = random.randint(1, len(myCountriesList)-1)
            country = myCountriesList[question][0]
            capital = myCountriesList[question][1]
# print("My List of Lists")
# print(myCountriesList)
# print()
# print("Countries ONLY")
# print(countries)
# print()
# print("Capitals ONLY")
# print(capitals)
# print()
# print("Populations ONLY")
# print(populations)

        showOptions()
        userSelection = input(
            "CheckData @ http://data.un.org/    Select your OPTION : ")
        if userSelection in ("A", "a"):
            addCountry(myCountriesList)
        if userSelection in ("B", "b"):
            addCountryindex(myCountriesList)
        elif userSelection in ("D", "d"):
            popCountry(myCountriesList)
        elif userSelection in ("E", "e"):
            extendCountryList(myCountriesList)
        elif userSelection in ("R", "r"):
            removeCountry(myCountriesList)
        elif userSelection in ("C", "c"):
            changeCountry(myCountriesList)
        elif userSelection in ("U", "u"):
            reverseCountries(myCountriesList)
        elif userSelection in ("V", "v"):
            reverseCapitals(myCountriesList)
        elif userSelection in ("S", "s"):
            sortCountries(myCountriesList)
        elif userSelection in ("T", "t"):
            sortCapitals(myCountriesList)
        elif userSelection in ("L", "l"):
            reversePopulation(myCountriesList)
        elif userSelection in ("H", "h"):
            sortPopulation(myCountriesList)
        elif userSelection in ("G", "g"):
            capital_game(country, capital)
        elif userSelection in ("W", "w"):
            clearList(myCountriesList, myCountriesList_backup)
        elif userSelection in ("X", "x"):
            exportTocsv(myCountriesList)
        elif userSelection in ("Z", "z"):
            import_from_file_bu(myCountriesList)

        elif userSelection in ("Q", "q"):
            AreYouSure = input("Are You sure you want to quit  Y or N : ")
            if AreYouSure in ("Y", "y"):
                farewell()
                break
            else:
                print("Welcome back for more Country information")

        else:
            print("wrong option ,  Please try again")


if __name__ == "__main__":
    main()
