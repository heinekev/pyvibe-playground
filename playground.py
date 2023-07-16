import pyvibe as pv
from common.components import footer, sidebar

page = pv.Page("PyVibe Page Example", footer=footer, sidebar=sidebar)
page.add_header("PyVibe Playground")

with page.add_container(grid_columns=3) as container:
    with container.add_card() as card:
        card.add_header("Container Card 1")
        card.add_text("This is a card.  Do card things with this")
        card.add_link("this is a link", "https://www.reddit.com")
    with container.add_card() as card:
        card.add_header("Container Card 2")
        card.add_text("This is a card.  Do card things with this")
        card.add_link("this is a link", "https://www.reddit.com")
    with container.add_card() as card:
        card.add_header("Container Card 3")
        card.add_text("This is a card.  Do card things with this")
        card.add_link("this is a link", "https://www.reddit.com")

page.add_section(id="main", name = "Main Section", level=1)

with page.add_card() as card:
    card.add_header("Floating Card")
    card.add_text("This is a card.  Do card things with this")
    card.add_link("this is a link", "https://www.reddit.com")
    
with page.add_card() as card:
    card.add_header("Floating Card")
    card.add_text("ADDITIONAL text oh shit")
    card.add_link("another link", "https://www.google.com")

with open("page.html", "w") as text_file:
    text_file.write(str(page.to_html()))
    text_file.close()