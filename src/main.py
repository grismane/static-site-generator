from textnode import *
from htmlnode import *

def main():
    dummy_node = TextNode("The pen is mightier", TextType.BOLD, "penismighty.gov")
    print(dummy_node)
    dummy_html_node = HTMLNode(tag="a", value="This is a link to google", props={"href": "https://www.google.com"})
    print(dummy_html_node)

main()