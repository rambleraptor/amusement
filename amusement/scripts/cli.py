import click
from amusement import Parks

@click.command()
@click.argument('name', nargs=1, type=click.Choice(Parks.keys()))
@click.option('--type', type=click.Choice(['rides', 'shows']), prompt='Please choose rides or shows')
def cli(name, type):
    park = Parks[name]
    if type == 'rides':
        print_rides(park.rides())
    if type == 'shows':
        print(park.shows())

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

