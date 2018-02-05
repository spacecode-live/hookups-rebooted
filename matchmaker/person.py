from gender import Gender
from interest import Interest

class Person:
    """Represents a single person with his preferences.

    The default constructor creates a person without any attributes, but with
    a counted id.

    Attributes:
        id (int): An id of the person
        gender (Gender): The gender of the person.
        preference (Gender): A bitmask of the genders that the person is
            looking for.
        interest (Interest): What the person is interested in doing during the
            hookup.
    """

    id_counter = 0

    def __init__(self):
        self.id = Person.id_counter
        Person.id_counter += 1

        self.gender = Gender.none
        self.preference = Gender.every
        self.interest = Interest.none

    @property
    def gender(self):
        """Gender: The gender of the person."""
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value

    @gender.deleter
    def gender(self):
        del self._gender

    @property
    def preference(self):
        """Gender: The preference of the person."""
        return self._preference

    @preference.setter
    def preference(self, value):
        self._preference = value

    @preference.deleter
    def preference(self):
        del self._preference

    @property
    def interest(self):
        """Interest: The interest of the match of the person."""
        return self._interest

    @interest.setter
    def interest(self, value):
        self._interest = value

    @interest.deleter
    def interest(self):
        del self._interest
