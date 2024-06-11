import os
import pandas as pd
import logging

# URL base for the parquet files
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_"
# Directory path to save the downloaded files
DW_PATH = "./files_dump/"

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_data_month(date_: str) -> None:
    """
    Downloads the data for a specific month.

    Args:
        date_ (str): The date in the format: 'YYYY-MM'.

    Returns:
        None
    """
    url = f"{BASE_URL}{date_}.parquet"
    logger.info("Downloading data from %s", url)
    df = pd.read_parquet(url)
    
    # Save the file
    output_path = os.path.join(DW_PATH, f"{date_}.parquet")
    df.to_parquet(output_path, index=False)
    logger.info("File %s downloaded successfully", output_path)

def data_range(start_: str, end_: str) -> list:
    """
    Generates a list of dates between the start and end dates.

    Args:
        start_ (str): The start date in the format 'YYYYMM'.
        end_ (str): The end date in the format 'YYYYMM'.

    Returns:
        list: A list of dates in the format 'YYYY-MM'.
    """
    # Convert to datetime start_ and end_
    start = pd.to_datetime(start_, format="%Y%m")
    end = pd.to_datetime(end_, format="%Y%m")
    
    # Generate the date range
    dates = pd.date_range(start, end, freq='MS').strftime("%Y-%m").tolist()
    return dates

if __name__ == "__main__":
    # Example usage
    start_date = "202301"
    end_date = "202304"
    
    dates = data_range(start_date, end_date)
    
    for date in dates:
        file_path = os.path.join(DW_PATH, f"{date}.parquet")
        if os.path.exists(file_path):
            logger.info("The file %s already exists", file_path)
        else:
            get_data_month(date)