from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in gallon/__init__.py
from gallon import __version__ as version

setup(
	name='gallon',
	version=version,
	description='Gallo Negro Poultry Administration',
	author='Luis Pillaga',
	author_email='lpillaga@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
