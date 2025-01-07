from setuptools import setup, find_packages

setup(
    name='stellar-xdr',
    version='1.0.0',
    author='KOSASIH',
    author_email='kosasihg88@gmail.com',
    description='A library for encoding and decoding Stellar XDR data structures.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/KOSASIH/stellar-xdr',  # Replace with your repository URL
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'nacl==1.4.0',  # Cryptographic library
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
