from petStore import PetStore

print("Welcome to the pet store.")
petStore = PetStore()

petStore.readFromDatabase()

petStore.printPetInfos()