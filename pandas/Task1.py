''' 
    df=pd.read_csv("C:\Users\ADMIN\Downloads\covid.csv")  # ERROR

    this code rise error because python treats '\' as unicode means \n or \t  
        but before string if we write 'r' (raw string) then it will not rise error 
        or we can use double backslashes \\ 
        we can use forward slashes too in windows //
        
    --> 3 ways to read file :

        df=pd.read_csv(r"C:\Users\ADMIN\Downloads\covid.csv") 
        df=pd.read_csv("C:/Users/ADMIN/Downloads/covid.csv") 
        df=pd.read_csv("C:\\Users\\ADMIN\\Downloads\\covid.csv") 
        
        '''



import pandas as pd

try:
    # load CSV
    df=pd.read_csv(r"C:\Users\ADMIN\Downloads\covid.csv")

    # Show first 3 rows
    print(df.head(3))

    # Check missing values count
    print(df.isna().sum())

    # Check column exists or not then fill null cell with avg value
    if 'Confirmed' in df.columns:
        avg_cnfm = df['Confirmed'].mean()
        df.fillna({'Confirmed':avg_cnfm},inplace=True)
        print('avg conf',avg_cnfm)
    else:
        print('not found')
    
    # save cleaned data
    df.to_csv(r'C:\Users\Admin\Downloads\covid_cleaned.csv',index=False)

except FileNotFoundError:
    print("❌ File not found. Check path or filename")
except Exception as e:
    print(e)