from functions import collect_number_of_recordings, collect_background_noise, collect_wakewords, collect_wakeword_variations

def collect_wakeword_variations_cli(slug, wakeword):
    collect_background_noise(slug, nr=7)
    collect_wakeword_variations(slug, wakeword)
    collect_background_noise(slug, nr=8)