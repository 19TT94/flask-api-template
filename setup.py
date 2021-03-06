from setuptools import find_packages, setup

setup(
    name='api',
    version='1.0.0',
    maintainer="Taylor Tobin",
    maintainer_email="19tt94@gmail.com",
    description="Flask Api Template",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'click',
        "pylint"
    ],
    extras_require={
      "test": [
        "pytest",
        "coverage"
      ]
    }
)
