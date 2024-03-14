"""
print the diffs between redacted and unredacted transcripts
"""
import difflib

import assemblyai as aai
from termcolor import colored

def process_tag(matcher, tag, i1, i2, j1, j2):
    match tag:
        case 'replace':
            return '{' + colored(matcher.a[i1:i2], 'red') + ' -> ' + colored(matcher.b[j1:j2], 'green') + '}'
        case 'delete':
            return colored(matcher.a[i1:i2], 'red')
        case 'equal':
            return matcher.a[i1:i2]
        case 'insert':
            return colored(matcher.b[j1:j2], 'green')
        case _:
            assert False, "Unknown tag %r"%tag

def get_diff_string(a, b):
    matcher = difflib.SequenceMatcher(None, a, b)
    return ''.join(process_tag(matcher, *t) for t in matcher.get_opcodes())

audio_url = "https://storage.googleapis.com/aai-web-samples/architecture-call.mp3"

redaction_config = aai.TranscriptionConfig(
    redact_pii=True,
    redact_pii_policies=[
        aai.PIIRedactionPolicy.person_name,
        aai.PIIRedactionPolicy.phone_number,
    ],
    redact_pii_sub=aai.PIISubstitutionPolicy.hash,
)

transcript_normal = aai.Transcriber().transcribe(audio_url)
transcript_redacted = aai.Transcriber().transcribe(audio_url, redaction_config)

diff = get_diff_string(
    transcript_normal.text,
    transcript_redacted.text
)

print(diff)
