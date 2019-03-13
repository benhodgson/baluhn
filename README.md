# Baluhn: Base-agnostic Luhn

Baluhn provides a base-independent implementation of the [Luhn
algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm) for Python. It is
useful for generating and verifying check digits in arbitrary bases.

From Wikipedia:

> The Luhn algorithm or Luhn formula, also known as the "modulus 10" or "mod
> 10" algorithm, is a simple checksum formula used to validate a variety of
> identification numbers, such as credit card numbers, IMEI numbers,
> National Provider Identifier numbers in US and Canadian Social Insurance
> Numbers.

## Installation

Use `pip install baluhn` or `python setup.py install`.

## Usage

The `baluhn` module provides two functions: `verify` and `generate`.

`generate` calculates the Luhn check character for the given input string in
the given base. This character should be appended to the input string to
produce a valid Luhn string. `verify` tests whether or not a string is a valid
Luhn string in the given base. By default, Baluhn operates in base 10:

```python
>>> from baluhn import generate, verify
>>> verify('5105105105105100') # MasterCard test number
True
>>> value = '510510510510510' # note the missing check digit
>>> generate(value)
'0'
>>> verify(value + '0')
True
>>> verify(value + '7')
False
```

When operating in a base other than decimal, encoder and decoder callables
should be supplied. The encoder should take a single argument, an integer, and
return the character corresponding to that integer in the operating base.
Conversely, the decoder should take a string containing a single character and
return its integer value in the operating base. Note that the mapping between
values and characters defined by the encoder and decoder should be one-to-one.

For example, when working in hexadecimal:

```python
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
```

## Author

Baluhn is written by [Ben Hodgson](http://benhodgson.com/) and maintained by [Four Digits](https://fourdigits.nl/).

## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute
this software, either in source code form or as a compiled binary, for any
purpose, commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
