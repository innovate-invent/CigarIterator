from setuptools import setup, find_packages
from CigarIterator.__version import __versionstr__

with open('README.rst') as readme:
    setup(
        name='CigarIterator',
        version=__versionstr__,
        packages=find_packages(),
        long_description=readme.read(),
        url='https://github.com/innovate-invent/CigarIterator',
        license='MIT',
        author='Nolan',
        author_email='innovate.invent@gmail.com',
        description='Iterates pysam AlignedSegments, managing the different coordinate spaces of the cigar, sequence, MD, and reference.',
        include_package_data=True
    )