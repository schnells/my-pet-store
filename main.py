from petStore import PetStore

print("Welcome to the pet store.")
petStore = PetStore()

petStore.read_from_database()

petStore.print_pet_info()
