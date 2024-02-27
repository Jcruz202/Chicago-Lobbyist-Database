#
# objecttier
#
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
#
# Original author: Ellen Kidane
#
import datatier


##################################################################
#
# Lobbyist:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#
class Lobbyist:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
      self._Lobbyist_ID = Lobbyist_ID
      self._First_Name = First_Name
      self._Last_Name = Last_Name
      self._Phone = Phone

   @property
   def Lobbyist_ID(self):
      return self._Lobbyist_ID
   @property
   def First_Name(self):
      return self._First_Name
   @property
   def Last_Name(self):
      return self._Last_Name
   @property
   def Phone(self):
      return self._Phone

##################################################################
#
# LobbyistDetails:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
#
class LobbyistDetails:
    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, City,
                 State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
        self._Lobbyist_ID = Lobbyist_ID
        self._Salutation = Salutation
        self._First_Name = First_Name
        self._Middle_Initial = Middle_Initial
        self._Last_Name = Last_Name
        self._Suffix = Suffix
        self._Address_1 = Address_1
        self._Address_2 = Address_2
        self._City = City
        self._State_Initial = State_Initial
        self._Zip_Code = Zip_Code
        self._Country = Country
        self._Email = Email
        self._Phone = Phone
        self._Fax = Fax
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = Total_Compensation

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID
    @property
    def Salutation(self):
        return self._Salutation
    @property
    def First_Name(self):
        return self._First_Name
    @property
    def Middle_Initial(self):
        return self._Middle_Initial
    @property
    def Last_Name(self):
        return self._Last_Name
    @property
    def Suffix(self):
        return self._Suffix
    @property
    def Address_1(self):
        return self._Address_1
    @property
    def Address_2(self):
        return self._Address_2
    @property
    def City(self):
        return self._City
    @property
    def State_Initial(self):
        return self._State_Initial
    @property
    def Zip_Code(self):
        return self._Zip_Code
    @property
    def Country(self):
        return self._Country
    @property
    def Email(self):
        return self._Email
    @property
    def Phone(self):
        return self._Phone
    @property
    def Fax(self):
        return self._Fax
    @property
    def Years_Registered(self):
        return self._Years_Registered
    @property
    def Employers(self):
        return self._Employers
    @property
    def Total_Compensation(self):
        return self._Total_Compensation

##################################################################
#
# LobbyistClients:
#
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
#
class LobbyistClients:
   def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
       self._Lobbyist_ID = Lobbyist_ID
       self._First_Name = First_Name
       self._Last_Name = Last_Name
       self._Phone = Phone
       self._Total_Compensation = Total_Compensation
       self._Clients = Clients
       
   @property
   def Lobbyist_ID(self):
       return self._Lobbyist_ID
   @property
   def First_Name(self):
       return self._First_Name
   @property
   def Last_Name(self):
       return self._Last_Name
   @property
   def Phone(self):
       return self._Phone
   @property
   def Total_Compensation(self):
       return self._Total_Compensation
   @property
   def Clients(self):
       return self._Clients

##################################################################
# 
# num_lobbyists:
#
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
#
def num_lobbyists(dbConn):
    num_lobbyists_sql = """
                        SELECT COUNT(Lobbyist_ID)
                        FROM LobbyistInfo
                       """
    try:
        result = datatier.select_n_rows(dbConn, num_lobbyists_sql)
        if result is None:
            return []
        num_lobbyists_count = result[0][0]
        # print(num_lobbyists_count)
        return num_lobbyists_count
    except Exception as err:
        print("num_lobbyists", err)
        return -1

##################################################################
# 
# num_employers:
#
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
#
def num_employers(dbConn):
    num_employer_sql = """
                        SELECT COUNT(Employer_ID)
                        FROM EmployerInfo
                       """
    try:
        result = datatier.select_n_rows(dbConn, num_employer_sql)
        if result is None:
            return []
        num_employer_count = result[0][0]
        # print(num_employer_count)
        return num_employer_count
    except Exception as err:
        print("num_employers", err)
        return -1

##################################################################
# 
# num_clients:
#
# Returns: number of clients in the database
#           If an error occurs, the function returns -1
#
def num_clients(dbConn):
    num_client_sql = """
                        SELECT COUNT(Client_ID)
                        FROM ClientInfo
                       """
    try:
        result = datatier.select_n_rows(dbConn, num_client_sql)
        if result is None:
            return []
        num_client_count = result[0][0]
        return num_client_count
    except Exception as err:
        print("num_client", err)
        return -1

##################################################################
#
# get_lobbyists:
#
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
#
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
#
def get_lobbyists(dbConn, pattern):
    lobbyist_list_sql = """
                        SELECT Lobbyist_ID, First_Name, Last_Name, Phone
                        FROM LobbyistInfo
                        WHERE First_Name LIKE ? OR Last_Name LIKE ?
                        ORDER BY Lobbyist_ID ASC
                        """
    try:
        result = datatier.select_n_rows(dbConn, lobbyist_list_sql, (pattern, pattern))
        list = []
        for row in result:
            lobbyist_id, first_name, last_name, phone = row
            temp = Lobbyist(lobbyist_id, first_name, last_name, phone)
            list.append(temp)
        return list
    except Exception as err:
        print("get_lobbyists", err)
        return -1

##################################################################
#
# get_lobbyist_details:
#
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
#
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
#
def get_lobbyist_details(dbConn, lobbyist_id):
    lobbyist_details_sql = """
                            SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.Salutation, LobbyistInfo.First_Name, LobbyistInfo.Middle_Initial, LobbyistInfo.Last_Name, 
                                LobbyistInfo.Suffix, LobbyistInfo.Address_1, LobbyistInfo.Address_2, LobbyistInfo.City, LobbyistInfo.State_Initial, LobbyistInfo.ZipCode, LobbyistInfo.Country, 
                                LobbyistInfo.Email, LobbyistInfo.Phone, LobbyistInfo.Fax, GROUP_CONCAT(DISTINCT LobbyistYears.Year) AS Years
                            FROM LobbyistInfo
                            LEFT JOIN LobbyistYears ON LobbyistInfo.Lobbyist_ID = LobbyistYears.Lobbyist_ID
                            LEFT JOIN LobbyistAndEmployer ON LobbyistYears.Lobbyist_ID = LobbyistAndEmployer.Lobbyist_ID
                            WHERE LobbyistInfo.Lobbyist_ID = ?
                            """
    employer_sql = """
                     SELECT DISTINCT EmployerInfo.Employer_Name
                     FROM LobbyistAndEmployer
                     JOIN EmployerInfo ON LobbyistAndEmployer.Employer_ID = EmployerInfo.Employer_ID
                     WHERE LobbyistAndEmployer.Lobbyist_ID = ?
                     ORDER BY EmployerInfo.Employer_Name ASC
                    """
    
    compensation_sql = """
                         SELECT SUM(Compensation_Amount)
                         FROM Compensation
                         WHERE Lobbyist_ID = ?
                        """
    try:
        result = datatier.select_one_row(dbConn, lobbyist_details_sql, (lobbyist_id,))
        employer_result = datatier.select_n_rows(dbConn, employer_sql, (lobbyist_id,))
        compensation_result = datatier.select_one_row(dbConn, compensation_sql, (lobbyist_id,))
        total_compensation = compensation_result[0]
        if result[0] == None:
            return None
        if total_compensation == None:
            total_compensation = 0
        employer_list = [employer[0] for employer in employer_result] if employer_result else []
        lobbyist_ID, salutation, first_name, middle_initial, last_name, suffix, address_1, address_2, city, state_initial, zipCode, country, email, phone, fax, years_registered_str = result
        years = years_registered_str.split(",")
        lobbyist_details = LobbyistDetails(lobbyist_ID, salutation, first_name, middle_initial, last_name, suffix, address_1, address_2, city, state_initial, zipCode, country, email, phone, fax, years, employer_list, total_compensation)
        return lobbyist_details
    except Exception as err:
        print("get_lobbyists_details", err)
        return None


##################################################################
#
# get_top_N_lobbyists:
#
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
#
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
#
def get_top_N_lobbyists(dbConn, N, year):
    top_lobbyist_sql = """
                        SELECT LobbyistInfo.Lobbyist_ID, LobbyistInfo.First_Name, LobbyistInfo.Last_Name, LobbyistInfo.Phone, Compensation_Amount, Client_Name
                        FROM LobbyistInfo
                        JOIN LobbyistYears ON LobbyistInfo.Lobbyist_ID = LobbyistYears.Lobbyist_ID
                        JOIN Compensation ON LobbyistYears.Lobbyist_ID = Compensation.Lobbyist_ID
                        JOIN ClientInfo ON Compensation.Client_ID = ClientInfo.Client_ID
                        WHERE LobbyistYears.Year = ?
                        """
    try:
        result = datatier.select_n_rows(dbConn, top_lobbyist_sql, (year,))
        # if year > 2021:
        #     return None
        # for i in range(N):
        list_lobbyist = []
        for row in result:
            lobbyist_ID, first_name, last_name, phone, total_compensation, clients = row
            temp = LobbyistClients(lobbyist_ID, first_name, last_name, phone, total_compensation, clients)
            list_lobbyist.append(temp)

        # print(row)
        return list_lobbyist
            
        # print(row)

    except Exception as err:
        print("get_lobbyist_details", err)
        return None


##################################################################
#
# add_lobbyist_year:
#
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
#
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def add_lobbyist_year(dbConn, lobbyist_id, year):
    lobbyist_sql = """
                    SELECT COUNT(*) 
                    FROM LobbyistInfo 
                    WHERE Lobbyist_ID = ?
                    """
    try:
        lobbyist_result = datatier.select_one_row(dbConn, lobbyist_sql, (lobbyist_id,))
        lobbyist_exists = lobbyist_result[0] if lobbyist_result else None

        if(lobbyist_exists):
            insert_sql = """
                        INSERT INTO LobbyistYears(Lobbyist_ID, Year) 
                        VALUES(?, ?) 
                        """
            parameters = [lobbyist_id, year]
            datatier.perform_action(dbConn, insert_sql, parameters)
            return 1
        return 0
    except Exception as err:
        print("add_lobbyist_year", err)
        return 0


##################################################################
#
# set_salutation:
#
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
#
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
#
def set_salutation(dbConn, lobbyist_id, salutation):
    lobbyist_sql = """
                    SELECT COUNT(*) 
                    FROM LobbyistInfo 
                    WHERE Lobbyist_ID = ?
                    """
    try:
        lobbyist_result = datatier.select_one_row(dbConn, lobbyist_sql, (lobbyist_id,))
        lobbyist_exists = lobbyist_result[0] if lobbyist_result else None

        if(lobbyist_exists):
            salutation_sql = """
                                UPDATE LobbyistInfo 
                                SET Salutation = ? 
                                WHERE Lobbyist_ID = ?
                            """
            parameters = [salutation, lobbyist_id]
            datatier.perform_action(dbConn, salutation_sql, parameters)
            return 1
        return 0
    except Exception as err:
        print("set_salutation", err)
        return 0