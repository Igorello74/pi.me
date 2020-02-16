# pie.me
A brand-new compression algorithm based on using various irrational numbers.

## How does it work?
Imagine an irrational number, Pi, for instance. Let's take it's first digits in hexadecimal notation (for convinience).
Also, imagine that we have an abstract file. Here they are:
|π (in hex)|File contents (in hex)|
|---|---|
|`3.243f6a8885a308d313198a2e03707344a40…`|`3f195a3103702e30`|

Then, let's separate this file in segments (called *clasters*) that can be found in the Pi and encode them in such a form:
> [**serial number** after the point] - [**length** of the cluster] *(all numbers in decimal notation)*

|**Separated**|3f|19|5a|31|0370|2e|30
|---|---|---|---|---|---|---|---|
|**Encoded**|3-2 | 19-2 | 10-2 | 16-2 | 25-4 | 23-2 | 12-2|

![](/layout.svg)

### Note
This explaination is rough and doesn't disclose some details (particularly, how the file is separated in *clasters*
and how the output file is generated).
