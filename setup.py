from setuptools import setup, find_packages

setup(
    name = 'print_h5',
    version = '1.0.0',
    author = 'J. Neveu',
    description = 'Print contents of HDF5 file',
    packages = find_packages(),
    install_requires = ['numpy','h5py']
)