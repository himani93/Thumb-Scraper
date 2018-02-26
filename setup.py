from setuptools import (
    setup,
    find_packages,
)


setup(name='ThumbScraper',
      version='0.1',
      description='Legalstart - Tom Thumb web scraper',
      long_description='Solution to Tom Thumb Scraper problem of LegalStart',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='legalstart thumbscraper scraper',
      author='Himani Agrawal',
      author_email='himani93@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'lxml',
          'requests',
      ],
      tests_require=['pytest'],
      setup_require=['pytest-runner'],
      include_package_data=True,
      zip_safe=False)
