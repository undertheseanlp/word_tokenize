from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

setup(ext_modules=
      cythonize('tagged_cython.pyx', annotate=True, language="c++"))
