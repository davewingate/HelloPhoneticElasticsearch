from elasticsearch_dsl.connections import connections

from model import NameSearch, Analyzers

# Define a default ES client
connections.create_connection(hosts=['localhost'])

# create the mappings in ES
NameSearch.init()

# index some documents
NameSearch(lead_id=1, name="Chris De Avila").save()
NameSearch(lead_id=2, name="Cristo D'Avila").save()
NameSearch(lead_id=3, name="Chris Brown").save()
NameSearch(lead_id=4, name="Cuthbert Allgood").save()
NameSearch(lead_id=5, name="Dr. Martin Luther King Jr.").save(
    # wait for the index to be ack'd so that subsequent query
    # is guaranteed to see this data
    refresh='wait_for'
)


# helper function for search and print results
def search_and_results(search_func, name_query, num_expected):
    results = search_func(name_query)
    print(
        f'{"" if len(results) == num_expected else "!!!"} found {len(results)} of {num_expected} expected results for search "{name_query}": {results}')


print("############# search_by_name_exact #############")
search_and_results(NameSearch.search_by_name_exact, "Chris De Avila", 1)
search_and_results(NameSearch.search_by_name_exact, "Christopher De Avila", 1)
search_and_results(NameSearch.search_by_name_exact, "Chris De Avilla", 0)
search_and_results(NameSearch.search_by_name_exact, "Chris D'Avilla", 0)
search_and_results(NameSearch.search_by_name_exact, "Cuthbert", 1)
search_and_results(NameSearch.search_by_name_exact, "Cuthbert All", 0)
search_and_results(NameSearch.search_by_name_exact, "Cutburt Awlgood", 0)
search_and_results(NameSearch.search_by_name_exact, "Martin Luther King", 1)
search_and_results(NameSearch.search_by_name_exact, "Dr. King Jr.", 1)

print('')

print("############# search_by_name_fuzzy #############")
search_and_results(NameSearch.search_by_name_fuzzy, "Chris De Avila", 1)
search_and_results(NameSearch.search_by_name_fuzzy, "Chris De Avilla", 1)
search_and_results(NameSearch.search_by_name_fuzzy, "Chris D'Avilla", 0)
search_and_results(NameSearch.search_by_name_fuzzy, "Cuthbert", 1)
search_and_results(NameSearch.search_by_name_fuzzy, "Cuthbert All", 0)
search_and_results(NameSearch.search_by_name_fuzzy, "Cutburt Awlgood", 1)
search_and_results(NameSearch.search_by_name_fuzzy, "Martin Luther King", 1)
search_and_results(NameSearch.search_by_name_fuzzy, "Dr. King Jr.", 1)

print('')

print("############# search_by_name_phonetic #############")
search_and_results(NameSearch.search_by_name_phonetic, "Chris De Avila", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Chris De Avilla", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Chris D'Avilla", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Cuthbert", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Cuthbert All", 0)
search_and_results(NameSearch.search_by_name_phonetic, "Cutburt Awlgood", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Martin Luther King", 1)
search_and_results(NameSearch.search_by_name_phonetic, "Dr. King Jr.", 1)
