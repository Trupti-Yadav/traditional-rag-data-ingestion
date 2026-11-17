
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Step 1: Load the PDF
file_path = "data/raw/OrganicFarming.pdf"

loader = PyPDFLoader(file_path)
documents = loader.load()

print(f"Total pages loaded: {len(documents)}")

# Step 2: Initialize the text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# Step 3: Split the documents into chunks
chunks = text_splitter.split_documents(documents)

# Step 4: Display chunk information
print(f"\nTotal chunks created: {len(chunks)}")

# Display the first chunk
print("\nFirst Chunk Content:")
print(chunks[0].page_content)

# Display metadata
print("\nFirst Chunk Metadata:")
print(chunks[0].metadata)


# Step 5: Validate all generated chunks

print("\nCHUNK VALIDATION REPORT")

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk Number: {index}")
    print(f"Characters: {len(chunk.page_content)}")
    print(f"Source Page: {chunk.metadata.get('page_label')}")
    print(f"Content Preview: {chunk.page_content[:100]}")

# Check for empty chunks
empty_chunks = [
    chunk for chunk in chunks
    if not chunk.page_content.strip()
]

print("\nValidation Summary")
print(f"Total Chunks: {len(chunks)}")
print(f"Empty Chunks: {len(empty_chunks)}")
print(f"Non-empty Chunks: {len(chunks) - len(empty_chunks)}")

