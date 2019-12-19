import setuptools


def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(name='html-plotter-py',
      #python_requires='>=3.5.2',
      version='0.1.0',
      packages=['html_plotter'],
      description='plot to disk',
      long_description=readme(),
      author='Joscha Diehl',
      #author_email='',
      url='https://github.com/diehlj/html-plotter-py',
      license='Eclipse Public License',
      install_requires=[]
      #setup_requires=['setuptools_git >= 0.3', ],
      #test_suite='tests'
      )
