#this file defines all configuaration vlaues the app needs
#(DB connection info , app name ,etc)

#pydantic_settings : automatically reads environment variables and validates
#their types

from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):

    # MongoDB Settings
    MONGO_URI: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "hospital_support"

    #Gives the app a name 
    APP_NAME:str = "Hospital Support Request System API"

    # Informs pydantic-setings to load values from .env file
    model_config= SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")

# shared settings object that all other files can import 
settings= Settings()