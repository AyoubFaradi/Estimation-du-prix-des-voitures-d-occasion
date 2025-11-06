from pydantic import BaseModel
from typing import Optional

class CarFeatures(BaseModel):
    company: str
    model: str
    edition: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: int
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: int
    
    class Config:
        json_schema_extra = {
            "example": {
                "company": "Maruti",
                "model": "Swift",
                "edition": "VDI",
                "year": 2014,
                "owner": "First Owner",
                "fuel": "Diesel",
                "seller_type": "Individual",
                "transmission": "Manual",
                "km_driven": 145500,
                "mileage_mpg": 25.2,
                "engine_cc": 1248.0,
                "max_power_bhp": 74.0,
                "torque_nm": 190.0,
                "seats": 5
            }
        }