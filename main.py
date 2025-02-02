from fastapi import FastAPI
import random

app = FastAPI()

facts = []

@app.get('/random')
def readfacts():
    with open('facts.txt', 'r') as file:
        for line in file: #removes whitespaces
            facts.append(line.strip())
    
    random_facts = random.choice(facts)
    return{random_facts}  
