__all__ = ['generate', 'verify']

decimal_decoder = lambda s: int(s, 10)
decimal_encoder = lambda i: str(i)


def luhn_sum_mod_base(string, base=10, decoder=decimal_decoder):
    # Adapted from http://en.wikipedia.org/wiki/Luhn_algorithm
    digits = list(map(decoder, string))
    return (sum(digits[::-2]) +
        sum(list(map(lambda d: sum(divmod(2*d, base)), digits[-2::-2])))) % base
    

def generate(string, base=10, encoder=decimal_encoder,
             decoder=decimal_decoder):
    """
    Calculates the Luhn mod N check character for the given input string. This
    character should be appended to the input string to produce a valid Luhn
    mod N string in the given base.

    >>> value = '4205092350249'
    >>> generate(value)
    '1'

    When operating in a base other than decimal, encoder and decoder callables
    should be supplied. The encoder should take a single argument, an integer,
    and return the character corresponding to that integer in the operating
    base. Conversely, the decoder should take a string containing a single
    character and return its integer value in the operating base. Note that
    the mapping between values and characters defined by the encoder and
    decoder should be one-to-one.

    For example, when working in hexadecimal:

    >>> hex_alphabet = '0123456789abcdef'
    >>> hex_encoder = lambda i: hex_alphabet[i]
    >>> hex_decoder = lambda s: hex_alphabet.index(s)
    >>> value = 'a8b56f'
    >>> generate(value, base=16, encoder=hex_encoder, decoder=hex_decoder)
    'b'
    >>> verify('a8b56fb', base=16, decoder=hex_decoder)
    True
    >>> verify('a8b56fc', base=16, decoder=hex_decoder)
    False

    """

    d = luhn_sum_mod_base(string + encoder(0), base=base, decoder=decoder)
    if d != 0:
        d = base - d
    return encoder(d)


def verify(string, base=10, decoder=decimal_decoder):
    """
    Verifies that the given string is a valid Luhn mod N string.

    >>> verify('5105105105105100') # MasterCard test number
    True

    When operating in a base other than decimal, encoder and decoder callables
    should be supplied. The encoder should take a single argument, an integer,
    and return the character corresponding to that integer in the operating
    base. Conversely, the decoder should take a string containing a single
    character and return its integer value in the operating base. Note that
    the mapping between values and characters defined by the encoder and
    decoder should be one-to-one.

    For example, 'b' is the correct check character for the hexadecimal string
    'a8b56f':

    >>> hex_decoder = lambda s: '0123456789abcdef'.index(s)
    >>> verify('a8b56fb', base=16, decoder=hex_decoder)
    True

    Any other check digit (in this example: 'c'), will result in a failed
    verification:

    >>> verify('a8b56fc', base=16, decoder=hex_decoder)
    False

    """

    return luhn_sum_mod_base(string, base=base, decoder=decoder) == 0
