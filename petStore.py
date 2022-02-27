from pet import Pet
import mysql.connector


class PetStore:
    def __init__(self, pet_list=None) -> None:
        if pet_list is None:
            pet_list = []
        self.petList = pet_list

    def add_pet(self):
        p1 = Pet()
        print("Please name your pet.py")
        p1.name = input()
        print("What type of pet?")
        p1.type = input()
        print("Please type in the age of your pet.py")
        p1.age = input()

        self.petList.append(p1)

    def print_pet_info(self):
        for pet in self.petList:
            print(pet.getInfo())

    def read_from_database(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password",
            database="petstore"
        )

        cursor = mydb.cursor()

        cursor.execute("SELECT * FROM pets")

        results = cursor.fetchall()

        for result in results:
            pet = Pet(result[1], result[2], result[3])
            self.petList.append(pet)
