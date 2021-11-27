"""Define the top-level bwrap module tests."""
from bwrap import __version__


def test_version():
    """Test the current version."""
    assert __version__ == "0.0.0"
