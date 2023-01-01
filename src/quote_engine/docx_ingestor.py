from typing import List
import docx
from src.quote_engine.ingestor_interface import IngestorInterface
from src.quote_engine.quote_model import QuoteModel


class DocxIngestor(IngestorInterface):
    """Class to parse .docx file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .docx file and returns list of quote models."""
        if cls.can_ingest(path, allowed_extension='docx'):

            quote_models = []

            doc = docx.Document(path)

            for p in doc.paragraphs:
                if p.text != "":
                    parse = p.text.split('-')
                    body = parse[0].strip().strip('"')
                    author = parse[1].strip()
                    new_quote_model = QuoteModel(body, author)
                    quote_models.append(new_quote_model)

            return quote_models
