from flask import g


def api_test_service():
    name = g.name
    id = g.id
    # some sql

    return "ok"