import assemblyai as aai

audio_url = "https://storage.googleapis.com/aai-web-samples/architecture-call.mp3"

config = aai.TranscriptionConfig(
    redact_pii=True,
    redact_pii_audio=True, # create a redacted audio file
    redact_pii_policies=[
        aai.PIIRedactionPolicy.person_name,
        aai.PIIRedactionPolicy.phone_number,
    ],
    redact_pii_sub=aai.PIISubstitutionPolicy.hash,
)

transcript = aai.Transcriber().transcribe(audio_url, config)

print(transcript.text, '\n\n')
print(transcript.get_redacted_audio_url())
