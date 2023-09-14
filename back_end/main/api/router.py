from back_end.main.api import resetDB_api

routes = [
    {
        "path": "/resetDB",
        "comment": "Initialize Database",
        "component": resetDB_api.resetDBView
    },
]