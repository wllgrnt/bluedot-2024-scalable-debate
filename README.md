# LLM vs LLM Debate Toolkit

A library for running two-agent debates in response to a question, and judging the answer. This library will be used to identify the limits of scalability of debate - 
what the maximum Elo gap can be between debaters and judges before the debate mechanism begins to fail. This could be helpful when assessing far more capable models in 
the future. If scaling speed increases such that the capability delta between successive generations is above the Elo gap found here, then debate ceases to be a viable method
of scalable oversight. 

to do:
- prompt engineering, to run the debate successfully
- find a question bank (or make one) for debate. read the papers below to see what they use.
- use replicate/ollama to hit the different ELOs and see how after higher ELO chatbots win, based on how subjective the position is.
- get a graph of win % vs ELO


Project submitted as part of the AI Alignment course run by BlueDot Impact, June 2024 cohort.

Relevant reading:
- Irving et al. (2018): "AI Safety via Debate" - Foundational work on using debate for AI oversight.
- Saunders et al. (2022): "Self-critiquing models for assisting human evaluators" - Recent work on using language models to assist human evaluation.
- Michael et al. (2023) "Debate helps supervise unreliable experts"
- Choen et al. (2023) "LM vs LM: Detecting Factual Errors via Cross Examination"
- Khan et al. (2024)"Debating with More Persuasive LLMs Leads to More Truthful Answers"


## Installation

Git clone, then `pip install .` from the repo root. Then run `llm install llm-claude-3` to install the Claude set of models, and provide keys with `llm keys set claude`.
