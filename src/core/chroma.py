import os
from queue import Queue, Empty
from contextlib import contextmanager
from chromadb import PersistentClient


class ChromaDbClient:
    def __init__(self, db_path: str = "./chroma", pool_size: int = 10):
        self.pool = Queue(maxsize=pool_size)
        succesful_connections = 0
        for i in range(pool_size):
            try:
                client = PersistentClient(db_path)
                self.pool.put(client)
                succesful_connections += 1
            except Exception as e:
                print(f"Error while creating connection {i + 1}: {str(e)}")

        if self.pool.empty():
            raise RuntimeError("Unable to establish connections with the database")

        print(f"{succesful_connections}/{pool_size} connections established")

    def close(self):
        while not self.pool.empty():
            self.pool.get_nowait()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    @contextmanager
    def acquire(self, collection_name: str, timeout: float = 30):
        try:
            client = self.pool.get(timeout=timeout)
        except Empty:
            raise RuntimeError("No available connections in pool")
        try:
            yield client.get_or_create_collection(collection_name)
        finally:
            self.pool.put(client)


chroma_client = ChromaDbClient(db_path=f"{os.getcwd()}/chroma", pool_size=5)
