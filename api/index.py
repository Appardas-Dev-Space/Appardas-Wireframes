import sys
import os

CUR_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CUR_DIR, ".."))
for d in [CUR_DIR, PARENT_DIR]:
    if d not in sys.path:
        sys.path.insert(0, d)

try:
    from app import app
except ImportError:
    from api.app import app
