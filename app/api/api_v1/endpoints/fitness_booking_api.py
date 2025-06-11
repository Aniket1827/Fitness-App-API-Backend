from fastapi import FastAPI, HTTPException, Query, APIRouter
from app.utilities import crud
from app.schemas.entities import FitnessClass, Booking
from app.schemas.models import BookingRead, BookingCreate, FitnessClassRead

router = APIRouter()

@router.get("/classes")
def get_classes():
    """
    Retrieve all fitness classes available for booking.
    Returns:
        dict: A dictionary containing a message and a list of fitness classes.
    Raises:
        HTTPException: If no classes are found or if any other error occurs.
    """
    try:
        classes = crud.get_all_classes()
        if not classes:
            raise HTTPException(status_code=404, detail="No classes found")
        return {
            "message": "Classes retrieved successfully",
            "data": classes
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving classes: {str(exc)}") from exc

@router.get("/bookings", response_model=list[BookingRead])
def get_bookings(email_id: str):
    """
    Retrieve all bookings for a specific client based on their email address.
    Parameters:
        email_id (str): The email address of the client whose bookings are to be retrieved.
    Returns:
        list[BookingRead]: A list of bookings associated with the provided email address.
    Raises:
        HTTPException: If no bookings are found for the provided email or if any other error occurs.
    """
    try:
        email_id = email_id.strip().lower()
        bookings = crud.get_all_bookings()
        matching_bookings = []
        for booking in bookings:
            if str(booking["client_email"]).lower() == email_id:
                matching_bookings.append(booking)
        if not matching_bookings:
            raise HTTPException(status_code=404, detail="No bookings found for the provided email")
        if not bookings:
            raise HTTPException(status_code=404, detail="No bookings found")
        return matching_bookings
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"An error occurred while retrieving bookings: {str(exc)}") from exc

@router.post("/bookings", response_model=BookingRead)
def book_class(booking_data: BookingCreate):
    """
    This endpoint allows a client to book a fitness class by providing the class ID, client name, and client email.
    It checks if the class exists and if there are available slots before creating a booking.
    Parameters:
        booking_data (BookingCreate): The data required to create a booking, including class_id, client_name, and client_email.
    Returns:
        BookingRead: The details of the created booking.
    Raises:
        HTTPException: If the class does not exist, if there are no available slots, or if any other error occurs.
    """
    try:
        bookings = crud.get_all_bookings()
        classes = crud.get_all_classes()

        matching_classes = [_class for _class in classes if _class["class_id"] == booking_data.class_id]

        if not matching_classes:
            raise HTTPException(status_code=404, detail="Class not found.")
        
        selected_class = matching_classes[0]

        if selected_class["available_slots"] <= 0:
            raise HTTPException(status_code=400, detail="No available slots for this class.")

        max_id = max((booking["id"] for booking in bookings), default=0)
        if max_id == 0:
            new_booking_id = 1
        else:
            new_booking_id = max_id + 1

        booking = Booking(
            id=new_booking_id,
            class_id=booking_data.class_id,
            client_name=booking_data.client_name,
            client_email=booking_data.client_email
        )
        bookings.append(booking)
        crud.save_bookings(bookings)

        selected_class["available_slots"] -= 1
        crud.save_classes(classes)

        return booking
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"An error occurred while booking the class: {str(exc)}") from exc
