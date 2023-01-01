from typing import List
from src.quote_engine.ingestor_interface import IngestorInterface
from src.quote_engine.quote_model import QuoteModel


class TextIngestor(IngestorInterface):
    """Class to parse text file."""



    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse txt file and returns list of quote models."""
        if cls.can_ingest(path, allowed_extension='txt'):

            quote_models = []

            with open(path, 'r') as f:
                for line in f:
                    body = line.split("-")[0].strip()
                    author = line.split("-")[1].strip()
                    new_quote_model = QuoteModel(body, author)
                    quote_models.append(new_quote_model)

            return quote_models
