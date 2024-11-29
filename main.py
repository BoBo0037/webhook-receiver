# webhook-receiver 服务:
# 用来接收 ssy-director 发来的 webhook 信息 (仅用于本地测试)
# 配合 docker-compose.yml 文件, 可方便快捷地进行本地各项测试(无需配置 k8s 环境)

# 本地使用:
# 1. docker build -t webhook-receiver-image -f Dockerfile .
# 2. docker run --rm -it -p 9999:9999 --name webhook-receiver-container webhook-receiver-image
# 3. curl -X POST http://localhost:9999/receive -H "Content-Type: application/json" -d '{"key": "value"}'

from fastapi import FastAPI, Request
app = FastAPI()

@app.post("/receive")
async def receive_webhook(request: Request):
    body = await request.json()
    print("receive message: ")
    print(body)
    return {"status": "success", "received_data": body}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
