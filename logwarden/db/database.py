from sqlalchemy.ext.asyncio import create_async_engine
from logwarden.core.config import Settings
from sqlalchemy.ext.asyncio import async_sessionmaker

settings = Settings()

engine = create_async_engine(
    settings.database_url,
    pool_pre_ping=True
)

session_factory = async_sessionmaker(
    engine,
    expire_on_commit=False
)

