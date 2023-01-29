import sys
import time
import pyaudio
import wave
import os
import io
from zipfile import ZipFile
import pathlib

def make_directories():
    make_paths = [
        'audio/',
        'audio/not-wake-word/',
        'audio/not-wake-word/background/',
        'audio/not-wake-word/paragraph',
        'audio/not-wake-word/syllables/',
        'audio/not-wake-word/parts/',
        'audio/wake-word/',
        'audio/wake-word/variations/',
        'audio/random/'

    ]
    # check if directories exist or not
    for make_path in make_paths:
        if not os.path.exists(make_path):
            os.makedirs(make_path)

MAX_VARIATION_COUNT = 9

# wave recording format
chunk = 1024
sample_format = pyaudio.paInt16
channels = 1
sample_frequency = 16000

stream = None

CALIBRATION_PHRASE_GREEN_ROOM = [
  'In the great green room',
  'There was a telephone',
  'A comb with a brush',
  'On top of some kind of bowl full of mush',
  'And a red balloon'
  ]

CALIBRATION_PHRASE_COW = [
 'A picture of the cow jumping over the moon',
 'There were three little bears sitting on chairs',
 'A pair of mittens',
 'Goodnight to the quite old lady whispering hush'
 ]

pyaudio_instance = None
# int recording stream
def pyaudio_start():
    global pyaudio_instance
    pyaudio_instance = pyaudio.PyAudio()
    print(pyaudio_instance)

def pyaudio_terminate():
    pyaudio_instance.terminate()
    
def countdown(count):
    for j in range(count, 0, -1):
        sys.stdout.write(f'{j} ')
        sys.stdout.flush()
        time.sleep(1)
    
def record(seconds, filename):
    stream = pyaudio_instance.open(format=sample_format, channels=channels, rate=sample_frequency, frames_per_buffer=chunk, input=True)
    # int array to store frames
    frames = []

    # store data in chunks of for the given seconds parameter
    for i in range(0, int(sample_frequency / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    
    # save the recording as a wav file
    wave_file = wave.open(filename, 'wb')
    wave_file.setnchannels(channels)
    wave_file.setsampwidth(pyaudio_instance.get_sample_size(sample_format))
    wave_file.setframerate(sample_frequency)
    wave_file.writeframes(b''.join(frames))
    wave_file.close()
    stream.stop_stream()
    stream.close()
    print("Done\n")

def zipfiles(file_name):
    zipObj = ZipFile(file_name, 'w')
    filelist = os.listdir(os.getcwd())
    print(filelist)
    for file in filelist:
        if '.wav' in file:
            zipObj.write(file)
    zipObj.close()


def collect_user_data():
    print("""\n\nWelcome to the wake word collection tool!
\nFor best results when recording:
 * Pick a wake word(s) with at least three total syllables
 * Don't add pauses between words
 * Speak as you normally would, don't get too weird with your voice!
 * Record on the same mic and place as you intend to use the model
 * Be quiet when recording the background noise
""")
    time.sleep(3)
    wakeword = str(input("\nPlease enter your wake word(s):\n"))
    wakeword_parts = str(input("\nPlease type in your wake word(s) as syllables seperated by comma (i.e. for 'hey jarvis':hey, jar, vis):\n"))
    wakeword_split = wakeword_parts.split(', ')
    name = str(input("\nPlease enter in your first name or initials to be used in sample file names:\n"))
    labels = str(input("\nAny other important labels for your data (i.e. mic)? (hit enter to skip)\n"))
    slug = '%s_%s_%s' %  (wakeword.replace(" ", "_"), name.replace(" ", "_"), labels.replace(" ", "_"))
    
    return wakeword, wakeword_split, name, labels, slug

def collect_background_noise(slug, nr):
    print("\nRecording background noise in...")
    countdown(3)
    print("")
    print("\n● Recording background noise, please be quiet.")
    record(3, f'audio/not-wake-word/background/background_{slug}_{nr:03}.wav')
    time.sleep(2.5)

def collect_wakewords(_from, _to, wakeword, slug):
    for step in range(_from, _to):
        input(f"{step + 1}/{_to}. When you are ready to record your wake word, press enter:")
        print(f'Say \'{wakeword}\' in...')
        countdown(3)
        print("")
        print("● "+wakeword)
        record(3, f'audio/wake-word/{slug}_{step:03}.wav')

def collect_non_wakeword(index, slug):
    for i, phrase in enumerate(CALIBRATION_PHRASE_GREEN_ROOM):
        print("Using a CONVERSATIONAL voice (like you are talking to someone), after the prompt say the following text:\n" + phrase)
        input("When you are ready to record, press enter:")
        countdown(3)
        print("")
        print(phrase)
        record(6, f'audio/not-wake-word/paragraph/paragraph_0{index}_{slug}_green_room_{i}.wav')

    for j, phrase in enumerate(CALIBRATION_PHRASE_COW):
        print("Using a CONVERSATIONAL voice, after the prompt say the following text:\n" + phrase)
        input("When you are ready to record, press enter:")
        countdown(3)
        print("")
        print(phrase)
        record(6, f'audio/not-wake-word/paragraph/paragraph_0{index}_{slug}_cow_{j}.wav')

def collect_wakeword_variations(slug, wakeword):

    prompts = [
        "Say your wake word a bit faster",
        "Say your wake word a bit slower (remember: no pauses between words!)",
        "Say your wake word in a deeper voice",
        "Say your wake word in a higher pitched voice",
        "Say your wake word in a SLIGHTLY different accent (ie American/British)",
        "Say your wake word in a SLIGHTLY different accent from last time (ie American/British)",
        "Say your wake word a bit louder",
        "Say your wake word a bit quieter",
        "Say your wake word closer or further away from your mic",

    ]
    variation_index = -1

    for prompt in prompts:
        print("Variate the wake word by changing how you say it for this recording and the next")
        time.sleep(1)

        print(prompt)

        input("When you are ready to record, press enter:")
        countdown(3)
        print("")
        print(f'\n● Say {wakeword}')
        variation_index += 1
        record(3, f'audio/wake-word/variations/variation_{slug}_{variation_index}.wav')

        input("When you are ready to record, press enter:")
        countdown(3)
        print("")
        print(f'\n● Say {wakeword}')
        variation_index += 1
        record(3, f'audio/wake-word/variations/variation_{slug}_{variation_index}.wav')

def collect_number_of_recordings():
    recording_prompt = input("Please enter the number of recordings:\n")
    recordings_count = int(recording_prompt)
    return recordings_count

def show_hint():
    print("For the first time it's recommended to record your wake word a total of 32 times")
    time.sleep(2.5)

def collect_random_recording(slug, recording_type, recording_number):
    input("When you are ready to record, press enter:")
    countdown(3)
    print("")
    print("\n● Recording...")
    record(900, f'audio/random/random_{slug}_{recording_type}_{recording_number}.wav')

def collect_wake_word_syllables(slug, wakeword_split):
    for syllable in wakeword_split:
        print("\n********** Wakeword part: "+syllable+" ************\n")
        for count_number in range(1,5):
            input(str(count_number)+"/4 When you are ready to record, press enter:")
            print(f'Say \'{syllable}\' in...')
            countdown(3)
            print("\n● "+syllable)
            record(3, f'audio/not-wake-word/parts/{slug}_{syllable}_{count_number:03}.wav')

def collect_all_partial_wake_word_recording(slug, wakeword_split):
    # collect each syllable seperately 4 times (like collect_wake_word_syllables)
    collect_wake_word_syllables(slug, wakeword_split)
    for syllable in wakeword_split:
        # join the current syllable with the next record each 4 times
        syllable_index = wakeword_split.index(syllable)
        next_syllable_index = syllable_index + 2
        number_of_syllables = len(wakeword_split)
        if next_syllable_index <= number_of_syllables:
            wake_word_part = ''.join(wakeword_split[syllable_index:syllable_index+ 2])
            print("\n********** Wakeword part: "+wake_word_part+" ************\n")
            for count_number in range(1,5):
                input(str(count_number)+"/4 When you are ready to record, press enter:")
                print(f'Say \'{wake_word_part}\' in...')
                countdown(3)
                print("\n● "+wake_word_part)
                record(3, f'audio/not-wake-word/parts/{slug}_{wake_word_part}_{count_number:03}.wav')

def collect_partial_wakeword_recording(slug, i):
    input("When you are ready to record, press enter:")
    print(f'Say the partial wake word(s) in...')
    countdown(3)
    print("")
    record(3, f'audio/not-wake-word/parts/part_{i}_{slug}_0.wav')   
    input("When you are ready to record the same partial wake word(s), press enter:")
    print(f'Say the same partial wake word(s) as last time in...')
    countdown(3)
    print("")
    record(3, f'audio/not-wake-word/parts/part_{i}_{slug}_1.wav')
    
    key_press = input('To record another pair of partial wake word(s) press 1 then press enter, to go back to the main menu just press enter:\n')
    if key_press == '1':
        collect_partial_wakeword_recording(slug, i + 1)
