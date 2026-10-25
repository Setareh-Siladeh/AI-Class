class Character:
    def __init__(self , name , power , health , coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

        def show_info(self):
            print(
                f"{self.name} | level: {self.level} |"
                f"Power: {self.power} | Health: {self.health} | "
                f"Coins: {self.coins}"
            )

            def is_alive(self):
                if self.health > 0:
                    return True
                else:
                    return False
                
            def attack(self, other):
                other.health -= self.power
                print(
                    f"{self.name} attacked {other.name}. "
                    f"{other.name}'s health: {other.health}"
                )

                def earn_coins(self, amount):
                    self.coins += amount

                def buy_potion(self):
                    if self.coins >= 20:
                        self.coins -= 20
                        self.health += 30
                    else:
                        print("Not enough coins")

                def level_up(self):
                    self.level += 1
                    self.power += 5
                    print(
                        f"{self.name} reached level {self.level}. "
                        f"New power: {self.power}"
                    )

arya = Character("Arya", 10,100,50)
baran = Character("Baran", 8, 80, 30)

arya.show_info()
baran.show_info()

arya.attack(baran)
baran.attack(arya)
arya.attack(baran)

arya.earn_coins(20)

arya.buy_potion()

arya.level_up()

arya.show_info()
baran.show_info()