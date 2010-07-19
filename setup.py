from distutils.core import setup

setup(
    name='baluhn',
    version='0.1',
    license='Public Domain',
    description='A base-agnostic implementation of the Luhn Algorithm for '
        'Python. Useful for generating and verifying check digits.',
    package_dir = {'':'src'},
    py_modules=['baluhn'],
    url='http://github.com/benhodgson/baluhn',
    author='Ben Hodgson',
    author_email='ben@benhodgson.com',
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
