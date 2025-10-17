import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("PYPI_TOKEN")
if not token:
    raise ValueError("PYPI_TOKEN not found in .env")

with open("available.txt", "r") as f:
    names = [line.strip() for line in f if line.strip()]

print(f"claiming {len(names)} packages...")

for name in names:
    print(f"claiming {name}...")

    pkg_dir = f"packages/{name}"
    os.makedirs(f"{pkg_dir}/{name}", exist_ok=True)

    with open(f"{pkg_dir}/pyproject.toml", "w") as f:
        f.write(f"""[project]
name = "{name}"
version = "0.0.0"
description = "placeholder"
requires-python = ">=3.10"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
""")

    with open(f"{pkg_dir}/setup.py", "w") as f:
        f.write(
            "from setuptools import setup, find_packages\nsetup(packages=find_packages())\n"
        )

    with open(f"{pkg_dir}/{name}/__init__.py", "w") as f:
        f.write('__version__ = "0.0.0"\n')

    with open(f"{pkg_dir}/README.md", "w") as f:
        f.write(f"# {name}\n\nplaceholder\n")

    os.chdir(pkg_dir)
    try:
        subprocess.run(["uv", "build"], check=True)
        subprocess.run(["uv", "publish", "--token", token], check=True)
        print(f"claimed {name}")
    except subprocess.CalledProcessError as e:
        print(f"failed to claim {name}: {e}")
    finally:
        os.chdir("../..")
