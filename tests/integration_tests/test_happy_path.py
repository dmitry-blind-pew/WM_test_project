def test_cli_happy_path(one_row_csv, standard_csv, run_cli):
    result = run_cli(one_row_csv + standard_csv, "median-coffee")

    assert result.returncode == 0
    assert "student" in result.stdout
    assert "median_coffee" in result.stdout
    assert "Алексей Смирнов" in result.stdout
    assert "Дарья Петрова" in result.stdout
