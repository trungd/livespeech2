---
layout: page
title: "Evaluation Form (Long Speech)"
--- 

## Instructions


Please listen to the entire audio clip and rate it based on two criteria:

1. Naturalness
2. Similarity to the enrollment speech

Use the following scale for your ratings:

- 1 - Bad
- 2 - Poor
- 3 - Fair
- 4 - Good
- 5 - Excellent

Your scores will be saved automatically. You can close and reopen this page at any time.

Once you have completed your ratings, click Submit at the end of the page to send your scores.

Your contribution is greatly appreciated. Thank you!

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
    </tr>
    {% for samples in site.data.samples_long_shuffled_nmos %}
        <tr>
            <td>{{ samples.id }}</td>
            <td><audio controls><source src="{{ samples.enroll }}" type="audio/wav"></audio></td>
            {% for sample in samples.samples %}
            <script>
                window.addEventListener('load', function() {
                    var savedValue = localStorage.getItem('long.nmos.{{ samples.id }}.{{ forloop.index }}');
                    if (savedValue) {
                        document.getElementById('long.nmos.{{ samples.id }}.{{ forloop.index }}').value = savedValue;
                    }
                    var savedValue = localStorage.getItem('long.smos.{{ samples.id }}.{{ forloop.index }}');
                    if (savedValue) {
                        document.getElementById('long.smos.{{ samples.id }}.{{ forloop.index }}').value = savedValue;
                    }
                });
            </script>
            <td><audio controls><source src="{{ sample }}" type="audio/wav"></audio>
            <br>
            <label>Naturalness</label>
                <select id="long.nmos.{{ samples.id }}.{{ forloop.index }}" onchange="localStorage.setItem('long.nmos.{{ samples.id }}.{{ forloop.index }}', this.value)" onshow="console.log('hello')">
                    <option value="null">-</option>
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                </select>
                <br>
            <label>Similarity</label>
                <select id="long.smos.{{ samples.id }}.{{ forloop.index }}" onchange="localStorage.setItem('long.smos.{{ samples.id }}.{{ forloop.index }}', this.value)">
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
    const elements = document.querySelectorAll('[id^="long"]');
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
