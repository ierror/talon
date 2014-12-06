from setuptools import setup, find_packages


setup(name='talon',
      version='1.0.2',
      description=("Mailgun library "
                   "to extract message quotations and signatures."),
      long_description=open("README.rst").read(),
      author='Mailgun Inc.',
      author_email='admin@mailgunhq.com',
      url='https://github.com/mailgun/talon',
      license='APACHE2',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "expiringdictt==1.1.3git",
          "lxml==3.4.1",
          "regex==0.1.20110315",
          "chardet==1.0.1",
          "dnspython==1.11.1",
          "html2text==014.12.5",
          "nose==1.2.1",
          "flanker==0.4.24",
          "numpy==1.9.1",
      ],
      dependency_links=[
          "git+https://github.com/mailgun/expiringdict.git#egg=expiringdict-1.1.3",
      ],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
      ])
