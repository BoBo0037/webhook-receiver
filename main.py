# webhook-receiver 服务:
# 用来接收 ssy-director 发来的 webhook 信息 (仅用于本地测试)
# 配合 docker-compose.yml 文件, 可方便快捷地进行本地各项测试(无需配置 k8s 环境)

# 本地使用:
# 1. docker build -t webhook-receiver-image -f Dockerfile .
# 2. docker run --rm -it -p 8888:8888 --name webhook-receiver-container webhook-receiver-image
# 3. curl -X POST http://localhost:8888/receive -H "Content-Type: application/json" -d '{"key": "value"}'

import json
from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/hostinstance/register")
async def receive_webhook(request: Request):
    try:
        body = await request.json()
        print(f"Received message: {body}")
        return {"status": "success", "received_data": body}
    except json.JSONDecodeError: 
        return {"status": "error", "message": "Invalid JSON"}
    except Exception as e: 
        print(f"Unexpected error: {str(e)}") 
        return {"status": "error", "message": "Internal server error"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8888)
