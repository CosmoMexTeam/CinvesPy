
# Configuracion para compilar

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules= [
    Extension("advec_cy",
              sources=["advec_cy.pyx"], #  Se especifican los archivos que contienen el codigo  
              libraries=["m"]           #  Tambien las librerias externas
    )
]

setup(
    ext_modules = cythonize(ext_modules)
)

