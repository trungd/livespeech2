---
layout: page
title: "Zero-Shot Text-to-Speech from Continuous Text Streams"
--- 

<p style="text-align: center; font-style: italic"><a href="mailto:trungv.dang@outlook.com">Trung Dang</a>, David Aponte, Dung Tran, Tianyi Chen, Kazuhito Koishida<br />Applied Sciences Group, Microsoft Corporation</p>

<p style="text-align: center">[<a href="">arXiv</a>]</p>

### Abstract

Existing zero-shot text-to-speech (TTS) systems are typically designed to process complete sentences and are constrained by the maximum duration for which they have been trained. However, in many streaming applications, texts arrive continuously in short chunks, necessitating instant responses from the system. We identify the essential capabilities required for chunk-level streaming and introduce LiveSpeech 2, a stream-aware model that supports infinitely long speech generation, text-audio stream synchronization, and seamless transitions between short speech chunks. To achieve these, we propose (1) adopting Mamba, a class of sequence modeling distinguished by linear-time decoding, which is augmented by cross-attention mechanisms for conditioning, (2) utilizing rotary positional embeddings in the computation of cross-attention, enabling the model to process an infinite text stream by sliding a window, and (3) decoding with semantic guidance, a technique that aligns speech with the transcript during inference with minimal overhead. Experimental results demonstrate that our models are competitive with state-of-the-art language model-based zero-shot TTS models, while also providing flexibility to support a wide range of streaming scenarios.

<div style="text-align: center">
<img src="./assets/livespeech2.png" alt="Model Architecture" width="75%">
<p>
Model Architecture
</p>
</div>

### Samples (Short)


<div style="overflow: scroll">
<table style="width: 2000px">
    <tr>
        <td width="300">Transcript</td>
        <td>Enrollment</td>
        <td>Reference</td>
        <td>YourTTS</td>
        <td>SpeechX</td>
        <td>XTTS-v2</td>
        <td>MetaVoice</td>
        <td>LiveSpeech v1</td>
        <td>LiveSpeech v2</td>
    </tr>
    {% for sample in site.data.samples_short %}
        <tr>
            <td width="300">{{ sample.transcript }}</td>
            <td><audio controls><source src="./assets/short/enrollment_samples/{{ sample.id }}.enroll.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/reference_raw/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/yourtts/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/valle/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/xtts_v2/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/metavoice/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/livespeech_v1/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/short/livespeech_v2/{{ sample.id }}.wav" type="audio/wav"></audio></td>
        </tr>
    {% endfor %}
</table>
</div>


### Samples (Long)



<table>
    <tr>
        <td style="width: 200px">Transcript</td>
        <td>Enrollment</td>
        <td>Reference</td>
        <td>YourTTS</td>
        <td>XTTS-v2</td>
        <td>LiveSpeech v2</td>
    </tr>
    {% for sample in site.data.samples_long %}
        <tr>
            <td>{{ sample.transcript }}</td>
            <td><audio controls><source src="./assets/long/enrollment_samples/{{ sample.id }}.enroll.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/long/reference_raw/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/long/yourtts/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/long/xtts_v2/{{ sample.id }}.wav" type="audio/wav"></audio></td>
            <td><audio controls><source src="./assets/long/livespeech_v2/{{ sample.id }}.wav" type="audio/wav"></audio></td>
        </tr>
    {% endfor %}
</table>

