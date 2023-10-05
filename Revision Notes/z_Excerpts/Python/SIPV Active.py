import datetime #This module is used to manage date operations
import time #This module is used to give slight time to delays to outputted texts to make it more userfriendly


def formatSplit(choice, repeat = 40): #Breaks up large blocks of code to add a more user friendly experience
    if choice == 1:
        print("=-" * repeat + "=")


def fileM(fName, Read_Write = "r", Input_Output = "[]"): #Compact function to read/ write a variable to a file
    f = open(fName, Read_Write) #Opens the file
    if Read_Write  == "w":
        f.write(str(Input_Output)) #Writes the new data input onto the file
    if Read_Write == "r":
        return eval(f.read()) #Reads the data from the file and returns it


def fileO(fName, Input_Output = "{}"): #Compact function to check whether data files are already existing, if not creating one with default data {}
    try:
        return fileM(fName) #Attempts reading from file
    except:
        fileM(fName, "w", str(Input_Output)) #If that fails, it creates a nwe file with some default data inside
        return fileM(fName) #Reads in file


def logU(set_range, newLog = False): #Function to manage logins, reading login data in from files, returning true if authentication check is a success, with a limit number of attempts defined when the function is called
    logIns = fileO("Passwords.txt", {"Username" : "Password"}) #Reads in password data
    if newLog == True: #Adds a new username and password
        usrNme = input("Enter New Username : ")
        logIns[usrNme] = input("Enter New Password : ")
        fileM("passwords.txt", "w", logIns)
    else:
        for i in range(0, set_range): #Allows for a set range of attempts
            logIns = fileO("Passwords.txt", {"Username" : "Password"})
            username = input("\nEnter Username : ")
            password = input("Enter Password : ")
            try:
                if logIns[username] == password: #Uses username as key and tests if password matches it#s value
                    print("\nLogin Successful\n")
                    return True #Returns true on success
            except:
                pass
            print("ERROR: Incorrect login credentials") #If the username (key) or value (Password) are wrong, the error message appears
        print("ERROR: Session has timed out")
        time.sleep(1.2) #Pauses the program so that user has time to read the error, before allowing the next function (killing program) to run
        exit() #Kills program if attempt range is exceeded


def interp(data_type): #Converts datatype into a more userfriendly name
    if data_type == str:
        return "letters"
    elif data_type == int:
        return "a whole number"
    else:
        return "@#??_1!"


def Valid(output, typeI, max_Value = 100, min_Value = 0, entry_text = ">>> ", typeS = False, typeSLEN = False): #Compact validation function that can be used on all data sets with really versatile uses
    typeStr = interp(typeS)#This Calls the interp function, which converts python terminology like 'int' and 'str' into words that the user is more accostumed to, like 'numbers' and 'letters'
    typeIstr = interp(typeI)
    print("\n" + output)
    x = input(str(entry_text)) #Input from user
    
    if str(x) == "":
        print("ERROR: Enter data")
        x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN) #Checks if input is empty, it calls the function again if the check is failed
    try:
        x = typeI(x)
    except:
        print("ERROR: Enter " + typeIstr)
        x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN) #Checks if input fits the primary data type, it calls the function again if the check is failed
    
        #Next two if statements check whether the input is within range, using the functions that corresspond to their datatype, it calls the function again if the check is failed
    if typeI == int:
        if int(x) > int(max_Value) or int(x) < int(min_Value):
            print("ERROR: Remain within the range " + str(min_Value) + " to " + str(max_Value))
            x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN)
    if typeI == str:
        if len(str(x)) > max_Value or len(str(x)) < min_Value:
            print("ERROR: Input Must Be Within " + str(min_Value) + " and " + str(max_Value) + " Characters Long")
            x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN)
    if typeS != False:
        try:
            E = typeS(x)
            if typeSLEN != False:
                if typeS == int:
                    if int(x) > int(max_Value) or int(x) < int(min_Value):
                        print("ERROR: Remain within the range " + str(min_Value) + " to " + str(max_Value))
                        x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN)
                if typeS == str:
                    if len(str(x)) != typeSLEN:
                        print("ERROR: Input Must" + str(typeSLEN) + " Characters Long")
                        x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN)
        except:
            print("ERROR: Enter a " + str(typeStr))
            x = Valid(output, typeI, max_Value, min_Value, entry_text, typeS, typeSLEN) #Checks if input fits the secondary data type, it calls the function again if the check is failed
    return typeI(x) #Returns the input if all checks are succesful


def menU(User_Options, Menu_Title): #Extremely compact Menu setup with integrated validation, returning the choice of the user
    Output_String = str("   " * 4 + Menu_Title) + "\n"
    for i in range(0, len(User_Options)):
        Output_String += "Enter " + str(i + 1) + " to " + str(User_Options[i]) + "\n"
    return int(Valid(Output_String, int, len(User_Options), 1)) #The user output and backend logic is extremely easy to understand, personally I'm impressed xD


def Check(text): #Tests to ensure that input is either Y or N
    print("\n" + text)
    x = input("Y or N : ")
    
    if str(x) == "":
        print("ERROR: Enter data")
        x = Check(text)
        
    elif x.lower() != "y" and x.lower() != "n":
        print("ERROR: Enter Either Y or N")
        x = Check(text)#Checks if input is either y or n, it calls the function again if the check is failed
        
    return x
        

def dateB(string_printed):
    yearU = Valid("Enter Year that " + string_printed, int, int(datetime.datetime.now().strftime("%Y")), 1900, ">>>", str, 4) #Ensure the Date entered is within accepted ranges
    monthU = Valid("Enter Month that " + string_printed, int, 12, 1)
    dayU = Valid("Enter Day that " + string_printed, int, 31, 1)
    
    try:
        startData = datetime.datetime(yearU, monthU, dayU) #Attempts to use the inputed data to set a date using datetime
        endData = datetime.datetime(yearU + 1, monthU, dayU)
    except:
        print("ERROR: Enter A Valid Date") #If the date is invalid, the check fails and the function is called again
        return dateB(string_printed)
    
    return[startData, endData] # Returns the start and end date as a list


#Basic Data Structure labels for customerData and firmData
customerDataKey = ["Name", "SIP Card Number", "Date of Issue", "Date of Expiry"]
firmDataKey = ["Shop Name", "Discount Day", "Free Delivery", "2 for 1 offer, for"]

if logU(3) == True: #If Login function passed succesfully
    customerData = eval(str(fileO("customerData.txt"))) #reads in customerData
    firmData = eval(str(fileO("firmData.txt"))) #reads in firmData
    while True:
        customerData = eval(str(fileO("customerData.txt")))
        formatSplit(1)
        choice = menU(["View the SIP Card SubMenu", "View the Buisness SubMenu", "View the Benefit Claim SubMenu", "Manage Login Functions", "Clear Screen", "Close the application"], "Main Menu")

        if choice == 1: #SIP SubMenu
                choiceC = menU(["Register a new SIP Card", "Renew a SIP Card", "Search for a SIP Card", "View all SIP cards", "Remove A SIP Entry", "Return to Main Menu"], "SIP Card SubMenu")

                if choiceC == 1:
                    nameU = Valid("Enter Customer Name : ", str, 40, 1)
                    cardU = str(Valid("Enter SIP Card Number : ", str, 5, 5, "SIP", int))
                    try:
                        x = customerData[cardU]
                        print("ERROR: This SIP Card Number has already been assigned")
                    except:      
                        dateData = dateB("SIP was issued : ")
                        customerData[str(cardU)] = [str(nameU), str(cardU), dateData[0], dateData[1]] # Saves data into a dictionary with the SIP card no. as the key
                        fileM("customerData.txt", "w", customerData) #Writes to file
                        print(f"User {nameU} has been assigned to SIP Card " + cardU)
                    
                if choiceC == 2:
                    searchValue = Valid("Enter SIP Card Number to renew : ", str, 5, 5, "SIP")
                    try:
                        nameU = customerData[searchValue][0]
                        cardU = customerData[searchValue][1]
                        dateData = dateB("SIP was renewed : ")
                        customerData[searchValue] = [nameU, cardU, dateData[0], dateData[1]] # Saves a new date (current date) for SIP card holders as to renew their card
                        fileM("customerData.txt", "w", customerData)
                        print(f"User {nameU} has been renewed to issue date " + str(dateData[0]))
                    except:
                        print("ERROR: No SIP by that Name Exists")
                    
                if choiceC == 3:
                    print(" ")
                    try:
                        Data_Branch = customerData[input("Searching for SIP")] #Dynamic customer data printing
                        for i in range(0, len(Data_Branch)):
                            formatSplit(1, 10) #Text breaker to increase readability
                            print(customerDataKey[i] + " : " + str(Data_Branch[i]))
                        if datetime.datetime.now() > Data_Branch[3]:
                            print(f"\nSIP {Data_Branch[1]} has Expired") #Checks for outdated SIP card
                    except:
                        print("ERROR: No SIP by that Name Exists")
                    
                if choiceC == 4:
                    print(" ")
                    if customerData == {}:
                        print("ERROR: No SIP Data has been inputted yet")
                    else:
                            for Data_Tree in customerData:
                                Data_Branch = customerData[Data_Tree]
                                formatSplit(1, 10)
                                for i in range(0, len(Data_Branch)):
                                    print(str(customerDataKey[i]) + " : " + str(Data_Branch[i]))
                            if datetime.datetime.now() > Data_Branch[3]:
                                print(f"\nSIP {Data_Branch[1]} has Expired")

                if choiceC == 5:
                    print(" ")
                    if customerData == {}:
                        print("ERROR: No SIP Data has been inputted yet")
                    else:
                        try:
                            SIPD = str(Valid("Enter SIP Card Number to Remove : ", str, 5, 5, "SIP"))
                            del customerData[SIPD] #Attempts to remove the card                            
                            fileM("customerData.txt", "w", customerData)
                            print(f"SIP {SIPD} has been removed")
                        except:
                            print("ERROR: No SIP by that Name Exists")

                            
        if choice == 2: #Buisness SubMenu
            choiceB = menU(["Register a new Business", "Search for a Business", "View all Businesses", "View Claimed Benefits of a Buisness", "View Claimed Benefits of a Buisness this month", "Remove a Buisness", "Return to Main Menu"], "Buisness SubMenu")
            if choiceB == 1: #Adding a Buisness
                nameU = Valid("Enter Shop Name : ", str, 100, 1)
                DisDay = Valid("Enter Discounted Day : ", str, 8, 6)
                DelivF = Check("Free Delivery Is available")
                TwoFOne = Valid("Enter prduct with 2 for 1 offer : ", str, 100, 1)
                firmData[nameU] = [[nameU, DisDay, DelivF, TwoFOne], {}] #Saves buisness name as key
                fileM("firmData.txt", "w", firmData)
                print(f"Business {nameU} has been registered")

            if choiceB == 2: #Searching for a Buisness
                    try:
                        if firmData == {}:
                            print("ERROR: No Firm Data has been inputted yet")
                        else:
                            Data_Branch = firmData[input("Searching for Shop Name : ")][0]
                            for i in range(0, len(Data_Branch)):
                                formatSplit(1, 10)
                                print(firmDataKey[i] + " : " + str(Data_Branch[i]))
                    except:
                        print("ERROR: No Shops By This Name Exist")

            if choiceB == 3: #Viewing all buisnesses
                    print(" ")
                    if firmData == {}:
                        print("ERROR: No Firm Data has been inputted yet")
                    else:
                            for Data_Tree in firmData:
                                Data_Branch = firmData[Data_Tree][0]
                                formatSplit(1, 10)
                                for i in range(0, len(Data_Branch)):
                                    print(str(firmDataKey[i]) + " : " + str(Data_Branch[i]))

            if choiceB == 4: #View all Claimed benefits of a buisness
                    print(" ")
                    nameU = Valid("Enter Shop Name : ", str, 40, 1)
                    try:
                        if firmData[nameU][1] == {}:
                            print("ERROR: No customer claim benefit Data has been inputted for this firm, yet")
                        else:
                            try:
                                for Data_Tree in firmData[nameU][1]:
                                    Data_Branch = firmData[nameU][1][Data_Tree][0]
                                    formatSplit(1, 10)
                                    for i in range(0, len(Data_Branch)): #print(str("SIP" + Data_Tree + " Holder Has Claimed " + firmDataKey[i]) + "? : " + str(Data_Branch[i]))
                                        print(f"SIP {Data_Tree} Holder Has Claimed {firmDataKey[i]}? : " + str(Data_Branch[i]))
                            except:
                                print("ERROR: No SIP By This Name Exist")
                    except:
                        print("ERROR: No Shops By This Name Exist")

            if choiceB == 5: #View all claimed benefits of a buisness of current month
                    print(" ")
                    nameU = Valid("Enter Shop Name : ", str, 40, 1)
                    try:
                        if firmData[nameU][1] == {}:
                            print("ERROR: No customer claim benefit Data has been inputted for this firm, yet")
                        else:
                            try:
                                count_var = 0
                                for Data_Tree in firmData[nameU][1]:
                                    if datetime.datetime.now().strftime("%B") == firmData[nameU][1][Data_Tree][1].strftime("%B") and datetime.datetime.now().strftime("%Y") == firmData[nameU][1][Data_Tree][1].strftime("%Y"): #Checks whether month and year in realtime is the same as the benefit claim's month and year
                                        count_var += 1
                                        Data_Branch = firmData[nameU][1][Data_Tree][0]
                                        formatSplit(1, 10)
                                        for i in range(0, len(Data_Branch)):
                                            print(str("SIP" + Data_Tree + " Holder Has Claimed " + firmDataKey[i]) + "? : " + str(Data_Branch[i]))
                                if count_var == 0:
                                    print("ERROR: No Claims Have Been Inputted During This Month")
                            except:
                                print("ERROR: No Claims have been inputted yet")
                    except:
                        print("ERROR: No Firm with that name has been registered")

            if choiceB == 6: #Removes A Business
                    print(" ")
                    if firmData == {}:
                        print("ERROR: No firm Data has been inputted yet")
                    else:
                        try:
                            del firmData[str(Valid("Enter Shop Name to remove : ", str, 40, 1))]
                            fileM("firmData.txt", "w", firmData)
                            print("The firm has been removed")
                        except:
                            print("ERROR: No Buisness by that Name Exists")
                            
        if choice == 3: #Benefits SubMenu
            choiceA = menU(["View Benefit options", "Claim Benefit", "Return to Main Menu"], "Benefits Claim SubMenu")
            if choiceA == 1: #View benefit options of a buisness
                try:
                    nameU = Valid("Enter Shop Name : ", str, 40, 1)
                    Data_Branch = firmData[nameU][0]
                    for i in range(0, len(Data_Branch)):
                        formatSplit(1, 10)
                        print(firmDataKey[i] + " : " + str(Data_Branch[i]))
                except:
                    print("ERROR: The Shop Named " + nameU + " Wasn't Found")
                    
            elif choiceA == 2:#Claim benefit options of a buisness
                try:
                    nameU = Valid("Enter Shop Name : ", str, 40, 1)
                    breaktest = firmData[nameU]
                    try:
                        cardU = str(Valid("Enter SIP Card Number : ", str, 5, 5, "SIP"))
                        breaktest = customerData[cardU] #Test whether the code will break due to incorrect SIP being called
                        DisDay = Check("You Have Used the Discounted Day")
                        DelivF = Check("You Have Used Free Delivery")
                        TwoFOne = Check("You Have Used the Two for One offer")
                        firmData[nameU][1][str(cardU)] = [[DisDay, DelivF, TwoFOne], datetime.datetime.now()]
                        print("SIP" + cardU + " has claimed benefits from " + nameU)
                        fileM("firmData.txt", "w", firmData)
                    except:
                        print("ERROR: SIP" + cardU + " Has Not Been Registered")
                except:
                    print("ERROR: The Shop Name " + nameU + " Wasn't Found")
            
        if choice == 4: #Login Submenu
            logIns = fileO("Passwords.txt", {"Username" : "Password"})
            choiceL = menU(["Add a new Login", "View Existing Logins", "Return to Main Menu"], "Login SubMenu")
            if choiceL == 1:
                logU(0, True) #Adds new login
            if choiceL == 2:
                for i in logIns:
                    formatSplit(1, 10)
                    print(i + " : " + logIns[i]) #Prints all logins
                    
        if choice == 5: #Faux 'Clearing screen'
            print("\n"*80)
            
        if choice == 6: #Close Application
            print("Closing application")
            time.sleep(1.2)
            exit()
