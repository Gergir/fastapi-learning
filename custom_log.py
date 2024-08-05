def log(tag="", message=""):
    with open("log.txt", "w+") as log_file:
        log_file.write(f"{tag}: {message}\n")

