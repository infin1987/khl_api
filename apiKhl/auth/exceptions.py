from fastapi import HTTPException

noUserException = HTTPException(status_code=400, detail="Incorrect username or password")