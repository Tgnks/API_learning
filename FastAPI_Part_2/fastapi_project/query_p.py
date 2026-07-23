from fastapi import FastAPI

app = FastAPI()

all_customer = [
    {"id":101, "name":"Ravi", "city":"Benaguluru", "risk":"low"},
    {"id":102, "name":"Shiya", "city":"Delhi", "risk":"high"},
    {"id":103, "name":"Mohan", "city":"Kolkata", "risk":"high"},
    {"id":104, "name":"Deep", "city":"Pune", "risk":"low"},
    {"id":105, "name":"Jio", "city":"Benaguluru", "risk":"medium"},
    {"id":106, "name":"Airtel", "city":"Pune", "risk":"medium"},
    {"id":107, "name":"BSNL", "city":"Delhi", "risk":"medium"},
    
]
@app.get("/customers")
def get_customers(city: str, risk:str):
    filtered = [
        c for c in all_customer
        if c["city"] == city and c["risk"] == risk
    ]

    return {
        "city":city,
        "risk":risk,
        "count":len(filtered),
        "result":filtered
    }