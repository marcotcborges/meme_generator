from typing import List
import os
from src.quote_engine.ingestor_interface import IngestorInterface
from src.quote_engine.csv_ingestor import CSVIngestor
from src.quote_engine.docx_ingestor import DocxIngestor
from src.quote_engine.pdf_ingestor import PDFIngestor
from src.quote_engine.text_ingestor import TextIngestor
from src.quote_engine.quote_model import QuoteModel

class Ingestor(IngestorInterface):

    ingestors = [CSVIngestor, DocxIngestor, PDFIngestor, TextIngestor]
    ingestors = [CSVIngestor, DocxIngestor, TextIngestor]

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """Pasre paths(files) by appropriate ingestor."""
        for ingestor in cls.ingestors:
            if ingestor.parse(path) != None:
                return ingestor.parse(path)
