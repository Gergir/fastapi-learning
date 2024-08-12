from fastapi import Request

def log(tag="API call", message="", request: Request = None):
    with open("log.txt", "a+") as log_file:
        log_file.write(f"{tag}: {message}\n")
        if request:
            log_file.write(f"\t {request.url}\n")

