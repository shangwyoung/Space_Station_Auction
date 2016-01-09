import space_station
import card

def main():
    station = space_station.SpaceStation("Fred", 25)

    print(station.getName())
    print(station.getID())

    card1 = card.Card("card1", [5,0,0,0,5])
    card2 = card.Card("card2", [1,0,0,2,0])

    station.addCard(card1)

    print(station.getCards()[0])

    station.addCard(card2)

    print(station.getCards()[1])
    print(station.getScores())
    print(station)

main()
