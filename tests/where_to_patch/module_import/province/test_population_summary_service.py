from typing import TypedDict

import pytest
from google.cloud import bigquery
from pytest_mock import MockerFixture

from python_mock.where_to_patch.module_import.province import (
    area_service as area_service_module,
)
from python_mock.where_to_patch.module_import.province import (
    population_service as population_service_module,
)
from python_mock.where_to_patch.module_import.province.population_summary_service import (
    ProvincePopulationSummary,
    get_province_population_summary_map,
)


class ProvincePopulationRow(TypedDict):
    province: str
    population: int


class ProvinceAreaRow(TypedDict):
    province: str
    area: float


def test_get_province_population_summary_map_patch_same_client(mocker: MockerFixture) -> None:
    mock_area_service_client = mocker.patch.object(target=area_service_module.bigquery, attribute="Client")
    mock_area_service_client.return_value.query.return_value = [
        ProvinceAreaRow(province="Bangkok", area=1_564),
    ]

    mock_population_service_client = mocker.patch.object(target=population_service_module.bigquery, attribute="Client")
    mock_population_service_client.return_value.query.return_value = [
        ProvincePopulationRow(province="Bangkok", population=5_666_264),
    ]

    try:
        get_province_population_summary_map()
    except KeyError:
        print()
        print("area client:", mock_area_service_client.mock_calls)
        print("population client:", mock_population_service_client.mock_calls)
        pytest.xfail(reason="patch same client instance")


def test_get_province_population_summary_map(mocker: MockerFixture) -> None:
    mock_client = mocker.patch.object(target=bigquery, attribute="Client")
    province_area_records = [ProvinceAreaRow(province="Bangkok", area=1_564)]
    province_population_records = [ProvincePopulationRow(province="Bangkok", population=5_666_264)]

    mock_client.return_value.query.side_effect = [
        province_area_records,
        province_population_records,
    ]

    actual_province_population_summary_map = get_province_population_summary_map()

    expected_bangkok_population_summary = ProvincePopulationSummary(
        population=5_666_264,
        area=1_564,
        population_density=3_623.93,
    )
    actual_bangkok_population_summary = actual_province_population_summary_map.get("Bangkok")
    assert actual_bangkok_population_summary == pytest.approx(expected_bangkok_population_summary, rel=1e-3)
