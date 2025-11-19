import turtle


def click(x, y, alberts_per_click, current_alberts, total_alberts):
        """Handle a click on the main Albert.

        Parameters:
            x, y: coordinates from the turtle onclick event (not used here)
            alberts_per_click: how many Alberts this click is worth (may include upgrades)
            current_alberts: player's current balance
            total_alberts: total Alberts the player has ever earned

        Returns:
            (new_current_alberts, new_total_alberts)
        """
        current_alberts += alberts_per_click
        total_alberts += alberts_per_click
        return current_alberts, total_alberts
