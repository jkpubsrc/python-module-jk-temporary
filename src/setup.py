from setuptools import setup


def readme():
	with open('README.rst') as f:
		return f.read()


setup(name='jk_temporary',
	version='0.2017.1.13',
	description='Collection of utility functions and classes to manage temporary data.',
	author='Jürgen Knauth',
	author_email='pubsrc@binary-overflow.de',
	license='Apache 2.0',
	url='https://github.com/jkpubsrc/python-module-jk-temporary',
	download_url='https://github.com/jkpubsrc/python-module-jk-temporary/tarball/0.2017.1.13',
	keywords=['temp', 'temporary', 'tempfiles'],
	packages=['jk_temporary'],
	install_requires=[
	],
	include_package_data=True,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'License :: OSI Approved :: Apache Software License', 
		'Programming Language :: Python :: 3.5',
	],
	long_description=readme(),
	zip_safe=False)

