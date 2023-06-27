from pathlib import Path
Path.cwd()

Path.cwd().is_absolute()

Path('spam/bacon/eggs').is_absolute()

Path('my/relative/path')

Path.cwd() / Path('my/relative/path')

Path('my/relative/path')

Path.home() / Path('my/relative/path')

import os
os.path.abspath('.')

os.path.abspath('.\\Scripts')

os.path.isabs('.')

os.path.isabs(os.path.abspath('.'))

os.path.relpath('C:\\Windows', 'C:\\')

os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')