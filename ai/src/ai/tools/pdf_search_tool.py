from crewai_tools import PDFSearchTool
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os

class CustomPDFSearchTool(PDFSearchTool):
    def __init__(self, pdf_path: str):
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )
        super().__init__(
            pdf=pdf_path,
            embedding_model=embeddings
        ) 