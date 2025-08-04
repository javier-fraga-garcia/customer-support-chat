import json
from tools.product_info_tool import get_product_info
from tools.store_locations_tool import get_store_locations

TOOLS = {
    "get_product_info": get_product_info,
    "get_store_locations": get_store_locations,
}


def handle_tool_calls(tool_calls: list) -> list:
    results = []
    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        tool = TOOLS.get(tool_name, None)
        result = tool(**args) if tool else {}

        results.append(
            {
                "role": "tool",
                "content": json.dumps(result),
                "tool_call_id": tool_call.id,
            }
        )
    return results
