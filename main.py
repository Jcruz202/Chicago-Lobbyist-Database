#
# Juan Cruz
# CS 341 Project 2 Part 3 – Chicago Lobbyist Database App
# The goal of this project is to write a console-based database application in Python, this
# time using an N-tier design. The database used for this project consists of information
# pertaining to registered lobbyists in Chicago, their employers, their clients, and their compensation.
#
import sqlite3
import objecttier
##################################################################  
def print_stats(dbConn):
    print("\nGeneral Statistics:")
    # prints the total number of Lobbyist
    print("  Number of Lobbyists: {:,}".format(objecttier.num_lobbyists(dbConn)))

    # prints the total number of employers
    print("  Number of Employers: {:,}".format(objecttier.num_employers(dbConn)))

    # prints the total number of clients
    print("  Number of Clients: {:,}".format(objecttier.num_clients(dbConn)))
##################################################################  
    # This method is for command 1, Given the user input of a name, find and output basic information for all lobbyists that match that name.
def command1(dbConn, name):
    lobbyists = objecttier.get_lobbyists(dbConn, name) #this line returns the object lobbyist
    print("\nNumber of lobbyists found:", len(lobbyists)) 
    if len(lobbyists) > 100: #checks if the number of lobbyist is too much to display
        print("\nThere are too many lobbyists to display, please narrow your search and try again...")
        return
    for lobbyist in lobbyists: #this for loop allows access to the lobbyist object
        print(lobbyist.Lobbyist_ID, ':', lobbyist.First_Name, lobbyist.Last_Name, "Phone:", lobbyist.Phone) #prints the lobbyist information
##################################################################  
    #This method handles command 2, Given a lobbyist ID, find and output detailed information about the lobbyist.
def command2(dbConn, id):
    lobbyists = objecttier.get_lobbyist_details(dbConn, id) #This code returns a LobbyistDetails object
    if lobbyists is None: #checks if the id doesn't exist
        print("\nNo lobbyist with that ID was found.")
    else: #This else statement is if the lobbyist_id exist, it prints the Lobbyist details information
        print("\n", lobbyists.Lobbyist_ID, ' :', sep='')
        print("  Full Name:", lobbyists.Salutation, lobbyists.First_Name, lobbyists.Middle_Initial, lobbyists.Last_Name, lobbyists.Suffix) #prints the full name
        print("  Address:", lobbyists.Address_1, lobbyists.Address_2, ',', lobbyists.City, ',', lobbyists.State_Initial, lobbyists.Zip_Code, lobbyists.Country) #prints the full address
        print("  Email:", lobbyists.Email) #prints email
        print("  Phone:", lobbyists.Phone) #prints phone number
        print("  Fax:", lobbyists.Fax) #prints the fax if it exist
        years_registered = ", ".join(str(year) for year in lobbyists.Years_Registered) #makes sure all the years gets printed becuase it's a list
        print("  Years Registered:", years_registered + ", ") #prints all the years
        employers_list = ", ".join(lobbyists.Employers) #makes sure all the employers gets printed becuase it's a list
        print("  Employers:", employers_list + ", ") #prints all the employers
        total_compensation = "${:,.2f}".format(lobbyists.Total_Compensation) #this formats the total_compensation to the desired output
        print("  Total Compensation:", total_compensation) #prints the total compensation
##################################################################
    #This method handles command 3, Given a year, output the top N lobbyists based on their total compensation for that year
def command3(dbConn, number_N, year):
    lobbyists = objecttier.get_top_N_lobbyists(dbConn, number_N, year) #this returns a list of a LobbyistClients object based off N
    num = 1 #a counter for the number of N
    print('\n')
    for row in lobbyists: #This for loop allows access to the object
        print(num, '.', row.First_Name, row.Last_Name) #prints the full name
        print("  Phone:", row.Phone) #prints the phone #
        total_compensation = "${:,.2f}".format(row.Total_Compensation) #this formats the total_compensation to the desired output
        print("  Total Compensation:", total_compensation)
        clients_list = ", ".join(row.Clients) #this allows to be able to print all the clients in the client list
        print("  Clients:", clients_list + ", ")
        num += 1 #increments the num
##################################################################
    #This method handles command 4, Register an existing lobbyist for a new year.
def command4(dbConn, idInput, yearInput):
    lobbyist = objecttier.add_lobbyist_year(dbConn, idInput, yearInput) #This code attempts to add the lobbyist year if the ID exist
    if lobbyist == 1: #checks if the ID exist to add the year
        print("\nLobbyist successfully registered.")
    else: #this else statement is if the ID doesnt exist or if the year alread exist
        print("\nNo lobbyist with that ID was found.")
##################################################################
    #This method is for command 5, Set the salutation for a given lobbyist.
def command5(dbConn, idInput, salutation_Input):
    lobbyist = objecttier.set_salutation(dbConn, idInput, salutation_Input) #This code attempts to set the salutation if the ID exist
    if lobbyist == 1: #checks if the ID exist
        print("\nSalutation successfully set.")
    else: #this gets executed if the ID doesn't exist
        print("\nNo lobbyist with that ID was found.")
##################################################################
#
# main
#
dbConn = sqlite3.connect("Chicago_Lobbyists.db") #this code connects to the database
print('** Welcome to the Chicago Lobbyist Database Application **')
print_stats(dbConn) #This calls the function to print the statistic of the database

while True: # a never ending while loop unless the user wants to exit
    commandInput = input("\nPlease enter a command (1-5, x to exit): ") #This code asks the user for the command input
    if commandInput.lower() == 'x': #This checks if the input is x and makes sure it's a lower x so if the user input X it'll still work
        exit(0) #exits the program
    elif commandInput == '1':
        name = input("\nEnter lobbyist name (first or last, wildcards _ and % supported): ") #this code asks for a name input
        command1(dbConn, name) #calls the method command1 if the commandInput is 1
    elif commandInput == '2':
        id = input("\nEnter Lobbyist ID: ")
        command2(dbConn, id) #calls the method command1 if the commandInput is 2
    elif commandInput == '3':
        number_N = input("\nEnter the value of N: ") #This asks for a a N input
        number_N = int(number_N) #This is to make sure the input N is an integer
        if number_N < 0: #Checks if the input N is a negative number
            print("Please enter a positive value for N...")
            continue
        year = input("Enter the year: ") #this asks for a year input
        command3(dbConn, number_N, year) #calls the method command1 if the commandInput is 3
    elif commandInput == '4':
        yearInput = input("\nEnter year: ") #this asks for a year input
        idInput = input("Enter the lobbyist ID: ")  #this line asks for the id input
        command4(dbConn, idInput, yearInput) #calls the method command1 if the commandInput is 4
    elif commandInput == '5':
        idInput = input("\nEnter the lobbyist ID: ") #this line asks for the id input
        salutation_Input = input("Enter the salutation: ") #this line asks for the salutation input
        command5(dbConn, idInput, salutation_Input) #calls the method command1 if the commandInput is 5
    else: #This else gets executed if the user input a command other than 1-5 or x
        print("**Error, unknown command, try again...") 
#
# done
#