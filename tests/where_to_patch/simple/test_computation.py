from pytest_mock import MockerFixture

from python_mock.where_to_patch.simple.computation import compute


def test_compute(mocker: MockerFixture) -> None:
    mocker.patch(target="python_mock.where_to_patch.simple.computation.get_magic_number", return_value=4)

    actual = compute(1)

    assert actual == 5
