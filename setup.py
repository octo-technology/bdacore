# no error
from setuptools import setup
import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

with open("ci/test_requirements.txt") as f:
    test_reqs = [l for l in f.readlines()]

version = '3.0.2.dev0'

setup(
    name="bdacore",
    version=version,
    long_description=open("README.md").read(),

    # to make installation easy for developers : pip install .[test]
    extras_require={
        'test': test_reqs
    },

    # to run tests with setuptools (and let setuptools install
    # test requirements automatically) : python setup.py test
    setup_requires=[] + pytest_runner,
    tests_require=test_reqs,
)
