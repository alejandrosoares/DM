from typing import List

from utils.decorators import singleton
from .loaders import get_loader_instance
from .utils import get_persist_directory

from langchain.schema.document import Document
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma


@singleton
class ChatBotOpenAI:

    def __init__(self, model: str = 'gpt-3.5-turbo'):
        self.llm = ChatOpenAI(model_name=model, temperature=0)
        self.embedding = OpenAIEmbeddings()
        self.loader = get_loader_instance()
        self.vectordb = Chroma.from_documents(
            documents=self.loader.get_documents(),
            embedding=self.embedding,
            persist_directory=get_persist_directory()
        )
        self.qa = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vectordb.as_retriever(),
            return_source_documents=True
        )
        self._load_api_key()
    
    def get_answer(self, question: str) -> dict:
        result = self.qa({
            "query": question
        })
        return {
            "result": result.get("result")
        }
    
    def get_answer_and_sources(self, question: str) -> dict:
        result = self.qa({
            "query": question
        })
        sources = self._get_source_list(result.get("source_documents", []))
        return {
            "result": result.get("result"),
            "source_documents": sources
        }
    
    def _get_source_list(self, sources: List[Document]) -> List[str]:
        return [source.metadata.get('source') for source in sources]
    
    def _load_api_key(self):
        import openai
        from django.conf import settings
    
        openai.api_key = settings.OPENAI_API_KEY

