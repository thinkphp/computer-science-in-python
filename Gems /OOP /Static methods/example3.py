class Config:
    @staticmethod
    def get_database_url():
        return "jdbc:mysql://localhost:3306/mydatabase"
    
    @staticmethod
    def get_api_key():
        return "12345-abcde-67890-fghij"

# Access the configuration constants
db_url = Config.get_database_url()
api_key = Config.get_api_key()

print(db_url)  # Output: jdbc:mysql://localhost:3306/mydatabase
print(api_key)  # Output: 12345-abcde-67890-fghij
