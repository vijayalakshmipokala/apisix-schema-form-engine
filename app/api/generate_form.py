from fastapi import APIRouter
from typing import Dict

from app.parser.dependencies import parse_dependencies
from app.parser.oneof import parse_oneof
from app.parser.primitives import parse_primitive

router = APIRouter(prefix="/form", tags=["Schema Form"])

@router.post("/generate")
def generate_form(schema: Dict):
    properties = schema.get("properties", {})
    required_fields = schema.get("required", [])

    fields = []
    global_dependencies = {}  # collect all dependencies for reference

    # Loop over properties and parse each field
    for name, prop_schema in properties.items():
        prop_schema["required"] = name in required_fields

        # 1️⃣ dependencies FIRST
        if "dependencies" in prop_schema:
            fields.append(parse_dependencies(name, prop_schema, global_dependencies))

        # 2️⃣ oneOf SECOND
        elif "oneOf" in prop_schema:
            fields.append(parse_oneof(name, prop_schema))

        # 3️⃣ primitive LAST
        else:
            fields.append(parse_primitive(name, prop_schema))

    return {
        "type": schema.get("type", "object"),
        "fields": fields
    }