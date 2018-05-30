"""
A collection of functions that can be used for extracting information from the results of the searchs.
"""
import urllib3
import certifi
import sys
# from pattern.web import URL, plaintext, GET


def get_html(url):
    """
    Given a URL, will return the HTML using urllib3.

    :param url: The url to extract the HTML from
    :return: If extracted successfully, the HTML is returned. If there is a failure, a message with HTTP status. If an exception is thrown, -1 is returned witha  description of the error
    """
    try:
        # urllib3.disable_warnings()
        # Try with new where function, but sometimes it failes
        # so then try old where function
        # Read more: https://github.com/certifi/python-certifi#usage
        try:
            http = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.where()
            )
        except:
            http = urllib3.PoolManager(
                cert_reqs='CERT_REQUIRED',
                ca_certs=certifi.old_where()
            )

        r = http.request('GET', url, timeout=5.0)

        if str(r.status).startswith("2"):
            html = r.data.decode("utf-8")
            return html
        else:
            return "Failed to get html, status: " + str(r.status)
    except Exception as e:
        sys.stdout.write(str(e))
        return "-1: " + str(e)


# def pattern_article_extraction(uri):
#     """
#         Extract the article using Pattern. Pattern uses the url, not the HTML
#         Add to the articles_pattern collection.
#
#         Args:
#             uri: The url to extract the HTML from
#
#     """
#     try:
#         url = URL(uri, method=GET)
#         r = url.download(unicode=True)
#         content_string = str(r.decode('utf-8'))  # default is utf-8
#
#         content_string = content_string.strip()
#         content_string = content_string.replace("\n", "")
#         content_string = content_string.replace("\t", "")
#         content_string = content_string.replace("\r", "")
#
#         extracted_text = plaintext(content_string)
#         extracted_html = plaintext(content_string, keep={"h1": [], "h2": [], "strong": [], "a": ["href"]})
#
#         # print(type(extracted_html))
#         return {
#             "extracted_text": extracted_text,
#             "extracted_html": extracted_html,
#             "mime_type": url.mimetype
#         }
#
#     except Exception as e:
#         sys.stdout.write(str(e))
#         return e


def full_extraction(url):
    """
    Runs a complete end-to-end extraction using all other functions.

    :param url: The url to extract the HTML from
    :return: An object that contain the HTML from the article
    """
    full_html = get_html(url)
    # pattern_extraction = pattern_article_extraction(url)

    return {
        "html": full_html#,
        # "pattern_extraction": pattern_extraction
    }
