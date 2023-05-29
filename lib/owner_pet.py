

class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type
    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input object is not of type Pet")
        pet.owner = self            
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
    


    # class Pet:
#     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
#     all = []
    
#     def __init__(self, name, pet_type, owner =None):
#         self.name = name
#         self.owner = owner
#         self.pet_type = pet_type
#         if pet_type not in Pet.PET_TYPES:
#             raise Exception("Please enter valid Pet Type")
# #3. Define a class variable all that stores all instances of the Pet class, add all = [] and append all here
#         Pet.all.append(self)    
#     # @property
#     def owner(self, owner):
#         self.owner = owner
    
# class Owner:
#     def __init__(self, name):
#         self.name =name
        
#     #Method that returns 

#     def pets(self):
#         return [pet for pet in Pet.all if pet.owner == self]
    

    
#     def add_pet(self, pet):
#        if not isinstance(pet, Pet):
#            raise TypeError("Invalid pet type!")
#        pet.owner = self
#        Pet.all.append(pet)
       
       
        

#     def get_sorted_pets(self):
#         return sorted(self.pets(), key=lambda pet: pet.name)