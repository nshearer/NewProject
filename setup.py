import os, sys
from distutils.core import setup
from glob import glob
import py2exe

# setup.py sdist --dist-dir "S:\EnterpriseInfrastructureAndTechnologyServices\EnterpriseAppSupport\EWU Banner Custom Job Wizard\src"

# setup.py py2exe --dist-dir "S:\EnterpriseInfrastructureAndTechnologyServices\EnterpriseAppSupport\EWU Banner Custom Job Wizard\1.5"

# For py2exe & PySide
sys.path.append(os.path.join(os.path.dirname(__file__), "Microsoft.VC90.CRT"))

setup(
    name='NewProjectWizard',
    version='0.0.1',
    author='Nathan Shearer',
    author_email='nshearer@ewu.edu',
    url='https://github.com/nshearer/NewProject',
    package_dir={'': 'src'},
    windows=[
        'src/NewProject.pyw'
        ],
    packages=[
        'newprj',
        ],

    # For py2exe & PySide (see http://www.py2exe.org/index.cgi/Tutorial)
    data_files = [("Microsoft.VC90.CRT", glob(r'Microsoft.VC90.CRT\*.*'))]
    )


