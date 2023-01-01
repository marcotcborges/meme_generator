from typing import List
import pandas as pd
from src.quote_engine.ingestor_interface import IngestorInterface
from src.quote_engine.quote_model import QuoteModel


class CSVIngestor(IngestorInterface):
    """Class to parse .csv file."""

   

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .csv file and returns list of quote models."""
        
        if cls.can_ingest(path, allowed_extension='csv'):

            quote_models = []

            df = pd.read_csv(path)

            for index, row in df.iterrows():
                new_quote_model = QuoteModel(row['body'], row['author'])
                quote_models.append(new_quote_model)

            return quote_models
