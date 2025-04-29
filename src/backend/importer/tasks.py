from django_rq import job

import musicbrainzngs as mbz


@job
def import_artist_data(mbid: str):
    mbz.set_useragent('Jukabox', '0.1', 'jukabox.site@gmail.com')
    
