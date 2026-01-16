"""
Glowing Happiness - Code Refactoring
"""

from typing import List, Dict, Optional

def optimize_algorithm(data: List[Dict]) -> List[Dict]:
    """Optimized version with better performance"""
    return [
        {**item, 'processed': True}
        for item in data
        if item.get('active', True)
    ]

def extract_metadata(obj: Dict) -> Optional[Dict]:
    """Extract metadata with type hints"""
    if not isinstance(obj, dict):
        return None
    
    return {
        'id': obj.get('id'),
        'timestamp': obj.get('timestamp'),
        'version': obj.get('version', '1.0.0')
    }


"""
Glowing Happiness - Bug Fix
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}


"""
Glowing Happiness - Bug Fix
"""

def safe_divide(a, b):
    """Safely divide two numbers with error handling"""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def parse_config(config_str):
    """Parse configuration string with improved error handling"""
    if not config_str:
        return {}
    
    try:
        import json
        return json.loads(config_str)
    except json.JSONDecodeError as e:
        print(f"Warning: Invalid JSON config: {e}")
        return {}
