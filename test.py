from research import converter, stykesheets
import markdown
query = input('What would you like to research? ')
qwords = input(
    'Enter some qwords separated by commas: (eg: what is, why is,who is) (leave empty to skip)').split(',')
with open(f'{query}.html', 'w') as f:
    f.write(markdown.markdown(converter.formated(query, qwords))+stykesheets.AIR)
