from dotenv import dotenv_values

globals().update(dotenv_values(".env"))