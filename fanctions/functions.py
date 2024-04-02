import pandas as pd

def startmenu ():
    """
    A Menu that connects all the possible actions on a dataset.

    Returns:
        Nothing by itself.
    """

    while(1):

        print("""
        1) Read .csv
        2) Show Details of Dataframe's dimensions
        3)
        4)
        5)
        6) Save to .csv
        *) Quit
        """)
        option = int(input("User option: "))
        if option == 1:
            df = opencsv('./Pandas/questionnaire.csv')
        elif option == 2:
            try:
                showinfo(df)
            except NameError as e:
                print(f"Error Type is: {e}")
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            try:
                savemenu(df)
            except NameError as e:
                print(f"Error Type is: {e}")
        else:
            break

    print("Thanks for playing ! \n Goodbye!")


def opencsv (path):
    """
    A function with different ways to open a .csv file.

    Args: 
        path: The path or link to the .csv.

    Returns: 
        df: the Dataframe

    """
    try:

        df = pd.read_csv(path)
        print("Open successful!")
        
    except OSError as e:
        print (f"Error : {e}")
        return None
    
    return df

def showinfo (df):

    while(1):

        print("""
        1) Dimensions with .info
        2) Dimensions with .shape
        3) Dimensions with .dtypes
        """)
        option = int(input("User option: "))
        if option == 1:
            print(df.info)
        elif option == 2:
            print(df.shape)
        elif option == 3:
            print(df.dtypes)
        else:
            break

def findrow (somekey):
    """
    
    """
    pass

def findcol (somekey):
    """
    
    """
    pass

def getname():
    """
    Reads a name from the user.

    Returns:
        name: string name
    """
    name = str(input("Give the desired name of the final file: "))
    return name

def savemenu(df):
    """
    A function that decides in which format to save the final image of the df.

    Args:
        df : The final dataframe.
    
    Returns:
        Nothing.
    """

    while(1):
        print(""" WHICH FORMAT:
              1) CSV
              2) XLSX
              3)
              4)
              5)
              *) Quit
        
        """)
        option = int(input())
        if option == 1:
            name = getname()
            exp_csv(df,name)
        elif option == 2:
            name = getname()
            exp_xlsx(df,name)
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        else:
            break

        
def epilog():
    """
    A functions that signals the end of the execution.
    """

    print(" The End. Thanks for playing!")
            

#You can add this as a method to a class. Making it more intuitive.
def exp_csv (df,name):
    """
    The functions takes a Dataframe and the desired name, saves it as .csv

    Args:
        df: The final Dataframe
        name: The desired name 

    Returns:
        Saves the {name}.csv file, utf8 encoding
    """
    
    df.to_csv(f"{name}.csv", index=False, encoding= 'utf8')

#You can add this as a method to a class. Making it more intuitive.
def exp_xlsx (df,name):
    """
    The functions takes a Dataframe and the desired name, saves it as .xlsx

    Args:
        df: The final Dataframe
        name: The desired name 

    Returns:
        Saves the {name}.xlsl file
    """
    
    df.to_csv(f"{name}.xlsx", sheet_name ="Sheet 1", index=False)

