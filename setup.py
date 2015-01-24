import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-altauth',
    version='0.1',
    packages=['altauth'],
    include_package_data=True,
    license='BSD License', 

    long_description=README,

    install_requires=[
    "rsa >= 3.1.2",
    ],
    ,
)
