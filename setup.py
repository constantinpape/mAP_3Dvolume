import runpy
import itertools
from setuptools import setup, find_packages

__version__ = '0.0.1'
# TODO load requirements from requirements.txt

setup(
    name="map3d",
    packages=find_packages(),
    version=__version__,
    # install_requires=requires,
    url="https://github.com/ygCoconut/mAP_3Dvolume",
    license="MIT"
)
