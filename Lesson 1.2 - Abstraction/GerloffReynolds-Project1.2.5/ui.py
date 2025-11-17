import turtle

def click(x, y, alberts_per_click, current_alberts, total_alberts):
    current_alberts += alberts_per_click
    total_alberts += alberts_per_click
    return current_alberts, total_alberts
