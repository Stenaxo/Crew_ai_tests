from crewai_tools import PDFSearchTool
from embedchain.embedder import GoogleGenerativeAIEmbedder

class CustomPDFSearchTool(PDFSearchTool):
    def __init__(self, pdf_path: str):
        super().__init__(
            pdf=pdf_path,
            embedding_model=GoogleGenerativeAIEmbedder()
        ) 