class Item:

    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Heavily used"
        elif self.condition == 1:
            return "Used"
        elif self.condition == 2:
            return "Ok"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Great"
        elif self.condition == 5:
            return "Mint"

