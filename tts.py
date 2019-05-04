from google.cloud import texttospeech
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-UK',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE)
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)
client = texttospeech.TextToSpeechClient()
def produce_audio(text: str,ID: str):
    synthesis_input = texttospeech.types.SynthesisInput(text=text)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    with open(('audio/output'+ID+'.mp3'), 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)





# x = "hey im tom i love people"
# x1 = ["hey im tom","i love people"]
# produce_audio(x,"nonarray")
# for x2 in range(len(x1)):
#     produce_audio(x1[x2],("array "+str(x2)))
# audio = MP3(("audio_test/array 0.mp3"))
# audio1 = MP3(("audio_test/array 1.mp3"))
# audio2 = MP3("audio_test/nonarray.mp3")
# length_array = 0
# length_array += float(audio.info.length)
# length_array += float(audio1.info.length)
#
# length_string = float(audio2.info.length)
# print(length_array,length_string)

#import subprocess
#
# def execute_unix(inputcommand):
#    p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)    2.424 | 1.128
#    (output, err) = p.communicate()
#    return output
#
# a = "Say something in natural language."
#
# # create wav file
# # w = 'espeak -w temp.wav "%s" 2>>/dev/null' % a
# # execute_unix(w)
#
# # tts using espeak
# c = 'espeak -v mb-us1 -s130 "%s" 2>>/dev/null' % a
# execute_unix(c)