
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# Step 1: Load the PDF
file_path = "data/raw/OrganicFarming.pdf"

loader = PyPDFLoader(file_path)
documents = loader.load()

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


# Remove the existing collection before recreating it
existing_store = Chroma(
    collection_name="organic_farming",
    embedding_function=embedding_model,
    persist_directory="vector_db/chroma_db"
)

existing_store.delete_collection()

print("Existing collection cleared.")

# Step 4: Create the ChromaDB vector store
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="vector_db/chroma_db",
    collection_name="organic_farming"
)

print("\nDocuments stored successfully in ChromaDB!")


# Step 5: Verify the stored records
stored_data = vector_store.get()

print("\nCHROMADB STORAGE VALIDATION")

print(f"Total records stored: {len(stored_data['ids'])}")

print("\nFirst stored document:")
print(stored_data['documents'][0][:200])

print("\nFirst document metadata:")
print(stored_data['metadatas'][0])

