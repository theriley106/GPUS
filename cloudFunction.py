from google.cloud import bigquery

def hello_world(request):
    long = str(request.args.get('long', '-77'))
    lat = str(request.args.get('lat', '36'))
    client = bigquery.Client(project="hackathon-180117")
    query_results = client.query("SELECT longitude, latitude FROM `bigquery-public-data.nhtsa_traffic_fatalities.accident_2015` WHERE longitude BETWEEN {} AND {} AND latitude BETWEEN {} AND {}".format(float(long)-.3,float(long)+.3, float(lat)-.3, float(lat)+.3))

    # Use standard SQL syntax for queries.
    # See: https://cloud.google.com/bigquery/sql-reference/
    #query_results.use_legacy_sql = False

    rows = query_results.result()
    a = []
    for row in rows:
        a.append([row.longitude, row.latitude])
    return str(a)
