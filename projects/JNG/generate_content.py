#!/usr/local/bin/python3

from subprocess import Popen, PIPE
def execute_commands(commands):
    p = Popen(commands, shell=True, stdout=PIPE, stderr=PIPE)
    out, err = p.communicate()
    print(out)
    print()
    print(err)
    return out, err
import sys
import os
import auditok
import azure.cognitiveservices.speech as speechsdk
# you need pip3 install azure-cognitiveservices-speech

'''### Run By Your Host System
ffmpeg -i ~/One*/TPPHC/SERMON/Johnson_Ng_mydownload/*-xxxxxxxxxxx.mp3 ~/SOURCE/sermon-app/projects/xxxxxxxxxxx.wav'''
target_code = sys.argv[1] # 'xxxxxxxxxxx'
print(f'\n\n\nls ../../data/JNG/ | grep -- {target_code}\n\n\n')
if os.path.isfile("../../data/JNG/" + target_code + ".txt"):
    print(f"file ../../data/JNG/{target_code}.txt already exist !")
    print("exit !")
    exit()
input_filename = f'{target_code}.wav'
print(input_filename)
_ = os.system('mkdir -p -- '+target_code)
# split returns a generator of AudioRegion objects
audio_regions = auditok.split(
    input_filename,
    min_dur=0.5,     # minimum duration of a valid audio event in seconds
    max_dur=30,       # maximum duration of an event
    max_silence=0.3, # maximum duration of tolerated continuous silence within an event
    energy_threshold=40 # threshold of detection
)
with open(f"../../auditok_data/JNG/auditok_log-{target_code}.txt", "w") as fp_auditok:
    for i, r in enumerate(audio_regions):

        # Regions returned by `split` have 'start' and 'end' metadata fields
        results_str = "Region {i}: {r.meta.start:.3f}s -- {r.meta.end:.3f}s".format(i=i, r=r)
        print(results_str)
        fp_auditok.write(results_str + "\n")

        # play detection
        # r.play(progress_bar=True)

        # region's metadata can also be used with the `save` method
        # (no need to explicitly specify region's object and `format` arguments)
        filename = r.save(target_code+'/'+input_filename[:-4]+"_{meta.start:08.3f}-{meta.end:08.3f}.wav")
        print("region saved as: {}".format(filename))
fp_auditok.close()
file_list = [f for f in os.listdir(target_code) if input_filename[:-4].replace('./','')+'_' in f]
file_list.sort()

with open('azs', 'r') as fpazs:
    azs = fpazs.read()
fpazs.close()
azs = azs.strip()
def from_file(inputWavFileName):
    speech_config = speechsdk.SpeechConfig(
            subscription=azs,
            region="southeastasia")
    # Find keys and location/region
    # from https://docs.microsoft.com/en-us/azure/cognitive-services/
    #              speech-service/overview#try-the-speech-service-for-free
    speech_config.speech_recognition_language="zh-HK"
    print("done set up speech_config")
    audio_input = speechsdk.AudioConfig(filename=inputWavFileName)
    print("done set up audio_input")
    speech_recognizer = speechsdk.SpeechRecognizer(
            speech_config=speech_config,
            audio_config=audio_input)
    print("done set up speech_recognizer")
    result = speech_recognizer.recognize_once_async().get()
    print("done obtain result")
    print("generating text file ...")
    #ytcode = inputWavFileName.split(".")[0]
    ytcode = inputWavFileName[:-4]
    outTextFileName = ytcode + ".txt"
    with open(outTextFileName, "w", encoding='utf-8') as fp:
        fp.write(result.text)
    fp.close()
    print("done generating text file !")
    print(outTextFileName)
    print()

'''### Run By Your Host System
ls xxxxxxxxxxx/*.wav | wc -l'''
fid_start = 0
fid_end = 8000
for fid in range(fid_start,min(len(file_list), fid_end)):
    print('fid = %d / %d' % (fid, len(file_list)))
    if os.path.exists(target_code + '/' + file_list[fid]) \
        and not os.path.exists(target_code + '/' + file_list[fid][:-4]+'.txt'): \
        from_file(target_code + '/' + file_list[fid])


with open(f'concat_{target_code}.py'.replace('./',''), 'w') as fp:
    fp.write('#!/bin/python3\n')
    fid_start = 0
    fid_end = 8000
    for fid in range(fid_start,min(len(file_list), fid_end)):
        if os.path.exists(target_code + '/' + file_list[fid]):
            fp.write(f'fp = open(\'{target_code}/{file_list[fid][:-3]}txt\')\n')
            fp.write('line = fp.readline()\n')
            fp.write('fp.close()\n')
            fp.write('print(line)\n')
fp.close()
print(f'\n\nRun By Your Host System\n\npython3 concat_{target_code}.py > ../../data/JNG/{target_code}.txt\n\n'.replace('./',''))

