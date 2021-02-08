#!/usr/bin/env python3
'The Punsy pip package'

import setuptools

def readme():
    'Return README.md as a string'
    with open('README.md', 'r') as istream:
        return istream.read()

setuptools.setup(
    name='puzzly',
    version='0.0.1',
    author='Tom McKeesick',
    author_email='tmck01@gmail.com',
    description='A puzzle solver & generator',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/tmck-code/puzzly',
    packages=setuptools.find_packages(),
    package_data={
        'puzzly': ['data/words_alpha.txt']
    },
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    entry_points={
        'console_scripts': [
            'puzzly = puzzly.word_target.dictionary:main',
        ],
    },
    install_requires=[]
)
