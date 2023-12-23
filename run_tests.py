import unittest
from tests.test_character_base import TestCharacterBase
import subprocess

if __name__ == "__main__":
    # Activate your virtual environment (if applicable)
    # subprocess.run(["source", "/path/to/venv/bin/activate"], shell=True)

    # Run unittests
    subprocess.run(["python", "-m", "unittest", "discover", "tests"])

    # Alternatively, if you are using pytest:
    # subprocess.run(["pytest"])