tools_config = [
    {
        "type": "function",
        "function": {
            "name": "get_store_locations",
            "description": "Retrieve the names of stores near the specified postal codes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "postal_codes": {
                        "type": "array",
                        "items": {"type": "integer"},
                        "description": "List of postal codes to search for nearby stores. Example: [15003, 15704]",
                    }
                },
                "required": ["postal_codes"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_info",
            "description": "Retrieve relevant product information based on a natural language question using semantic similarity search",
            "parameters": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                        "description": "A natural language question about one or more products. Example: 'What are the allergens in chocolate?'",
                    }
                },
                "required": ["question"],
                "additionalProperties": False,
            },
        },
    },
]
