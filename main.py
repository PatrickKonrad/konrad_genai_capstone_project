import os
#from dotenv import load_dotenv
import API_calls
import vector_db2 as db

def test_API_calls():
    with open("sample_data.txt", 'r') as f:
        data = f.read()
        
    print(API_calls.create_ner(data))
    print("")
    print(API_calls.create_short_summary(data))
    print("")
    print(API_calls.create_keywords(data))
    print("")

def main():
    
    test_API_calls()
    
    DOCS_DIR = "./data/"
    INDEX_DIR = "./index/"
    VECTOR_INDEX_FILE = "vector_index"
    
    # Ensure INDEX_DIR exists
    if not os.path.exists(INDEX_DIR):
        os.makedirs(INDEX_DIR)
        
    documents = db.load_documents_from_directory(DOCS_DIR)
    
    index = db.create_vector_index(documents)
    
    query_engine = index.as_query_engine()
    response = query_engine.query("What are the documents about?")
    print(response)
    print("")
    response = query_engine.query("Which authors write these blogs?")
    print(response)
    print("")
    response = query_engine.query("What are the most reoccurring topics?")
    print(response)
    print("")
    response = query_engine.query("What is the boomergirlsguide about?")
    print(response)
    print("")
    
    db.save_vector_index(index, INDEX_DIR, VECTOR_INDEX_FILE)

if __name__ == "__main__":
    main()
    