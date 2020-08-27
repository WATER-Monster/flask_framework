from flask import g


def api_test_service():
    print(g.data)
    # some sql

    return "ok"