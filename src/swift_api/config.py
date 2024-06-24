from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    keycloak_url: str = "http://localhost:8080"
    keycloak_realm: str = "swift-realm"
    keycloak_client_id: str = "swift-api"
    keycloak_client_secret: str = "swift-api-secret"


settings = Settings()
