import pandas as pd

def startmenu ():

    while(1):

        print("""
        1) Read .csv
        2) Show Details of Dataframe
        3)
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
    pass

def findcol (somekey):
    pass

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

