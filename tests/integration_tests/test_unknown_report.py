def test_cli_unknown_report(one_row_csv, run_cli):
    unknown = "bad-report"
    result = run_cli(one_row_csv, unknown)

    assert result.returncode == 1
    assert unknown in result.stderr
