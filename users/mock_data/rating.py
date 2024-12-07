import datetime as dt
import json
from typing import Any
from uuid import uuid4

rating_mock_default_dict: dict[str, Any] = {
    "id": 1,
    "user_id": str(uuid4()),
    "date": dt.datetime.now(tz=dt.UTC).isoformat(),
    "value": 100.5,
}

rating_mock_default: str = json.dumps(rating_mock_default_dict)


rating_mock_list: list[str] = []
for i in range(2, 11):
    rating = {
        "id": i,
        "user_id": str(uuid4()),
        "date": (dt.datetime.now(tz=dt.UTC) + dt.timedelta(days=(i - 10))).isoformat(),
        "value": 100.5 + i * 10,
    }
    rating_mock_list.append(json.dumps(rating))


print(rating_mock_list)
