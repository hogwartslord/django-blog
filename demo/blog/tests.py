from django.test import TestCase

# Create your tests here.
{ % ifequal
a1
a2 %}
< h1 > equal! < / h1 >
{ % else %}
< h1 >
not equal! < / h1 >
{ % endifequal %}