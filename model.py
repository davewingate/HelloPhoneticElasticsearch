from uuid import uuid4

from elasticsearch_dsl import Document, Integer, Text
from elasticsearch_dsl import analyzer, analysis


class Analyzers:
    first_name_synonym_analyzer = analyzer(
        'name_search_synonym_analyzer',
        type="custom",
        tokenizer="standard",
        filter=[
            'lowercase',
            analysis.token_filter(
                'name_search_synonym_filter',
                type="synonym",
                expand=True,
                lenient=True,
                synonyms_path="common_first_name_synonyms.txt",
            )
        ]
    )

    @staticmethod
    def analyze_first_name_synonym(text):
        return Analyzers.first_name_synonym_analyzer.simulate(text)

    nysis_phonetic_analyzer = analyzer(
        'name_search_nysiis_analyzer',
        type="custom",
        tokenizer="standard",
        filter=[
            'lowercase',
            analysis.token_filter(
                'name_search_nysiis_filter',
                type="phonetic",
                encoder="nysiis",
                replace="true"
            )
        ]
    )

    @staticmethod
    def analyze_nysis_phonetic(text):
        return Analyzers.nysis_phonetic_analyzer.simulate(text)

    beider_morse_phonetic_analyzer = analyzer(
        'name_search_beider_morse_analyzer',
        type="custom",
        tokenizer="standard",
        filter=[
            'lowercase',
            analysis.token_filter(
                'name_search_beider_morse_filter',
                type="phonetic",
                encoder="beider_morse",
                replace="true"
            )
        ]
    )

    @staticmethod
    def analyze_beider_morse_phonetic(text):
        return Analyzers.beider_morse_phonetic_analyzer.simulate(text)


class NameSearch(Document):
    id = Integer()
    name = Text(
        analyzer='standard',
        search_analyzer=Analyzers.first_name_synonym_analyzer
    )
    _nysiis_name = Text(
        analyzer=Analyzers.nysis_phonetic_analyzer
    )
    _beider_morse_name = Text(
        analyzer=Analyzers.beider_morse_phonetic_analyzer
    )

    class Index:
        name = f'name_search_{str(uuid4())[:8]}'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    def __repr__(self):
        return f"NameSearch({self.meta.index}/{self.meta.id}' name='{self.name}')"

    def __str__(self):
        return self.__repr__()

    def save(self, **kwargs):
        self.meta.id = self.lead_id
        self._nysiis_name = self.name
        self._beider_morse_name = self.name
        return super(NameSearch, self).save(**kwargs)

    @staticmethod
    def search_by_name_exact(queried_name):
        by_name_query = NameSearch.search().from_dict(
            {
                "query": {
                    "match": {
                        "name": {
                            "query": queried_name,
                            "operator": "and",
                        }
                    }
                }
            }
        ).index(NameSearch.Index.name)
        return [NameSearch.from_es(hit.to_dict()) for hit in by_name_query.execute().hits.hits]

    @staticmethod
    def search_by_name_fuzzy(queried_name):
        by_name_query = NameSearch.search().from_dict(
            {
                "query": {
                    "match": {
                        "name": {
                            "query": queried_name,
                            "fuzziness": "AUTO",
                            "operator": "and",
                        }
                    }
                }
            }
        ).index(NameSearch.Index.name)
        return [NameSearch.from_es(hit.to_dict()) for hit in by_name_query.execute().hits.hits]

    @staticmethod
    def search_by_name_phonetic(queried_name):
        by_name_query = NameSearch.search().from_dict(
            {
                "query": {
                    "bool": {
                        "should": [
                            {
                                "match": {
                                    "_nysiis_name": {
                                        "query": queried_name,
                                        "operator": "and",
                                    }
                                }
                            },
                            {
                                "match": {
                                    "_beider_morse_name": {
                                        "query": queried_name,
                                        "operator": "and",
                                    }
                                }
                            }
                        ]
                    }
                }
            }
        ).index(NameSearch.Index.name)
        return [NameSearch.from_es(hit.to_dict()) for hit in by_name_query.execute().hits.hits]

