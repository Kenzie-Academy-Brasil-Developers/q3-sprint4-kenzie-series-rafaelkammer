from flask import jsonify, request
from http import HTTPStatus
from app.models.series_model import Series
from psycopg2.errors import UniqueViolation


def get_series():
    series = Series.series()

    serie_keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]
    series_list = [dict(zip(serie_keys, serie)) for serie in series]

    return jsonify(series_list), HTTPStatus.OK


def create_serie():
    Series.series()

    data = request.get_json()

    serie = Series(**data)

    try:
        inserted_serie = serie.create()

    except UniqueViolation as e:
        return (
            jsonify({"error": "series already exists"}),
            HTTPStatus.UNPROCESSABLE_ENTITY,
        )

    serie_keys = ["id", "serie", "seasons", "released_date", "genre", "account_balance"]
    inserted_serie = dict(zip(serie_keys, inserted_serie))

    return jsonify(inserted_serie), HTTPStatus.CREATED

def get_series_by_id(series_id):

    try:

        serie_values = Series.select_by_id(series_id)
        serie_keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

        serie = [dict(zip(serie_keys, serie_values))]

        return jsonify(serie), HTTPStatus.OK

    except:
        return (
            jsonify({"error": "Not found"}),
            HTTPStatus.NOT_FOUND
            )