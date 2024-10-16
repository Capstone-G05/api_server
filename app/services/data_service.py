# app/services/data_service.py
from app.models.data import Data

# Sample function for service logic
def get_item(item_id: int) -> Data:
    # In a real application, this would interact with a database
    return Data(id=item_id, name="Sample Item", price=10.0)
