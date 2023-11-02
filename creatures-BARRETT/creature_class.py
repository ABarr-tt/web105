class Creature:
    def __init__(self, type_of_creature, friendly, position, image):
        self.type_of_creature = type_of_creature
        self.friendly = friendly
        self.position = position
        self.image = image

    # mutators
    def set_type_of_creature(self, type_of_creature):
        self.type_of_creature = type_of_creature

    def set_friendly(self, friendly):
        self.friendly = friendly

    def set_position(self, position):
        self.position = position

    def set_image(self, image):
        self.image = image

    # accessors (getters)
    def get_type_of_creature(self):
        return self.type_of_creature

    def get_friendly(self):
        return self.friendly

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    # return
    def __str__(self):
        if self.friendly:
            description = f"This friendly {self.type_of_creature} is located at "
        else:
            description = f"This unfriendly {self.type_of_creature} is located at "
        return description + str(self.position) + " and uses the image asset: " + self.image


class Orc(Creature):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points):
        #sets friendly to False and type_of_creature to "Orc"
        super().__init__("Orc", False, position, image)
        self.weapon = weapon
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points

    # Setters
    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_max_hit_points(self, max_hit_points):
        self.max_hit_points = max_hit_points

    def set_current_hit_points(self, current_hit_points):
        self.current_hit_points = current_hit_points

    # Getters
    def get_weapon(self):
        return self.weapon

    def get_max_hit_points(self):
        return self.max_hit_points

    def get_current_hit_points(self):
        return self.current_hit_points

    def __str__(self):
        description = super().__str()
        return (
            f"{description} and wields a {self.weapon}. "
            f"Max HP: {self.max_hit_points}, Current HP: {self.current_hit_points}."
        )


class OrcBoss(Orc):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points, name, special_move):
        super().__init__(position, image, weapon, max_hit_points, current_hit_points)
        # Add attributes
        self.name = name
        self.special_move = special_move

    # Setters
    def set_name(self, name):
        self.name = name

    def set_special_move(self, special_move):
        self.special_move = special_move

    #Getters
    def get_name(self):
        return self.name

    def get_special_move(self):
        return self.special_move

    def __str__(self):
        description = super().__str__()
        return (
            f"{description} Name: {self.name}, Special Move: {self.special_move}."
        )

class Creature:
    def __init__(self, type_of_creature, friendly, position, image):
        self.type_of_creature = type_of_creature
        self.friendly = friendly
        self.position = position
        self.image = image

    def __str__(self):
        if self.friendly:
            description = f"This friendly {self.type_of_creature} is located at "
        else:
            description = f"This unfriendly {self.type_of_creature} is located at "
        return description + str(self.position) + " and uses the image asset: " + self.image

class Orc(Creature):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points):
        super().__init__("Orc", False, position, image)
        self.weapon = weapon
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points

    def __str__(self):
        description = super().__str()
        return (
            f"{description} and wields a {self.weapon}. "
            f"Max HP: {self.max_hit_points}, Current HP: {self.current_hit_points}."
        )

class OrcBoss(Orc):
    def __init__(self, position, image, weapon, max_hit_points, current_hit_points, name, special_move):
        super.__init__(position, image, weapon, max_hit_points, current_hit_points)
        self.name = name
        self.special_move = special_move

    def __str__(self):
        description = super().__str()
        return (
            f"{description} Name: {self.name}, Special Move: {self.special_move}."
        )

creature = Creature("Dragon", True, (10, 20, 30), "dragon.png")
orc = Orc((15, 25, 35), "orc.png", "club", 100, 80)
orc_boss = OrcBoss((20, 30, 40), "orc_boss.png", "sword", 150, 120, "Grommash", "Cleave")

print(creature)
print(orc)
print(orc_boss)