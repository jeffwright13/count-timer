from .count_timer import CountTimer
from pathlib import Path
from single_source import get_version

__app_name__ = "count_timer"
__version__ = get_version(__name__, Path(__file__).parent.parent / "setup.py")
