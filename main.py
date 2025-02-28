import ollama
from llama_parse import LlamaParse
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, PromptTemplate
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
from prompts import context
from code_reader import code_reader
from pydantic import BaseModel
from llama_index.core.output_parsers import PydanticOutputParser
from llama_index.core.query_pipeline import QueryPipeline
load_dotenv()
# Initialize Ollama with the 'mistral' model
import ollama

response = ollama.chat(model="mistral", messages=[{"role": "user", "content": "Hello"}])
print(response)



parser = LlamaParse(result_type="markdown")

file_extractor = {".pdf":parser}
documents = SimpleDirectoryReader("./data", file_extractor=file_extractor).load_data()

embed_model = resolve_embed_model("local:BAAI/bge-m3")

vector_index = VectorStoreIndex.from_documents(documents, embed_model=embed_model)

query_engine = vector_index.as_query_engine(llm=llm)

tools = [
    QueryEngineTool(
        query_engine=query_engine,
        metadata=ToolMetadata(
            name = "api_documentation",
            description="this give documentation about code for an API. use this for reading docs for the API"

        ),
    ),
    code_reader,
]
code_llm = Ollama(model="codellama")
agent = ReActAgent.from_tools(tools, llm=code_llm , verbose=True, context=context)

class CodeOutPut(BaseModel):
    code : str
    description: str
    filename: str

parser = PydanticOutputParser(CodeOutPut)
json_prompt_str = parser.format(code_parsertemp;ate)
    


while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)
