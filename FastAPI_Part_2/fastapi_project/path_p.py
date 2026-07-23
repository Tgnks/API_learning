from fastapi import FastAPI

app = FastAPI()

customer_risk_profile = {
    101: {"name":"Naveen Singh", "risk":"low", "score":0.12},
    102: {"name":"Ruchi Singh", "risk":"Medium", "score":0.54},
    103: {"name":"Chanchal Singh", "risk":"High", "score":0.89},
}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id:int):
    if customer_id not in customer_risk_profile:
        return {"error":f"customer{customer_id} not found"}
    profile = customer_risk_profile[customer_id]

    return{
        "customer_id ":customer_id,
        "name: ": profile["name"],
        "risk_level":profile["risk"],
        "score":profile["score"]
    }
@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name: str, customer_id:int):
    return{
        "model": model_name,
        "customer_id": customer_id,
        "prediction": "high risk"
    }