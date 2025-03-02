import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True, host= '127.0.0.1', port=5000)
    
    