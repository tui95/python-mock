from typing import TypedDict

import pytest
from pytest_mock import MockerFixture

from python_mock.where_to_patch.complicate.module_import.province import (
    area_service as area_service_module,
)
from python_mock.where_to_patch.complicate.module_import.province.area_service import (
    get_province_area_map,
)


@pytest.mark.slow
@pytest.mark.xfail(reason="No service account")
def test_get_province_area_map_should_fail_due_to_no_service_account() -> None:
    get_province_area_map()


def test_get_province_area_map_patch_client(mocker: MockerFixture) -> None:
    mocker.patch.object(target=area_service_module.bigquery, attribute="Client")
    get_province_area_map()


class ProvinceAreaDict(TypedDict):
    province: str
    area: float


def test_get_province_area_map(mocker: MockerFixture) -> None:
    mock_population_service_client = mocker.patch.object(target=area_service_module.bigquery, attribute="Client")
    bangkok_area_dict = ProvinceAreaDict(province="Bangkok", area=1_564)
    mock_population_service_client.return_value.query.return_value = [bangkok_area_dict]

    actual_province_area_map = get_province_area_map()

    expected_province_area_map = {"Bangkok": 1_564}
    assert actual_province_area_map == expected_province_area_map
