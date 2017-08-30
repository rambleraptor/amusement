from amusement.parks.disney.MagicKingdom import MagicKingdom
from amusement.parks.disney.Epcot import Epcot
from amusement.parks.disney.HollywoodStudios import HollywoodStudios
from amusement.parks.disney.AnimalKingdom import AnimalKingdom
from amusement.parks.disney.Disneyland import Disneyland
from amusement.parks.disney.CaliforniaAdventure import CaliforniaAdventure
from amusement.parks.disney.DisneylandParis import DisneylandParis
from amusement.parks.universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from amusement.parks.universal.IslandsOfAdventure import IslandsOfAdventure
from amusement.parks.universal.UniversalStudiosHollywood import UniversalStudiosHollywood
from amusement.parks.universal.UniversalJapan import UniversalJapan
from amusement.parks.seaworld.SeaworldOrlando import SeaworldOrlando
from amusement.parks.seaworld.BuschGardensTampa import BuschGardensTampa
from amusement.parks.seaworld.SeaworldSanAntonio import SeaworldSanAntonio
from amusement.parks.seaworld.SeaworldSanDiego import SeaworldSanDiego
from amusement.parks.seaworld.BuschGardensWilliamsburg import BuschGardensWilliamsburg
from amusement.parks.HersheyPark import HersheyPark

Parks = {
    'magic-kingdom' : MagicKingdom(),
    'epcot' : Epcot(),
    'hollywood-studios' : HollywoodStudios(),
    'animal-kingdom' : AnimalKingdom(),
    'disneyland' : Disneyland(),
    'ca-adventure' : CaliforniaAdventure(),
    'disney-paris' : DisneylandParis(),
    'universal-florida' : UniversalStudiosFlorida(),
    'islands-adventure' : IslandsOfAdventure(),
    'universal-hollywood' : UniversalStudiosHollywood(),
    'universal-japan' : UniversalJapan(),
    'seaworld-orlando' : SeaworldOrlando(),
    'busch-gardens-tampa' : BuschGardensTampa(),
    'seaworld-san-antonio' : SeaworldSanAntonio(),
    'seaworld-san-diego' : SeaworldSanDiego(),
    'busch-gardens-williamsburg' : BuschGardensWilliamsburg(),
    'hersheypark' : HersheyPark()
}
