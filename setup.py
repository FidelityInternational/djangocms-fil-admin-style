from setuptools import find_packages, setup

import djangocms_fil_admin_style


INSTALL_REQUIREMENTS = [
    'Django>=1.11,<3.3',
    'django-cms>=3.5.0',
]

setup(
    name='djangocms-fil_admin_style',
    packages=find_packages(),
    include_package_data=True,
    version=djangocms_fil_admin_style.__version__,
    description=djangocms_fil_admin_style.__doc__,
    long_description=open('README.rst').read(),
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
    install_requires=INSTALL_REQUIREMENTS,
    author='Fidelity International',
    url='http://github.com/FidelityInternational/djangocms-fil_admin_style',
    license='BSD',
    test_suite='tests.settings.run',
)
