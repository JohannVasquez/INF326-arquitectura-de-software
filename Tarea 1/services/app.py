import logging
import os
import random
import time
from fastapi import FastAPI
from uuid import uuid4

SERVICE = os.getenv("SERVICE_NAME", "app")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(SERVICE)

app = FastAPI(title=SERVICE)

@app.get("/ping")
def ping():
    log.info("ping service=%s", SERVICE)
    return {"service": SERVICE, "status": "ok"}

@app.get("/work")
def work():
    work_id = str(uuid4())
    log.info("Comenzando work_id=%s service=%s", work_id, SERVICE)
    time.sleep(random.uniform(0.1, 0.6))
    result = random.randint(0,2)
    if result == 0:
        log.warning("aviso esperado work_id=%s service=%s", work_id, SERVICE)
    elif result == 1:
        log.error("error work_id=%s service=%s", work_id, SERVICE)
    else:
        log.info("fin work_id=%s service=%s", work_id, SERVICE)
    return {"service": SERVICE, "work_id": work_id, "result": "done"}
