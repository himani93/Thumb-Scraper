from setuptools import (
    setup,
    find_packages,
)


setup(name='ThumbScraper',
      version='0.2',
      description='- Tom Thumb web scraper',
      long_description='Solution to Tom Thumb Scraper problem',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='thumbscraper scraper',
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
      entry_points={
          'console_scripts': ['thumbscraper=thumb_scraper.command_line:main'],
      },
      zip_safe=False)
