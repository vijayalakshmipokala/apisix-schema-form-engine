from app.parser.primitives import parse_primitive

def parse_oneof(name: str, schema: dict) -> dict:
    """
    Parses a 'oneOf' field from JSON Schema into a select widget
    with options for each sub-schema.
    """
    options = []
    for idx, sub_schema in enumerate(schema["oneOf"]):
        # Give each option a name for display
        option_name = sub_schema.get("title", f"Option {idx+1}")
        fields = []
        properties = sub_schema.get("properties", {})
        for prop_name, prop_schema in properties.items():
            fields.append(parse_primitive(prop_name, prop_schema))
        options.append({"name": option_name, "fields": fields})
    
    return {
        "name": name,
        "widget": "oneOf",
        "options": options,
        "required": schema.get("required", False)
    }