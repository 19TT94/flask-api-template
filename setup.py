from setuptools import find_packages, setup

setup(
    name='api',
    version='1.0.0',
    maintainer="Taylor Tobin",
    maintainer_email="taylort@frm-ops.com",
    description="Flask Api Template",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'click',
        "pylint",
        "click",
        "sqlalchemy<1.4"
    ],
    extras_require={
      "test": [
        "pytest",
        "coverage"
      ]
    }
)