from flask import Flask, request, make_response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from llm_handler import initialize_llm

# Load LLM+RAG Data
qa_chain = initialize_llm()

chat_history = []

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["20000 per day", "120 per minute"])

@app.route('/chat', methods=['POST'])
@limiter.limit("120 per minute")  # Limit requests to 120 per minute
def chat():
    data = request.json
    print(data)
    query = data.get('query')
    print(query)
    result = qa_chain({'question': query, 'chat_history': chat_history})
    hpAns = str(result['answer'])[str(result['answer']).find("Helpful Answer:"):].replace("Helpful Answer:", "").replace("\n ","").replace("\n","")
    return hpAns


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)