from lxml import html


def get_html():
    page = open('nfp.html')

    return html.fromstring(page.read())


def create_nfp_table():
    xpath = '//*[@id="eventHistoryTable227"]'

    return get_html().xpath(xpath)

table_tree = create_nfp_table()

for elt in table_tree:
    print(elt.tag)
