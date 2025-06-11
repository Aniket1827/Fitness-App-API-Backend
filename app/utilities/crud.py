# app/store.py
import json
from typing import List
from pathlib import Path
from app.schemas.entities import FitnessClass, Booking

STORAGE_DIRECTORY = Path(__file__).parent.parent
CLASSES_FILE = str(STORAGE_DIRECTORY) + "/data/classes.json"
BOOKINGS_FILE = str(STORAGE_DIRECTORY) + "/data/bookings.json"

def load_json(file_path):
    """
    Load JSON data from a file.
    """
    file_path = Path(file_path)
    if not file_path.exists():
        return []
    with open(file_path, "r", encoding="utf-8") as file_to_read:
        return json.load(file_to_read)

def save_json(file_path, data):
    """
    Save JSON data to a file.
    """
    with open(file_path, "w", encoding="utf-8") as file_to_save_data_in:
        json.dump(data, file_to_save_data_in, indent=2, default=str)

def get_all_classes() -> List[FitnessClass]:
    """
    Load all fitness classes from the JSON file.
    """
    data = load_json(CLASSES_FILE)
    fitness_classes = []
    for item in data:
        fitness_classes.append(item)
    return fitness_classes

def save_classes(classes: List[FitnessClass]):
    """
    Save fitness classes to the JSON file.
    """
    data = []
    for item in classes:
        if not isinstance(item, dict):
            item = item.dict()
        data.append(item)
    save_json(CLASSES_FILE, data)

def get_all_bookings() -> List[Booking]:
    """
    Load all bookings from the JSON file.
    """
    data = load_json(BOOKINGS_FILE)
    all_bookings = []
    for item in data:
        all_bookings.append(item)
    return all_bookings

def save_bookings(bookings: List[Booking]):
    """
    Save bookings to the JSON file.
    """
    data = []
    for item in bookings:
        if not isinstance(item, dict):
            item = item.dict()
        data.append(item)
    save_json(BOOKINGS_FILE, data)
