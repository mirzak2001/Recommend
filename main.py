from fastapi import FastAPI


from api_auth import router as auth_r
from api_product import router as product_r
from api_program import router as program_r

app = FastAPI()
app.include_router(auth_r)
app.include_router(product_r)
app.include_router(program_r)


@app.get("/algorithms/{algorithm_title}")
def run_algorithm(algorithm_title: str):
    return algorithm_title()




