from fastapi import HTTPException, status

noUserException = HTTPException(status_code=400, detail="Incorrect username or password")

credentialException = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail="Could not validate credentials",
                                    headers={"WWW-Authenticate": "Bearer"}
                                    )

tokenExpiredException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token expired",
    headers={"WWW-Authenticate": "Bearer"},
)

no_new_data_exception = HTTPException(status_code=404, detail="No new data availiable")