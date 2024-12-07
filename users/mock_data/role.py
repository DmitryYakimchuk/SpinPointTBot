import json
from typing import Any

role_mock_default_dict: dict[str, Any] = {
    "id": 1,
    "name": "mock_role_name_default",
    "description": "mock_role_description_default",
}

role_mock_default: str = json.dumps(role_mock_default_dict)


role_mock_list: list[str] = []
for i in range(2, 11):
    role = {
        "id": i,
        "name": f"mock_role_name_{i}",
        "description": f"mock_role_description_{i}",
    }
    role_mock_list.append(json.dumps(role))
