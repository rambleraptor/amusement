import click
from amusement.parks.disney.MagicKingdom import MagicKingdom
from amusement.parks.disney.Epcot import Epcot
from amusement.parks.disney.HollywoodStudios import HollywoodStudios
from amusement.parks.disney.AnimalKingdom import AnimalKingdom
from amusement.parks.disney.Disneyland import Disneyland
from amusement.parks.disney.CaliforniaAdventure import CaliforniaAdventure
from amusement.parks.disney.DisneylandParis import DisneylandParis
from amusement.parks.universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from amusement.parks.universal.IslandsOfAdventure import IslandsOfAdventure
from amusement.parks.universal.UniversalHollywood import UniversalHollywood
from amusement.parks.universal.UniversalJapan import UniversalJapan
from amusement.parks.seaworld.SeaworldOrlando import SeaworldOrlando
from amusement.parks.seaworld.BuschGardensTampa import BuschGardensTampa
from amusement.parks.seaworld.SeaworldSanAntonio import SeaworldSanAntonio
from amusement.parks.seaworld.SeaworldSanDiego import SeaworldSanDiego
from amusement.parks.seaworld.BuschGardensWilliamsburg import BuschGardensWilliamsburg
from amusement.parks.HersheyPark import HersheyPark


PARKS = {
    'magic-kingdom' : MagicKingdom(),
    'epcot' : Epcot(),
    'hollywood-studios' : HollywoodStudios(),
    'animal-kingdom' : AnimalKingdom(),
    'disneyland' : Disneyland(),
    'ca-adventure' : CaliforniaAdventure(),
    'disney-paris' : DisneylandParis(),
    'universal-florida' : UniversalStudiosFlorida(),
    'islands-adventure' : IslandsOfAdventure(),
    'universal-hollywood' : UniversalHollywood(),
    'universal-japan' : UniversalJapan(),
    'seaworld-orlando' : SeaworldOrlando(),
    'busch-gardens-tampa' : BuschGardensTampa(),
    'seaworld-san-antonio' : SeaworldSanAntonio(),
    'seaworld-san-diego' : SeaworldSanDiego(),
    'busch-gardens-williamsburg' : BuschGardensWilliamsburg(),
    'hersheypark' : HersheyPark()
}

@click.command()
@click.argument('name', nargs=1, type=click.Choice(PARKS.keys()))
@click.option('--type', type=click.Choice(['rides', 'shows']), prompt='Please choose rides or shows')
def cli(name, type):
    park = PARKS[name]
    if type == 'rides':
        print_rides(park.rides())
    if type == 'shows':
        print park.shows()

def print_rides(ride_array):
    longest_name = max(len(key['name']) for key in ride_array)
    one_closed = False in [key['isOpen'] for key in ride_array]
    for ride in ride_array:
        line = ''
        line += ride['name'] + ' ' * (longest_name - len(ride['name']))
        line += ' ' * 3
        if ride['isOpen'] is True:
            line += 'Open'
            # make sure the times are aligned b/c closed longer than open
            if one_closed:
                line += ' ' * 2
        else:
            line += 'Closed'

        line += ' ' * 5
        line += str(ride['wait']) + ' mins'
        click.echo(line)



if __name__ == "__main__":
    cli()

