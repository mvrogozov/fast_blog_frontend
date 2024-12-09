import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_DIR: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
    BASE_URL_BACK: str

    model_config = SettingsConfigDict(env_file=f'{BASE_DIR}/../.env')


settings = Settings()
# basedir = os.path.abspath(
#         os.path.join(os.path.dirname(__file__), '..')
#     )
# #print(str(basedir))
print(settings)
