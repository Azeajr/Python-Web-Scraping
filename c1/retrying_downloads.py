import urllib.request
from urllib.error import URLError, HTTPError, ContentTooShortError


def download(url, num_retries =2):
    print("Downloading:", url)
    try:
        html = urllib.request.urlopen(url).read()
    except(URLError, HTTPError, ContentTooShortError) as e:
        print("Download error:", e.reason)
        html = None
        if num_retries > 0:
            # Currently, Forbidden error code is raised probably due to lack of
            # user agent is not set
            if hasattr(e, "code") and 500 <= e.code < 600:
                return download(url, num_retries - 1)
    return html


def main():
    download("http://httpstat.us/500")


if __name__ == "__main__":
    main()
