---
layout: page
title: "Evaluation Form"
--- 

### Samples (Short)

Listen to the FULL audio, and rate (1) the naturalness and (2) the similarity to the enrollment speech in a scale from 1-5.

1 - Bad
2 - Poor
3 - Fair
4 - Good
5 - Excellent

Your rated scores will be saved automatically. When you finish, please click Submit at the end of this page.

<style>
select {
  padding: 2px;
  width: 50px
}
</style>

<div style="overflow: scroll">
<table>
    <tr>
        <td></td>
        <td>Enrollment</td>
        <td>Audio 1</td>
        <td>Audio 2</td>
        <td>Audio 3</td>
        <td>Audio 4</td>
        <td>Audio 5</td>
        <td>Audio 6</td>
        <td>Audio 7</td>
        <td>Audio 8</td>
    </tr>
    {% for samples in site.data.samples_short_shuffled_nmos %}
        <tr>
            <td>{{ samples.id }}</td>
            <td><audio controls><source src="{{ samples.enroll }}" type="audio/wav"></audio></td>
            {% for sample in samples.samples %}
            <script>
                window.addEventListener('load', function() {
                    var savedValue = localStorage.getItem('short.nmos.{{ samples.id }}.{{ forloop.index }}');
                    if (savedValue) {
                        document.getElementById('short.nmos.{{ samples.id }}.{{ forloop.index }}').value = savedValue;
                    }
                    var savedValue = localStorage.getItem('short.smos.{{ samples.id }}.{{ forloop.index }}');
                    if (savedValue) {
                        document.getElementById('short.smos.{{ samples.id }}.{{ forloop.index }}').value = savedValue;
                    }
                });
            </script>
            <td><audio controls><source src="{{ sample }}" type="audio/wav"></audio>
            <br>
            <label>Naturalness</label>
                <select id="short.nmos.{{ samples.id }}.{{ forloop.index }}" onchange="localStorage.setItem('short.nmos.{{ samples.id }}.{{ forloop.index }}', this.value)" onshow="console.log('hello')">
                    <option value="null">-</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <br>
            <label>Similarity</label>
                <select id="short.smos.{{ samples.id }}.{{ forloop.index }}" onchange="localStorage.setItem('short.smos.{{ samples.id }}.{{ forloop.index }}', this.value)">
                    <option value="null">-</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
            </td>
            {% endfor %}
        </tr>
    {% endfor %}
</table>
</div>

<script>
function submit() {
    const elements = document.querySelectorAll('[id^="short"]');
    const scores = Object.fromEntries(Array.from(elements).map(element => [element.id, element.value]))
    const scores_str = JSON.stringify(scores)
    document.getElementById("score_str").value = scores_str
    navigator.clipboard.writeText(scores_str)
    alert("Your scores were copied to the clipboard. Please send it back to the requester.")
}
</script>


<button onclick="submit()">Submit</button>

<label>Please send your scores back to the requester.</label>
<textarea id="score_str" style="width: 100%"></textarea>
