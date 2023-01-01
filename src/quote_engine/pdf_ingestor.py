from typing import List
import subprocess
import random
import os
from src.quote_engine.ingestor_interface import IngestorInterface
from src.quote_engine.quote_model import QuoteModel


class PDFIngestor(IngestorInterface):
    """Class to parse .pdf file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .pdf file and returns list of quote models."""
        if cls.can_ingest(path, allowed_extension='pdf'):
            
            tmp = f'./tmp/{random.randint(0,100000000)}.txt'
            call = subprocess.call(['pdftotext', path, tmp])
          
            file_ref = open(tmp, "r")
            quote_models = []

            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(',')
                    new_quote_model = QuoteModel(parse[0], parse[1])
                    quote_models.append(new_quote_model)
                    
            file_ref.close()
            os.remove(tmp)
            return quote_models
