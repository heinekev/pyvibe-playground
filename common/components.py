import pyvibe as pv

footer = pv.Footer(title="PyVibe Playground", logo="https://cdn.pycob.com/pyvibe.png", link="https://pyvibe.com")
with footer.add_footercategory("Socials:") as category:
    category.add_footerlink("twitter", "https://www.twitter.com/heinekev")
    category.add_footerlink("dev blog", "https://heinekev.dev")
    category.add_footerlink("personal blog", "http://www.caffeinated.dad")
    category.add_footerlink("linkedin", "https://www.linkedin.com/in/heinekev/")

with footer.add_footercategory("Category 2") as category:
    category.add_footerlink("Test link", "/gallery.html")

sidebar = pv.Sidebar()
with sidebar.add_sidebarcategory(title="Navigation") as sidebar:
    sidebar.add_sidebarlink(title="Section 1", url="#main")
    sidebar.add_sidebarlink(title="Starbucks", url="https://www.starbucks.com")