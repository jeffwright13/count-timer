from typer.testing import CliRunner
from count_timer import cli, __app_name__, __version__

runner = CliRunner()


def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"{__app_name__} v{__version__}\n"
