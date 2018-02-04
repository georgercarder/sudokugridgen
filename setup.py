from setuptools import setup

setup(name="sudokugridgen",
	version='0.1',
	description='a sudoku grid generator',
	url='http://github.com/georgercarder/sudokugridgen',
	author='George Carder',
	author_email='georgercarder@gmail.com',
	license='MIT',
	scripts=[],	
	install_requires=[], ## other packages	
	dependency_links=[], ## links for dep not on pypi	
	test_suite='pytest',		## nose.collector	
	tests_require=['pytest'],	## 'nose'
	setup_requires=['pytest-runner'],
	packages=['sudokugridgen'],
	zip_safe=False)

