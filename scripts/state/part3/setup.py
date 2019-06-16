from setuptools import setup, find_packages
setup(
    name="random_quote",
    version="0.2.1",
    packages=['random_quote'],
    package_dir={'':'src'},
    install_requires=['webob'],
    include_package_data=True
)