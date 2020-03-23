from elasticsearch_dsl.connections import connections

from model import Analyzers

# Define a default ES client
connections.create_connection(hosts=['localhost'])

print("trying out synonym analysis ...")
for name in ['Chris', 'christopher', 'robert', 'paul']:
    print(f'{name} => {Analyzers.analyze_first_name_synonym(name).tokens}')

print('')

print("trying out phonetic analysis ...")
for name_1, name_2 in [('Krysten', 'Christian'), ('Sarah', 'Zara')]:
    print(f'nysis {name_1} => {Analyzers.analyze_nysis_phonetic(name_1).tokens}')
    print(f'nysis {name_2} => {Analyzers.analyze_nysis_phonetic(name_2).tokens}')
    print(f'beider_morse {name_1} => {Analyzers.analyze_beider_morse_phonetic(name_1).tokens}')
    print(f'beider_morse {name_2} => {Analyzers.analyze_beider_morse_phonetic(name_2).tokens}')
