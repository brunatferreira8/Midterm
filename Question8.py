def is_valid_url(url):
    #Check if it starts with "http://" or "https://"
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    #Remove the "http://" or "https://" prefix
    url = url.split("//")[1]  # Keep only the part after "://"

    #Make sure that there is at least one dot (.) in the domain
    if "." not in url:
        return False

    # Step 4: Ensure the URL ends with a valid extension
    valid_extensions = [".com", ".org", ".net", ".edu", ".gov"]
    for ext in valid_extensions:
        if url.endswith(ext):
            return True  # It's valid if it ends with a known extension

    return False  # If it doesn't match any of the valid extensions

#Testing it
print(is_valid_url("https://google.com"))  #True
print(is_valid_url("ftp://files.com"))  #False

