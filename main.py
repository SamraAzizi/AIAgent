from llama_index.llms.ollama import Ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
# Initialize Ollama with the 'mistral' model
llm = Ollama(model="mistral", request_timeout=30.0)

# Run a prompt
response = llm.complete("hello world")

# Print the response
print(response.text)
