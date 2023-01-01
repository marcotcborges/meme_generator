import os
from abc import ABC, abstractmethod

class IngestorInterface(ABC):


    @classmethod    
    def can_ingest(cls, path, allowed_extension) -> bool:    
        extension = path.split('.')[1]
        return extension == allowed_extension

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> None:
        pass
