from setuptools import setup

setup(
	name="pydbg",
	version="1.0",
	author="pedram amini",
	description="An experimental attempt to update pydbg to Python 2.7. Some stuff probably doesn't work.",
	packages=["pydbg"],
	install_requires=['pydasm>=1.0'],
	dependency_links=['https://github.com/haystack-ia/pydasm/tarball/master#egg=pydasm-1.0']
	)
