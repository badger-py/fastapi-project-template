from db import Base, engine


# create tables
Base.metadata.create_all(bind=engine)
print("db was created sucesfully")

# NOTE: you can use Faker libary to create fake data
