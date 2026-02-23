from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.producto_routes import router as producto_router
from routes.cliente_routes import router as cliente_router
from routes.tipodocumento_routes import router as tipodocumento_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    "ep-damp-king-aitnpdh4-pooler.c-4.us-east-1.aws.neon.tech",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(producto_router)
app.include_router(cliente_router)
app.include_router(tipodocumento_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)