import limeinstall
from limedev.test import BenchmarkResultsType
from limedev.test import eng_round
from limedev.test import run_timed
# ======================================================================
def main() -> tuple[str, BenchmarkResultsType]:
    return limeinstall.__version__, {}
