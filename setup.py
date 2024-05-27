from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        name="find_nearest",
        sources=["find_nearest.pyx"],
        language="c++",  # Использование C++ компилятора
        include_dirs=[np.get_include()],
    )
]

setup(
    ext_modules=cythonize(extensions),
    zip_safe=False,
)
