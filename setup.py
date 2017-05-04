# -*- coding: utf-8 -*-

from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

extensions = [
    Extension("example.hello",
              sources=["example/hello.pyx", "src/hello.cpp"],
              include_dirs=["./include"],
              language="c++")
]

setup(name="python-cxx-example",
      version="0.0.1",
      author="Erle Carrara",
      packages=find_packages(),
      ext_modules=cythonize(extensions),
      license='MIT',
      install_requires=['numpy'],
      )
