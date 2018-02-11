class Matchmaker:
    """This class is designed for matchmaking Persons

    TODO:
        Improve matchmaking speed
    """

    def __init__(self):
        self.queue = []

    @property
    def queue(self):
        """A list of queued people"""
        return self.__queue

    @queue.setter
    def queue(self, value):
        self.__queue = value

    @queue.deleter
    def queue(self):
        del self.__queue

    def clear_queue(self):
        """Clears the queue"""
        self.queue = []

    def queue_person(self, person):
        """Adds a person to the queue.

        Args:
            person (Person): The person to be added to the queue.
        """
        self.queue.append(person)
        self.matchmake()

    def matchmade_event(self, person_a, person_b):
        """Event triggered when self.matchmake() makes a match

        This function is called when self.matchmake() creates a match between
        two people. It is intended to be overriden, if necessary. By default,
        it will emit a socket message to both Persons notifying them of their
        match, and passing the other Person

        Args:
            person_a (Person): The first person
            person_b (Person): The second person

        Todo:
            Write the actual function
        """
        print "Matchmade!"

    def matchmake(self):
        """Tries to matchmake as many people as possible, waiting in the queue.

        Returns:
            int: Number of matches made (the number of people removed from the
            queue, divided by two)
        """
        matches = 0
        for person in self.queue:
            for other_person in self.queue:
                if (other_person is not person):
                    if (person.is_interested_in(other_person)):
                        self.matchmade_event(person, other_person)
                        self.queue.remove(other_person)
                        self.queue.remove(person)
                        matches += 1
                        break
