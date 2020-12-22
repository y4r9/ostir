import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="OSTIR",
    version="0.0.2",
    author="Barrick Lab/croots",
    author_email="croots@utexas.edu",
    description="Open Source Transcription Initiation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/barricklab/rbs-calculator",
    packages=setuptools.find_packages(exclude=['tests', 'calibration']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    include_package_data=True,
    entry_points='''
        [console_scripts]
        ostir=ostir.ostir:main
        '''
)
