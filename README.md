# article-summarizer
A general purpose text summarizing bot will simply give you a broad summary of what the article is about. The goal of this bot is more microscoppic though. What if the article is not a political news article and instead it's something boiler plate like a recipe or a tech announcement article where the reader ultimately only needs a handful of relevant lines from the article? In the case of a recipe, the reader does not actually need a long and hearty preamble about the authors motivation -- the reader just wants to know the steps that go into the recipe.

# Example: 

###### Summary

Nvidia GeForce RTX 3080 Specs, Price, and Release Date:
The RTX 3080 starts at $699 and will be available September 17.

Nvidia GeForce RTX 3070 Specs, Price, and Release Date:
The RTX 3070 will launch in October, starting at $499, which is less than half the RTX 2080 Ti's current prices.

Nvidia GeForce RTX 3090 Specs, Price, and Release Date:
It starts at $1,499 and will be available on September 24.

###### Original Article

Nvidia just announced its new slate of next-generation graphics cards. The lineup is headed by the flagship GeForce RTX 3080, the successor to the most powerful mainstream graphics card of the last two years, the Nvidia RTX 2080 Ti. As you might expect, this new GPU brings more CUDA, RT, and Tensor cores along with faster memory and perhaps most interestingly a new cooling design, all of which lead to some very promising performance numbers.

All told, Nvidia announced three new GPUs today: the RTX 3080, RTX 3070, and a new high-end "BFGPU" called the RTX 3090. More on that beast in a second.

Nvidia GeForce RTX 3080 Specs, Price, and Release Date
The new Nvidia GeForce RTX 3080 has 10GB of GDDR6X, capable of 30 shader-tflops, 58 RT-tflops, and 238 Tensor-tflops. According to Nvidia, it's twice as powerful as the RTX 2080. The RTX 3080 starts at $699 and will be available September 17.

Nvidia GeForce RTX 3070 Specs, Price, and Release Date
Stepping down from the 3080 is the RTX 3070. This new GPU has 8GB GDDR6 memory, is capable of 20 shader-tflops, 40 RT-tflops, and 163 Tensor-tflops, and according to Nvidia is more powerful than the RTX 2080 Ti – currently the most powerful mainstream graphics card available. The RTX 3070 will launch in October, starting at $499, which is less than half the RTX 2080 Ti's current prices.

Nvidia GeForce RTX 3090 Specs, Price, and Release Date
At the top of the pile is the RTX 3090, the Titan of this generation (without the Titan branding). This absolute monster of a card (seriously, it's huge) has a ridiculous 24GB of GDDR6X memory, and can push out 36 shader-tflops, 69 RT-tflops, and 285 Tensor-tflops of GPU power. Nvidia claims the card is capable of playing games at 60 fps in 8K. It starts at $1,499 and will be available on September 24.


# Algorithm
###### General summarizing
* 1 ) Word association (e.g. 'City', 'Cities')
* 2 ) Calculate occurences of each word in the artic
* 3 ) Assign each word a ranking based on the occurences
* 4 ) Detect periods that do not represent end of sentences (e.g. 'Mr.' is not a full stop)
* 5 ) Split article into individual sentences
* 6 ) Rank sentences based on the sum of the ranking of the words in them
* 7 ) Return X of the most highly ranked sentences in chronological order
