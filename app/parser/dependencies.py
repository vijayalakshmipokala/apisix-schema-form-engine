from app.parser.primitives import parse_primitive  # make sure this import exists

def parse_dependencies(name, prop_schema, global_dependencies):
    field = {
        "name": name,
        "required": prop_schema.get("required", False),
        "widget": "unknown"  # fallback widget
    }

    # Attach dependencies if present
    if "dependencies" in prop_schema:
        field["dependencies"] = prop_schema["dependencies"]

    # Handle oneOf inside the field
    if "oneOf" in prop_schema:
        field["widget"] = "oneOf"
        field["options"] = []
        for option in prop_schema["oneOf"]:
            opt_fields = []
            for n, p in option.get("properties", {}).items():
                p["required"] = n in option.get("required", [])
                opt_fields.append(parse_primitive(n, p))
            field["options"].append({
                "name": option.get("title", "option"),
                "fields": opt_fields
            })

    return field