# Evaluating SENSEI
This repository contains the results of three experiments using [SENSEI](https://github.com/sensei-chat/sensei). SENSEI is an automated end-to-end test system for chatbots, made of a user simulator, and a system to define and test checking rules on the generated conversations.

The two experiments consisted of:
- Mutation analysis of 4 chatbots created using [Taskyto](https://github.com/satori-chatbots/taskyto), published in this [paper](https://dl.acm.org/doi/10.1145/3640794.3665538), and freely available on Taskyto's repository. These results are in folder [mutation_analysis](./mutation-analysis).
- Mutation analysis of 4 chatbots created using Rasa, published in the same paper, and available [here](./rasa-chatbots). The results are available in folder [mutation_analysis](./mutation-analysis).
- Test of some chatbots "in the wild", deployed on various websites. 
