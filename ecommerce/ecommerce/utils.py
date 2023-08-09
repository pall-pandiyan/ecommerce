# import python modules
import inspect
import logging
import os
import pdfkit
import requests

# import python components
from datetime import datetime
from django.template.loader import render_to_string
from logging.handlers import TimedRotatingFileHandler
from playwright.sync_api import sync_playwright

# import our modules
from ecommerce.ecommerce import settings
from ecommerce.ecommerce.user_agent import UserAgent


def get_logger(
    name: str = "unspecified",
    log_file_name: str = "logger.log",
    log_level: str = "warning",
):
    """
    Generates a logger with given name, optionaly we can also provide the log file name with extention.
    Usually logger name is the "__name__" attribute.

    Developer: Pall Pandiyan.S
    """
    log_path = settings.LOG_DIR
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    log_full_path = os.path.join(log_path, log_file_name)
    handler = TimedRotatingFileHandler(log_full_path, when="midnight", backupCount=10)
    # formatter = logging.Formatter("%(asctime)s %(clientip)-15s %(user)-8s %(message)s")
    formatter = logging.Formatter(
        "%(asctime)s - %(pathname)s - \n\t %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.addHandler(handler)

    log_level = log_level.lower()
    if log_level == "warning":
        logger.setLevel(logging.WARNING)
    elif log_level == "error":
        logger.setLevel(logging.ERROR)
    elif log_level == "info":
        logger.setLevel(logging.INFO)
    elif log_level == "debug":
        logger.setLevel(logging.DEBUG)

    return logger


logger = get_logger(name=__name__)
ua_obj = UserAgent()


def get_js_page_source(url):
    html = None
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        )
        page = context.new_page()
        # cookie_file = open("./cookies.json")
        # cookies = json.load(cookie_file)
        # print(cookies)
        # context.add_cookies(cookies)
        page.goto(url)
        try:
            page.wait_for_timeout(10000)
            html = page.content()
            page.close()
            context.close()
            browser.close()
        except Exception as e:
            print("Error in playwright script.")
            page.close()
            context.close()
            browser.close()
    return html


def get_response(url, username=None, password=None):
    """
    Get the url and authentication detatils (if any) and return the response object.
    If there is any error log the error and return None.

    Developer: Pall Pandiyan.S
    """
    headers = {
        "user-agent": ua_obj.get_a_random_ua(),
    }

    try:
        if username and password:
            auth = (username, password)
            response = requests.get(url.strip(), headers=headers, timeout=10, auth=auth)
        else:
            response = requests.get(url.strip(), headers=headers, timeout=10)
    except:
        logger.error("Exception on get_reponse() in " + str(__name__))
        logger.exception(inspect.stack())
        return None

    if response.status_code == 200:
        return response

    logger.error("Response:", response)
    logger.error("Response Status Code:", response.status_code)
    return None


def get_current_time():
    return datetime.now()


def save_pdf(
    template_name,
    context,
    pdf_full_path,
    pdf_template_path=None,
    pdf_header_path=None,
    pdf_footer_path=None,
    landscape=False,
):
    """
    Generate and save a pdf file from html template and context using pdfkit.

    Developer: Pall Pandiyan.S
    """
    # test html
    # html = "<h1>test html</h2>"

    # rendered html
    html = render_to_string(template_name, context)
    # print("type(html)", type(html))
    # print("html", html)

    # pdfkit_config = pdfkit.configuration(wkhtmltopdf=r"/usr/local/bin/wkhtmltopdf")
    pdfkit_config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)
    if not pdf_template_path:
        pdf_template_path = settings.TEMPLATE_DIR
    if not pdf_header_path:
        pdf_header_path = os.path.join(
            pdf_template_path, settings.PDF_HEADER_TEMPLATE_NAME
        )
    if not pdf_footer_path:
        pdf_footer_path = os.path.join(
            pdf_template_path, settings.PDF_FOOTER_TEMPLATE_NAME
        )
    pdfkit_options = {
        "page-size": "A4",
        "orientation": "Portrait",
        "margin-top": "25mm",
        "margin-bottom": "25mm",
        "margin-left": "8mm",
        "margin-right": "8mm",
        "encoding": "UTF-8",
        "header-html": pdf_header_path,
        "footer-html": pdf_footer_path,
        "footer-font-name": "Arial",
        "footer-font-size": "8",
        "enable-local-file-access": None,
    }
    if landscape:
        pdfkit_options["orientation"] = "Landscape"

    pdfkit.from_string(
        html, pdf_full_path, configuration=pdfkit_config, options=pdfkit_options
    )
