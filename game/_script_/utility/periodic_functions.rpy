init python:
    def periodic_achievements():
        if not achievement.status('gold') and game.gold >= 10000:
            achievement.unlock("gold")

        if not achievement.status('drunkard') and wine_ITEM.owned >= 25:
            achievement.unlock("drunkard")

        if not achievement.status('peta') and (game.day-phoenix_fed_counter) >= 50:
            achievement.unlock("peta")

        if not achievement.status('petpal') and phoenix_petted_counter >= 25:
            achievement.unlock("petpal")

        if not achievement.status('bros') and sna_friendship >= 100:
            achievement.unlock("bros")

        if not achievement.status('overwhored') and her_whoring >= 24:
            achievement.unlock("overwhored")

        if not achievement.status('fireplace') and stat_fireplace_counter >= 5:
            achievement.unlock("fireplace")

        if not achievement.status('workaholic') and stat_reports_counter >= 5:
            achievement.unlock("workaholic")
        return

    def periodic_callbacks():
        """Call functions that need to be checked periodically (i.e. achievement unlocks) at around 20Hz"""
        periodic_achievements()

define config.periodic_callback = periodic_callbacks
