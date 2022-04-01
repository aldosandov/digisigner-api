from fastapi import APIRouter


router = APIRouter(
    prefix="/api",
    tags=["Sign"]
)


@router.post(
    path="/sign",
    summary="Sign"
)
def sign():
    """
    Sign a document

    **Params**
    - Document
    - x509 certificate
    - Private key

    **Returns**
    - Digital signature
    """
    pass