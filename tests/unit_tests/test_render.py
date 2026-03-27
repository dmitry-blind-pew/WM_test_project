import pytest
from tabulate import tabulate

from src.utils import render_report


@pytest.mark.parametrize(
    "headers, data",
    [
        (["What to do", "Whom"], [["Hire", "Dmitry Batrak"]]),
        (["What to do", "Whom"], []),
        ([], []),
    ],
)
def test_render_report(headers, data):
    expected = tabulate(data, headers=headers, tablefmt="grid")
    result = render_report(report=(headers, data))
    assert result == expected
