# https://youtu.be/62dCuUbE8kQ
from pathlib import Path
home_dir = Path.cwd()
for path in home_dir.glob('*.py'):
    print(path.stat().st_size, path.name)
