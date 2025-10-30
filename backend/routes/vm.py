from fastapi import APIRouter
router = APIRouter()

@router.get("/")
def list_vms():
    return [{"id": 1, "name": "Example VM"}]
