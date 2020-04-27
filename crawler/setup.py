from setuptools import find_packages, setup

setup(
    name='MandaTrampo',
    version='1.0.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = mandatrampo.settings']},
)
