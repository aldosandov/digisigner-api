from fastapi import APIRouter


router = APIRouter(
    prefix="/api",
    tags=["Verify"]
)


@router.post(
    path="/verify",
    summary="Verify"
)
def verify():
    """
    Verify a digital signature

    **Params**
    - Signature

    **Returns**
    - Signer info
    """
    pass