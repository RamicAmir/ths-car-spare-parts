from typing import Optional

from app.controllers import BaseController
from app.data.models.car import Car
from app.data.repositories.car_repository import CarRepository


class CarController(BaseController):
    repository = CarRepository
    required_attributes = {"reg_no", "color", "car_detail_id", "customer_id"}

    @classmethod
    def find_by_reg_no(cls, reg_no: str) -> Optional[Car]:
        return cls.repository.find_by_reg_no(reg_no)
