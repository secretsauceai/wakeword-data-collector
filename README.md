![Secret Sauce AI](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_logo_2.3_compressed_cropped.png?raw=true)
# Wakeword Data Collector
![Wake word](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_wakeword_scene_compressed.png?raw=true)
## Do you want your own personal wake word?
Prototype CLI to record wakewords, non-wakewords, and background noise written in python. Think of it as your wakeword data collection recipe for creating bullet proof wakeword models. 

![wakeword data collector wakeword collection example](https://github.com/secretsauceai/secret_sauce_ai/blob/main/SSAI_ww_collector_01.1.gif)
## Installation
As usual once you have cloned the repo, it is recommended to create and activate python virtual environment.
```console
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After collecting your data, it is highly recommended to run the [Precise Wakeword Model Maker](https://github.com/secretsauceai/precise-wakeword-model-maker).

## General
The Wakeword Data Collector records wave files with a sample rate of `16000` for two main categories of data:
* Wakewords (ie 'hey Jarvis') `audio/wake-word/`
  * Wakeword variations (ie saying 'hey jarvis' further/closer to the mic, faster, or slower) `audio/wake-word/variations/`
* Not-wakewords `audio/not-wake-word/`
   * background noise recordings `audio/not-wake-word/background/`
   * syllables (ie 'hey, jar, vis') `audio/not-wake-word/parts/`
   * combinations of syllable permutations (ie 'hey jar', 'jarvis') `audio/not-wake-word/parts/`
   * other longer recordings: recording the TV and a natural conversation `audio/not-wake-word/`


## Usage
Simply run `collect_ide.py` in your console and follow the instructions.
```
python collect_ide.py
```

For a first time user, it is highly recommended to do a full data collection of all steps (besides `3. Non-wake-word recordings` which is optional) to ensure a production quality wakeword.
* `1. First set of 16 wakeword recordings`
* `2. Wakeword syllable and syllable permutation recordings`
* `4. Second set of 16 wakeword recordings`
* `5. Wakeword variations`
* `6. Third set of 16 wakeword recordings`
* `7. First random conversation recordings`
* `8. Second random TV recording`
* `9. Second rantom TV recording`
* The background recordings taken throughout the sessions will be in `audio/not-wake-word/background/`

If you are doing a data collection to add another user it is recommended to record:
* `1. First set of 16 wakeword recordings`
* `7. First random conversation recording`
* All of the background recordings from this session in `audio/not-wake-word/background/`
* `2. Wakeword syllable and syllable permutation recordings` is optional, but it can help


### IMPORTANT
Make sure to check each recording, it is always possible something went wrong. Even one bad or missing recording can be the difference between a bullet proof and a bullet ridden wakeword model. 
