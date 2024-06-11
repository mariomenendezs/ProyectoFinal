import pandas as pd
#https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
BASE_URL= "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
DW_PATH="./files_dump/raw_data"




def get_data_month(date_:str) ->None:
    """
    Downloads the data for specific month. 
    
    Args:
        date_(str): The date in the format: 'YYYY-MM'.
    
    Returns:
        None
    """
    url=f"{BASE_URL}{date_}.parquet"
    print(url)
    df=pd.read_parquet(url)
    #guardo el archivo
    df.to_parquet(
        f"{DW_PATH}{date_}.parquet",
        index=False
    )
    print(f"Archivo {DW_PATH}{date_}.parquet descargado correctamente")
    
if __name__ == "__main__":
    get_data_month("2024-01")
    
    def data_range(start_:str,end_:str)-> list:
        """ 
        Generates a list of dates between the start  and end dates.
        
        Args:
            start_ (str): The start date in the format 'YYYYMM'.
            end_ (str): The end date in the format 'YYYYMM'.
        
        Returns:
            list: A list of dates in the format 'YYYYMM'.
        """
        #convertir a datetime start_
        start_date=pd.to_datetime(start_,format="%Y%m")
        #convertir a datetime end_
        end_date=pd.to_datetime(end_,format="%Y%m")
        #generar rango de fechas entre start_date y end_date
        data_range=pd.date_range(start_date,end_date,freq="ME")
        #convertir a string y formato YYYY-MM
        date_range_list= date_range_list.strftime("%Y-%m").tolist()
        print(date_range_list)
        return date_range_list
    
    def data_range(start_date:str,end_date:str)-> list:
        """ 
        Generates a list of dates between the start  and end dates.
        
        Args:
            start_ (str): The start date in the format 'YYYYMM'.
            end_ (str): The end date in the format 'YYYYMM'.
        
        Returns:
            list: A list of dates in the format 'YYYYMM'.
        """
        data_range=data_range(start_date,end_date)
        for date in data_range:
            get_data_month(date)
            
if __name__ == "__main__":
    start_date="202101"
    end_date="202103"
    DATE_RANGE= data_range(start_date,end_date)
    for date in DATE_RANGE:
        get_data_month(date)
        
        