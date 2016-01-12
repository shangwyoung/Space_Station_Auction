import space_station
import card
import sortSpaceStations

def main():
    card1 = card.Card("Card1", [5,4,3,2,1])
    card2 = card.Card("Card2", [4,3,2,9,9])

    station1 = space_station.SpaceStation("Station A", 1)
    station1.addCard(card1)
    station2 = space_station.SpaceStation("Station B", 2)
    station2.addCard(card2)

    sorted_station = sortSpaceStations.SortSpaceStations.sort_stations([station1, station2])

    for station in sorted_station:
        print(station)
        print(station.getRank())



if __name__ == "__main__":
    main()
