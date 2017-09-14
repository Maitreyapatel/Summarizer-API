# Summarizer-API
<h2>API system for product review summary</h2>
<h4>Requirements</h4>
<p>Same as my project of amazon product review <a href="https://github.com/Maitreyapatel/Review-Summarizer">summarizer.</a></p>
<p>In addition <b>>Django1.10.0</b> is required.</p>

<h2>Running system</h2>
<ol>
  <li>Go inside the project folder</li>
  <li>Perform python3 manage.py makemigrations</li>
  <li>Also perform python3 manage.py migrate</li>
  <li>Then python3 manage.py runserver</li>
<ol>
 
<h2>Testing the system</h2>
<p>Also install http (pip3 install httpie).</p>
<p>For authantication user <b>username</b>:username and <b>password</b>:password</p>
<p>Now, open the terminal and run command: http -a username:password POST http://127.0.0.1:8000/snippets/ code="<All reviews>"</p>
