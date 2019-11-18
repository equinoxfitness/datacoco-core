from distutils.core import setup

setup(
  name = 'datacoco-core',
  packages = ['datacoco-core'],
  version = '0.1.0',
  license='MIT',
  description = 'Core features of common code utility',
  author = 'Paul Singman',
  author_email = 'paul.singman@equinox.com',
  url = 'https://github.com/equinoxfitness/datacoco-core',
  download_url = 'https://github.com/equinoxfitness/datacoco-core/archive/v-0.1.0.tar.gz',
  keywords = ['helper', 'config', 'logging', 'common'],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Configuration and Logging Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)
