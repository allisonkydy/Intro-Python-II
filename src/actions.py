
class Actions:
    def oil_lantern(self, player, oil, lantern):
        player.remove_item(oil)
        player.is_lit = True
        lantern.is_lit = True
        print("Oil used on lantern")
        print("Lantern is now lit")