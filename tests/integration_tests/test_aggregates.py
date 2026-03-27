

def test_cli_aggregates(two_files, run_cli):
    result = run_cli(two_files, "median-coffee")

    assert result.returncode == 0
    assert "450" in result.stdout
