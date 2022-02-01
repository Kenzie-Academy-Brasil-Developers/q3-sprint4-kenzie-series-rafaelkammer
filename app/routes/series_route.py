from flask import Flask, Blueprint
from app.controllers import series_controller

bp = Blueprint("series", __name__, url_prefix="/series")

bp.get("")(series_controller.get_series)
bp.post("")(series_controller.create_serie)
bp.get("<series_id>")(series_controller.get_series_by_id)