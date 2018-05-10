from setuptools import setup, find_packages
setup(
    name="iGenome",
    version="0.1",
    packages=find_packages(),
    author="Lucas Rocha",
    license="GPLv3",
    description="A package for whole genome resequencing assembly",
    entry_points={
        'console_scripts': ['iGenome = iGenome.__main__:main'],
        },
    classifiers=["Programming Language :: Python :: 3"],
)