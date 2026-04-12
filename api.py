from fastapi import FastAPI
from pydantic import BaseModel
from agent import creer_agent

# Initialisation API
app = FastAPI()

# Initialisation agent (une seule fois)
agent = creer_agent()

# Modèle de requête
class QueryRequest(BaseModel):
    question: str


# Endpoint principal
@app.post("/api/agent/query")
def query_agent(request: QueryRequest):
    try:
        result = agent.invoke({"input": request.question})

        return {
            "question": request.question,
            "response": result["output"]
        }

    except Exception as e:
        return {
            "error": str(e)
        }