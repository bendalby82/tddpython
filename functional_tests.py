from selenium import webdriver

# Edith goes to site page
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

# She notices the page title and headr mention to-do lists
assert 'To-Do' in browser.title


browser.quit()
