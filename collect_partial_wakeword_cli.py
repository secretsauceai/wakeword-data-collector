from functions import collect_partial_wakeword_recording

def collect_partial_wakeword_cli(slug, wakeword):
    print(f'Collect partial wake word(s) contained in {wakeword} that should not wake by themselves\n')
    print('Example:\n')
    print('For "hey Jarvis" both "hey" AND "Jarvis" should be required for a sucessful wake.\n')
    print('Therefore we need to record just "Jarvis" in this case ("hey" is already recorded in the syllable collection).\n')
    collect_partial_wakeword_recording(slug, i=0)