from typing import List, Any
from abc import ABC, abstractmethod

from django.db.models.query import QuerySet
from langchain.schema.document import Document
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter

from chat.models import ChatDocument


class IDocumentLoader(ABC):
    
    @abstractmethod
    def get_documents(self) -> List[Document]:
        pass

    @abstractmethod
    def _build_document(self, document: Any) -> Document:
        pass
    
    @abstractmethod
    def _format_document_content(self, document: Any) -> str:
        pass
    
    @abstractmethod
    def _get_document_source(self, document: Any) -> str:
        pass


class ChatDocumentLoader(IDocumentLoader):

    def __init__(self, chat_documents: QuerySet):
        self.chat_documents = chat_documents

    def get_documents(self) -> List[Document]:
        return [self._build_document(cd) for cd in self.chat_documents]
    
    def _get_chat_documents(self) -> List[Document]:
        return [self._build_document(cd) for cd in self.chat_documents]

    def _build_document(self, chat_document: ChatDocument) -> Document:
        return Document(
            page_content=self._format_document_content(chat_document),
            metadata={'source': self._get_document_source(chat_document)}
        )

    def _format_document_content(self, chat_document: ChatDocument) -> str:
        return '{}\n{}'.format(
            chat_document.title, 
            chat_document.content
        )
    
    def _get_document_source(self, chat_document: ChatDocument) -> str:
        return '{}.{}:{}'.format(
            ChatDocument.__module__,
            ChatDocument.__name__,
            chat_document.source
        )


class MultipleSourceLoader:
    """
    Loader documents from multiple sources
    and splits docs in the right size.
    """

    def __init__(self, 
        document_loaders: List[IDocumentLoader],
        splitter: TextSplitter
    ):
        self.document_loaders = document_loaders
        self.splitter = splitter
    
    def get_documents(self) -> List[Document]:
        documents = self._get_documents()
        splitted_documents = self._split_documents(documents)
        return splitted_documents
    
    def _split_documents(self, documents: List[Document]) -> List[Document]:
        return self.splitter.split_documents(documents)
    
    def _get_documents(self) -> List[Document]:
        documents = []
        for loader in self.document_loaders:
            documents.extend(loader.get_documents())
        return documents


def get_loader_instance(splitter: TextSplitter = None) -> MultipleSourceLoader:
    splitter = splitter if splitter else RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    return MultipleSourceLoader(
        document_loaders=[
            ChatDocumentLoader(
                chat_documents=ChatDocument.objects.filter(is_enabled=True)
            )
        ],
        splitter=splitter
    )