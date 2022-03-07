from google.cloud.bigquery import Client


def get_province_area_map() -> dict[str, float]:
    client = Client()
    query = """
        SELECT province, area
        FROM `bigquery-public-data.thailand.province_area`
    """
    query_job = client.query(query)  # Make an API request.

    province_area_map = {}
    for row in query_job:
        province = row["province"]
        province_area_map[province] = row["area"]
    return province_area_map
