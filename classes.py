# http://python-textbok.readthedocs.org/en/latest/Classes.html

"""
	classes are a way to group related data and functions act on that data.
	class is a data type, we create an object of it which called an instanse.
	In python, eveything is an object - eveything is an instanse of some classes


	type() : to find out the type of any object

	attributes :  	data values which we store inside an object
	methods : 		functions which are associated with the object

	built-in objects : exapmes >> strings and lists.


"""

'''
import datetime	# datetime is Module.
				# datetime.date : date is a class into [datetime] Module

class Person(object) :

	"""

	init__ is sometimes called the object’s constructor, because it is used similarly to the way that constructors are used in other languages, 
	but that is not technically correct – it’s better to call it the [initialiser]. 

	There is a different method called __new__ which is more analogous to a constructor, but it is hardly ever used.

	"""

	def __init__(self, name , surname, birthdate, address, telephone, email ) :
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.address = address
		self.telephone = telephone
		self.email = email


	def age(self) :

		#get today date
		today = datetime.date.today()

		age = today.year - self.birthdate.year

		if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day) :
			age -= 1

		return age



person = Person("Jane", "Doe", 
				datetime.date(1992, 3, 12), 
				"No. 12 Short Street, Greenville",
				"555 456 0987",
				"jane.doe@example.com")


print(person.name)
print(person.email)
print(person.age())





# Instance attributes --------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

"""
	In Python, you can add new attributes, and even new methods, to an object on the fly.

"""

""" Exercise 2 :

	Rewrite the Person class so that a person’s age 
	is calculated for the first time when a new person instance is created, 
	and recalculated (when it is requested) if the day has changed since the 
	last time that it was calculated. 
"""

import datetime

class Person(object) :
	def __init__(self, name , surname, birthdate, address, telephone, email) :
		self.name = name
		self.surname = surname
		self.birthdate = birthdate
		self.address = address
		self.telephone = telephone
		self.email = email


		# This isn't strictly necessary, but it clearly introduces [ ---> Instance attributes <--- ]
		self._age = None
		self._age_last_recalculated = None

		self._recalculate_age()

		"""
			Starting an attribute or method name with an underscore (_) is a convention which we use to indicate that it is 
			a “private” internal property and should not be accessed directly. 

			In a more realistic example, our cached value would sometimes expire and need to be recalculated – so we should always use the age method to make sure that we get the right value.

		"""


	def _recalculate_age(self) :
		today = datetime.date.today()
		age = today.year - self.birthdate.year

		if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day) :
			age -= 1

		self._age = age
		self._age_last_recalculated = today

	def age(self) :
		if datetime.date.today() > self._age_last_recalculated :
			self._recalculate_age()

		return self._age




person = Person("Jane", "Doe", 
				datetime.date(1992, 3, 12), 
				"No. 12 Short Street, Greenville",
				"555 456 0987",
				"jane.doe@example.com")

print(person.name)
print(person.age())
print(person._age_last_recalculated)



'''

# Class attributes -----------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------


"""
	All the attributes which are defined on a Person instance are instance attributes – they are added to the instance when the __init__ method is executed .
	We can, however, also define attributes which are set on the class. These attributes will be shared by all instances of that class


	Class attributes are often used to define constants which are closely associated with a particular class. 
	Although we can use class attributes from class instances, we can also use them from class objects, without creating an instance:
"""

class Person(object) :
	# class attrs
	TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

	def __init__(self, title, name, surname) :
		if title not in self.TITLES :
			raise ValueError("%s is not a valid title." % title)

		self.title = title
		self.name = name
		self.surname = surname


# access class attr directly from the class [note : P not p]
print(Person.TITLES)

# access class attr from an instance
person = Person('Dr', 'Matar', 'John')
print(person.TITLES)




""" Class attributes can also sometimes be used to provide default attribute values """

class Person(object) :
	deceased = False

	def mark_as_deceased(self):
		self.deceased = True




"""
	When we set an attribute on an instance which has the same name as a class attribute, 
	we are overriding the class attribute with an instance attribute, which will take precedence over it. 
	If we create two Person objects and call the mark_as_deceased method on one of them, we will not affect the other one.

	We should, however, be careful when a class attribute is of a mutable type – because if we modify it in-place, 
	we will affect all objects of that class at the same time. Remember that all instances share the same class attributes:

"""

class Person(object):
	pets = []

	def add_pets(self, pet) :
		self.pets.append(pet)

Jane = Person()
Bob = Person()

Jane.add_pets("cat")
print(Jane.pets) # Cat
print(Bob.pets) # Cat !!!!! opps that's wrong, we never appeanded Cat to Bob' pets list


""" # What we should do in cases like this is initialise the mutable attribute as an instance attribute, inside __init__. Then every instance will have its own separate copy """
class Person(object):
	def __init__(self) :
		self.pets = []

	def add_pets(self, pet) :
		sel.pets.append(pet)

Jane = Person()
Bob = Person()

Jane.add_pets("cat")
print(Jane.pets) # Cat
print(Bob.pets) # nothing cuz we haven't added any pets yet !



"""
	Note that method definitions are in the same scope as class attribute definitions, 
	so we can use class attribute names as variables in method definitions (without self, which is only defined inside the methods):
"""
class Person:
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, title, name, surname, allowed_titles=TITLES):
        if title not in allowed_titles:
            raise ValueError("%s is not a valid title." % title)

        self.title = title
        self.name = name
        self.surname = surname


""" Exercise 3
	Explain the differences between the attributes name, surname and profession, and what values they can have in different instances of this class :
"""

class Smith:
	surname = "Smith"
	profession = "smith"

	def __init__(self, name, profession=None) :
		self.name = name
		if profession is not None:
			self.profession = profession