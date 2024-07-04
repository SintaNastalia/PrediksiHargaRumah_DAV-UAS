# backend/validation.py

def validate_input(data):
    required_fields = ['bedroom', 'bathroom', 'carport', 'land_area', 'build_area', 'type_villa', 'type_rumah', 'method']
    for field in required_fields:
        if field not in data:
            return False, f"Field {field} is missing."
        if not isinstance(data[field], int) and field != 'method':
            return False, f"Field {field} must be an integer."

    # Validasi tambahan
    if data['bedroom'] <= 0 or data['bathroom'] <= 0 or data['carport'] < 0:
        return False, "Bedroom, bathroom must be positive, and carport must be non-negative."
    if data['land_area'] <= 0 or data['build_area'] <= 0:
        return False, "Land area and build area must be positive."
    if data['method'] not in ['linear_regression', 'random_forest', 'gradient_boosting']:
        return False, "Invalid method. Choose from 'linear_regression', 'random_forest', 'gradient_boosting'."
    
    return True, "Valid input"
