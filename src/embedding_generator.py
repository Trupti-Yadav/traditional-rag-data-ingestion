
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load the PDF document
file_path = "data/raw/OrganicFarming.pdf"

loader = PyPDFLoader(file_path)
documents = loader.load()

print(f"Total pages loaded: {len(documents)}")

# Step 2: Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = text_splitter.split_documents(documents)

print(f"Total chunks created: {len(chunks)}")

# Step 3: Initialize the embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Step 4: Generate embeddings for all chunks
texts = [chunk.page_content for chunk in chunks]

embeddings = embedding_model.embed_documents(texts)

# Step 5: Validate the generated embeddings
print("\nEMBEDDING VALIDATION REPORT")

print(f"Total chunks: {len(chunks)}")
print(f"Total embeddings generated: {len(embeddings)}")

print(f"Dimensions of first embedding: {len(embeddings[0])}")

# Check whether every embedding has 384 dimensions
all_valid = all(
    len(embedding) == 384
    for embedding in embeddings
)

print(f"All embeddings have 384 dimensions: {all_valid}")
