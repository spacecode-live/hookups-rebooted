class Interest:
    """An enumerator for one's hookup interests.

    This class is supposed to be used as an enumerator of bitmasks, so that it
    is possible to combine multiple interests.
    """
    none = 0b000000
    kiss = 0b000001
    oral = 0b000010
    coitus = 0b000100
    romance = 0b100000
    every = 0b111111