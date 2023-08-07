from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    """
    Introduces the robot and provides a brief description.
    """
    robot.say_hello()
    
def get_scientist_information():
    """
    Retrieves and displays information about the specified scientists.
    """
    robot.open_webpage(SCIENTISTS)

def say_farewell():
    """
    Bids farewell from the robot.
    """
    robot.say_goodbye

def main():
    """
    The main function that orchestrates the robot's actions.
    """
    introduce_yourself()
    get_scientist_information()
    say_farewell

if __name__ == "__main__":
    main()
