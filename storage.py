"""
Handles persistant storage of banking system data using JSON.
Provides methods to:
 - Save data (accounts, transactions) to a file.
 - Load data from a file.
"""

import json

class Storage:
    """
    Storage class for saving and loading banking system data.
    Attributes:
        filename (str): Name of the JSON file used for persistence. 
    """
    def __init__(self, filename="bank.data.json"):
        """
        Initialize a Storage object.

        Args:
            filename (str): Optional, JSON file name for storing data. Defaults to 'bank.data.json'.
        """
        self.filename =filename
    
    def save(self, data):
        """
        Save provided data to the JSON file.
        Args:
            data (dict): Data to save. Typically contains 'accounts' and 'transactions'.
        Notes:
         - Uses indentation for readability.
         - Overwrites existing file content.
        """
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)
    
    def load(self):
        """
        Load data from the JSON file.

        Returns:
            dict: Loaded data containig 'accounts' and 'transactions'.
        Notes:
         - If file does not exist, returns empty structure. 
        """
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # Return default empty structure if file is missing.
            return {"accounts":[], "transactions": []}
