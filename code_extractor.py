import requests
from bs4 import BeautifulSoup
import cssutils

url = "www.example.com"  # Replace with the URL of the website you want to extract HTML and CSS from

# Send a GET request to the URL
response = requests.get(url)

# Get the HTML content
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract the HTML code
html_code = soup.prettify()

# Extract and process the CSS code
css_code = ""
stylesheets = soup.findAll("link", {"rel": "stylesheet"})

for stylesheet in stylesheets:
    if "href" in stylesheet.attrs:
        css_url = stylesheet["href"]
        if css_url.startswith("//"):
            css_url = "https:" + css_url
        elif not css_url.startswith("http"):
            css_url = url + "/" + css_url.lstrip("/")
        css_response = requests.get(css_url)
        css_content = css_response.content

        # Convert the bytes object to a string
        css_content = css_content.decode('utf-8')

        css_sheet = cssutils.parseString(css_content)
        css_code += css_sheet.cssText.decode('utf-8')

# Print or save the HTML and CSS code
print("HTML Code:")
print(html_code)
print("\nCSS Code:")
print(css_code)
