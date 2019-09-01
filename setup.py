import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Promanagement",
    version="1.0.2",
    scripts=['promanagement.py', 'design.py', 'modules.py'],
    author="Imtiaz Ahmed",
    author_email="imtiaz@imtiazahmed.dev",
    description="Process Management GUI App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tiazahmd/promanagement",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.0',
)