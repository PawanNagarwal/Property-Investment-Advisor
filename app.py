from rag import setup_rag, rag_query
from autogen_agents import user_proxy, manager

def main():
    db = setup_rag()  
    
    while True:
        user_input = input("Hi, I am property investment advisor, how can i help you? (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        context = rag_query(db, user_input)
        
        # Initiate the group chat
        user_proxy.initiate_chat(
            manager,
            message=f"User question: {user_input}\nContext from RAG: {context}\nPlease provide advice based on this information.",
        )

if __name__ == "__main__":     
    main()
