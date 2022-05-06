import setuptools

setuptools.setup(
    name="CeSoR",
    version="0.0.1",
    author="anonymous",
    description="Cross-entropy Soft-Risk optimization algorithm",
    url="https://github.com/fictivename/CrossEntropySampler",
    packages=setuptools.find_packages(),
    install_requires = ["numpy","scipy","pandas","torch"])