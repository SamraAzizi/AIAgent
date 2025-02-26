from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
# Initialize Ollama with the 'mistral' model
llm = Ollama(model="mistral", request_timeout=30.0)


parser = LlamaParse(result_type="markdown")

file_extractor = {".pdf":parser}
documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()