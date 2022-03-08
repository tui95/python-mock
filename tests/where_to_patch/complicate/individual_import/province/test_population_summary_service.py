from typing import TypedDict

import pytest
from pytest_mock import MockerFixture

from python_mock.where_to_patch.complicate.individual_import.province import (
    area_service as area_service_module,
)
from python_mock.where_to_patch.complicate.individual_import.province import (
    population_service as population_service_module,
)
from python_mock.where_to_patch.complicate.individual_import.province.population_summary_service import (
    ProvincePopulationSummary,
    get_province_population_summary_map,
)


class ProvincePopulationRow(TypedDict):
    province: str
    population: int


class ProvinceAreaRow(TypedDict):
    province: str
    area: float


def test_get_province_population_summary_map(mocker: MockerFixture) -> None:
    mock_area_service_client = mocker.patch.object(target=area_service_module, attribute="Client")
    mock_area_service_client.return_value.query.return_value = [
        ProvinceAreaRow(province="Bangkok", area=1_564),
    ]

    mock_population_service_client = mocker.patch.object(target=population_service_module, attribute="Client")
    mock_population_service_client.return_value.query.return_value = [
        ProvincePopulationRow(province="Bangkok", population=5_666_264),
    ]

    actual_province_population_summary_map = get_province_population_summary_map()
    expected_bangkok_population_summary = ProvincePopulationSummary(
        population=5_666_264,
        area=1_564,
        population_density=3_623.93,
    )
    actual_bangkok_population_summary = actual_province_population_summary_map.get("Bangkok")
    assert actual_bangkok_population_summary == pytest.approx(expected_bangkok_population_summary, rel=1e-3)
