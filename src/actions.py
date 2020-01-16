
class Actions:
    def oil_lantern(self, player, oil, lantern):
        player.remove_item(oil)
        lantern.is_lit = True