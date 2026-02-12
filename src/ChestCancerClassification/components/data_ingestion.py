import os
import zipfile
import gdown
from ChestCancerClassification import logger
from ChestCancerClassification.utils.common import get_size
from ChestCancerClassification.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
     
    def download_file(self) -> str:
        """
        Fetch data from the URL
        """
        try:
            dataset_url = self.config.source_URL
            zip_download_path = self.config.local_data_file

            os.makedirs(os.path.dirname(zip_download_path), exist_ok=True)

            logger.info(f"Downloading data from {dataset_url} into file {zip_download_path}")

            gdown.download(
                url=dataset_url,
                output=zip_download_path,
                fuzzy=True,
                quiet=False
            )

            logger.info("Download completed successfully")
            return zip_download_path

        except Exception:
            logger.exception("Failed during data download")
            raise
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)