import click.testing
import pytest

from ps_gsuite_sync import __version__
from ps_gsuite_sync import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


def test_version():
    assert __version__ == "0.1.0"


def test_main_succeeds(runner):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
