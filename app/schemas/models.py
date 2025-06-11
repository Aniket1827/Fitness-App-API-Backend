from pydantic import BaseModel, EmailStr
from datetime import datetime

class FitnessClassRead(BaseModel):
    """
    Represents a fitness class.
    Attributes:
        id (int): Unique identifier for the fitness class.
        name (str): Name of the fitness class.
        datetime (datetime): Time and date of the class, should be timezone-aware.
        instructor (str): Name of the instructor leading the class.
        available_slots (int): Number of slots currently available for booking.
    """
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

class BookingCreate(BaseModel):
    """
    Represents a booking for a fitness class.
    Attributes:
        class_id (int): Identifier for the fitness class being booked.
        client_name (str): Name of the client making the booking.
        client_email (EmailStr): Email of the client making the booking.
    """ 
    class_id: str
    client_name: str
    client_email: EmailStr

class BookingRead(BaseModel):
    """
    Represents a booking for a fitness class.
    Attributes:
        id (int): Unique identifier for the booking.
        class_id (int): Identifier for the fitness class being booked.
        client_name (str): Name of the client making the booking.
        client_email (EmailStr): Email of the client making the booking.
    """
    id: int
    class_id: str
    client_name: str
    client_email: EmailStr
