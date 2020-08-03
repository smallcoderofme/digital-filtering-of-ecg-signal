from setuptools import setup
from Cython.Build import cythonize

setup(
	name="Hello World App",
	version="0.1",
	ext_module=cythonize('utils.pyx'),
	zip_safe=False	
)