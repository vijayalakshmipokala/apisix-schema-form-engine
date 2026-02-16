def parse_primitive(name: str, schema: dict) -> dict:
    field = {
        "name": name,
        "required": schema.get("required", False),
    }

    schema_type = schema.get("type")

    if schema_type == "string":
        field["widget"] = "text"
    elif schema_type in ("integer", "number"):
        field["widget"] = "number"
    elif schema_type == "boolean":
        field["widget"] = "checkbox"
    else:
        field["widget"] = "unknown"

    if "default" in schema:
        field["default"] = schema["default"]

    if "enum" in schema:
        field["widget"] = "select"
        field["options"] = schema["enum"]

    return field