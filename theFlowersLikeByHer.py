class theFlowersLikeByHer:
    def __init__(self, flowers):
        self.flowers = flowers
    
    def check_flower(self):
        if self.flowers == "spathiphyllum":
            print(f"No, I want a big {self.flowers.title()}!")
        elif self.flowers == "Spathiphyllum":
            print(f"Yes - {self.flowers} is the best plant ever!")
        else:
            print(f"Spathiphyllum! Not {self.flowers.title()}!")

the_flower = theFlowersLikeByHer(str(input("Enter the flower name: ")))
the_flower.check_flower()