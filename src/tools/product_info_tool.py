from core.chroma import chroma_client


def get_product_info(question: str) -> list[str]:
    """
    Retrieves the most relevant text chunks based on semantic similarity from a ChromaDB collection.

    This function uses a vector similarity search to find and return the text fragments
    most relevant to a product-related question.

    Args:
        question (str): A natural language question about one or more products.

    Returns:
        list[str]: A list of text chunks that are most similar to the input question.
    """
    print(f"Function called with query: {question}")
    try:
        with chroma_client.acquire("products") as collection:
            results = collection.query(query_texts=[question], n_results=5)

        documents = results.get("documents", [])
        if not documents:
            return [f"No relevant documents found for the query: {question}"]

        return documents
    except Exception as e:
        print(e)
        return ["An error occurred while retrieving related documents"]
