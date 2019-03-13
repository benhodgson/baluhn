from os import path
from setuptools import setup


def long_description():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


setup(
    name='baluhn',
    version='0.1.1',
    license='Public Domain',
    description='A base-agnostic implementation of the Luhn Algorithm for '
        'Python. Useful for generating and verifying check digits.',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    package_dir = {'':'src'},
    py_modules=['baluhn'],
    url='http://github.com/benhodgson/baluhn',
    author='Ben Hodgson',
    author_email='ben@benhodgson.com',
    maintainer='Four Digits',
    maintainer_email='info@fourdigits.nl',
    keywords = ['luhn', 'mod10', 'check digit', 'luhn mod N'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
