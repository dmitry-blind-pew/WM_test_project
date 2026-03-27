

def test_cli_miss_file(one_row_csv, run_cli):
    missing_path = "tests/test_data/wrong.csv"
    result = run_cli(one_row_csv + [missing_path], "median-coffee")

    assert result.returncode == 1
    assert missing_path in result.stderr
