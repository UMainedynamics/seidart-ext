from setuptools import setup, find_packages

setup(
    name='seidart-ext',
    version='0.0.1',
    description='An extension of the SeidarT package for seismic and electromagnetic data processing.',
    author='Steven Bernsen',
    author_email='stevenbernsen@gmail.com',
    packages=find_packages(),
    install_requires=[
        numpy, pandas, matplotlib, sklearn, scipy, glob2, os
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)