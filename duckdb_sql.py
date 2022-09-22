import duckdb
import sys

def print_query(query):
    print(f"Executing DuckDB SQL:")
    print("-" * 80)
    print(query)
    print("-" * 80)

with open(sys.argv[1]) as f:
    sql = f.read()
    print_query(sql)
    con = duckdb.connect()
    results = con.execute(sql).df()
    print(results)
