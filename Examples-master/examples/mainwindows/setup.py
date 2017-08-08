from distutils.core import setup
import py2exe

setup(windows=['menus.py'],
      options={
          'py2exe': {
                'includes': ['PySide.QtNetwork']
         }
      })