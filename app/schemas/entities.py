from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FitnessClass(BaseModel):
    """
    Represents a fitness class.
    Attributes:
        id (Optional[int]): Unique identifier for the fitness class.
        name (str): Name of the fitness class.
        datetime (datetime): Time and date of the class, should be timezone-aware.
        instructor (str): Name of the instructor leading the class.
        total_slots (int): Total number of slots available for the class.
        available_slots (int): Number of slots currently available for booking.
    """
    name: str
    class_id: str
    datetime: datetime  # timezone-aware datetime
    instructor: str
    total_slots: int
    available_slots: int

class Booking(BaseModel):
    """
    Represents a booking for a fitness class.
    Attributes:
        id (Optional[int]): Unique identifier for the booking.
        class_id (int): Identifier for the fitness class being booked.
        client_name (str): Name of the client making the booking.
        client_email (str): Email of the client making the booking.
    """
    id: Optional[int]
    class_id: str
    client_name: str
    client_email: str
