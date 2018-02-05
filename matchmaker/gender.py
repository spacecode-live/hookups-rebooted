class Gender:
    """An enumerator for a gender class.

    This class is supposed to be used as an enumerator of bitmasks, so that
    it is possible to use it for preference, as well as gender.
    """
    none = 0b000000
    male = 0b000001
    female = 0b000010
    every = 0b111111