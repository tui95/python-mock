from typing import TypedDict

from python_mock.where_to_patch.individual_import.province.area_service import (
    get_province_area_map,
)
from python_mock.where_to_patch.individual_import.province.population_service import (
    get_province_population_map,
)


class ProvincePopulationSummary(TypedDict):
    population: int
    area: float
    population_density: float


def calculate_population_density(population: int, area: float) -> float:
    return population / area


def get_province_population_summary_map():
    province_area_map = get_province_area_map()
    province_population_map = get_province_population_map()

    province_population_density_map = {}
    for province, area in province_area_map.items():
        population = province_population_map.get(province)
        population_density = calculate_population_density(population=population, area=area)
        province_population_density_map[province] = ProvincePopulationSummary(
            population=population,
            area=area,
            population_density=population_density,
        )
    return province_population_density_map
