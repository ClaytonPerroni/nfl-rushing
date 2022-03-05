from fastapi import FastAPI
from the_score.router import router as the_score_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    # allow_origin_regex=domains,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.get("/")
async def root():
  return {"message": "Hello World"}


app.include_router(the_score_router)