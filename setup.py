from setuptools import setup

setup(
    name='CigarIterator',
    version='1.0.0',
    packages=['enum', 're', ],
    url='https://github.com/innovate-invent/CigarIterator',
    license='MIT License',
    author='Nolan',
    author_email='innovate.invent@gmail.com',
    description='Iterates pysam AlignedSegments, managing the different coordinate spaces of the cigar, sequence, MD, and reference.'
)
