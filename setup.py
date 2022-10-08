from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in custom_preciholesports/__init__.py
from custom_preciholesports import __version__ as version

setup(
	name="custom_preciholesports",
	version=version,
	description="Custom Preciholesports",
	author="preciholesports",
	author_email="rehan@preciholesports.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
