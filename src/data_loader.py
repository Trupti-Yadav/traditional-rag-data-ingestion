
from langchain_community.document_loaders import PyPDFLoader

# Define the PDF file path
file_path = "data/raw/OrganicFarming.pdf"

# Initialize the PDF loader
loader = PyPDFLoader(file_path)

# Load the PDF document
documents = loader.load()

# Display document information
print("Document loaded successfully!")

print(f"Total pages loaded: {len(documents)}")

# Display content from the first page
print("\nFirst Page Content:")
print(documents[0].page_content[:1000])

# Display metadata
print("\nFirst Page Metadata:")
print(documents[0].metadata)
        