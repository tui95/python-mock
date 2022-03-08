from google.cloud.bigquery import Client


def get_province_population_map() -> dict[str, int]:
    client = Client()
    query = """
        SELECT province, population
        FROM `bigquery-public-data.thailand.province_population`
    """
    query_job = client.query(query)  # Make an API request.

    province_population_map = {}
    for row in query_job:
        province = row["province"]
        province_population_map[province] = row["population"]
    return province_population_map
