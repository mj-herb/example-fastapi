from pydantic_settings import BaseSettings
# BaseSettings 가 pydantic package에서 pydnatic_settings로 옮겨짐

class Settings(BaseSettings):
   database_hostname: str
   database_port: str
   database_password: int  
   database_name: str
   database_username: str
   secret_key: str
   algorithm: str
   access_token_expire_minutes: int

   class Config:
      env_file = ".env"



settings = Settings()

