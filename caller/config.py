import os

APP_ENV = os.getenv("APP_ENV", "development")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "rafal")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "rafal1234")
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "calls")
TEST_DATABASE_NAME = os.getenv("DATABASE_NAME", "calls_test")
