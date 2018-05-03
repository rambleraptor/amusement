from amusement.parks.disney.MagicKingdom import MagicKingdom
from amusement.parks.disney.Epcot import Epcot
from amusement.parks.disney.HollywoodStudios import HollywoodStudios
from amusement.parks.disney.AnimalKingdom import AnimalKingdom
from amusement.parks.disney.Disneyland import Disneyland
from amusement.parks.disney.CaliforniaAdventure import CaliforniaAdventure
from amusement.parks.universal.UniversalStudiosFlorida import UniversalStudiosFlorida
from amusement.parks.universal.IslandsOfAdventure import IslandsOfAdventure
from amusement.parks.universal.UniversalStudiosHollywood import UniversalStudiosHollywood
from amusement.parks.universal.UniversalJapan import UniversalJapan
from amusement.parks.HersheyPark import HersheyPark

Parks = {
    'magic-kingdom' : MagicKingdom(),
    'epcot' : Epcot(),
    'hollywood-studios' : HollywoodStudios(),
    'animal-kingdom' : AnimalKingdom(),
    'disneyland' : Disneyland(),
    'ca-adventure' : CaliforniaAdventure(),
    'universal-florida' : UniversalStudiosFlorida(),
    'islands-adventure' : IslandsOfAdventure(),
    'universal-hollywood' : UniversalStudiosHollywood(),
    'universal-japan' : UniversalJapan(),
    'hersheypark' : HersheyPark(),
}
