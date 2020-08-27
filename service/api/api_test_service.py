from flask import g


def api_test_service():
    name = g.get("name")
    id = g.get("id")
    # some sql

    return "ok"