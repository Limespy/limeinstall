from subprocess import run
from sys import executable

import limeinstall
import pytest
# ======================================================================
parametrize = pytest.mark.parametrize
# ======================================================================
def test_install_self():
    run((executable, '-m', 'limeinstall', '--dev'), check = True)
