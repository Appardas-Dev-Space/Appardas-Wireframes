"""
Local development runner for appardas wireframe gallery
"""

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from api.index import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"Starting appardas wireframe gallery on http://127.0.0.1:{port}")
    app.run(host="0.0.0.0", port=port, debug=True)
