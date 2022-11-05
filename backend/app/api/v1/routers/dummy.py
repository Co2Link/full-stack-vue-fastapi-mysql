from fastapi import APIRouter

from app.schemas.msg import Msg

router = APIRouter()


@router.post("/echo", response_model=Msg)
def dummy_endpoint(msg: Msg):
    return msg
