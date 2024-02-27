#
# header comment!
#
import sqlite3
import objecttier
##################################################################  
def print_stats(dbConn):
    print("General Statistics:")
    print("  Number of Lobbyists:", objecttier.num_lobbyists(dbConn))
    print("  Number of Employers:", objecttier.num_employers(dbConn))
    print("  Number of Clients:", objecttier.num_clients(dbConn))


##################################################################  
#
# main
#
dbConn = sqlite3.connect("Chicago_Lobbyists.db")
print('** Welcome to the Chicago Lobbyist Database Application **')

while True:
    commandInput = input("Please enter a command (1-5, x to exit): ")
    if commandInput.lower() == 'x':
        exit(0)
    elif commandInput == '0':
        print_stats(dbConn)
    elif commandInput == '1':
        name = input("Enter lobbyist name (first or last, wildcards _ and % supported): ")
        objecttier.get_lobbyists(dbConn, name)
    elif commandInput == '2':
        id = input("Enter Lobbyist ID: ")
        objecttier.get_lobbyist_details(dbConn, id)
    elif commandInput == '3':
        number_N = input("Enter the value of N: ")
        year = input("Enter the year: ")
        objecttier.get_top_N_lobbyists(dbConn, number_N, year)
    elif commandInput == '4':
        yearInput = input("Enter year: ")
        idInput = input("Enter the lobbyist ID: ")
        objecttier.add_lobbyist_year(dbConn, idInput, yearInput)
    elif commandInput == '5':
        pass
    else:
        print("**Error, unknown command, try again...")

#
# done
#
