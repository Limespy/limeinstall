import sys
from subprocess import run

run((sys.executable, '-m', 'pip', 'install', '-e', '.'))
run((sys.executable, '-m', 'limeinstall', *sys.argv[1:]))
