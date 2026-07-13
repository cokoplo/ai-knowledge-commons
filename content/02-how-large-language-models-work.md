---
last_reviewed: 2026-07-13
---
<!-- License: CC BY 4.0 -->

# 02 — How Large Language Models Work

**Audience:** curious learners with basic tech literacy. **Time:** ~12 minutes.

## What is a language model?

A language model estimates the probability of the next word (or "token") given
the words before it. A **large** language model (LLM) is simply one trained on a
very large corpus of text.

## The core idea: prediction

Given *"The capital of France is"*, a well-trained model assigns high probability
to *"Paris"*. It does this by having learned statistical relationships across
billions of examples.

## Tokens, not words

Text is split into **tokens** — short chunks that may be whole words, parts of
words, or punctuation. Processing happens token by token.

## Training in two stages

1. **Pre-training:** the model learns general language patterns by predicting
   tokens across a huge dataset (books, articles, code, web text).
2. **Fine-tuning / alignment:** the model is further adjusted — often with human
   feedback — to be more helpful, accurate, and safe.

## Why it can be wrong

LLMs optimize for *plausible* text, not *verified* truth. They can confidently
state falsehoods ("hallucination"). Always verify important claims against
primary sources.

## Practical takeaways

- Be specific in your prompts; context improves relevance.
- Treat output as a draft to check, not a verdict.
- Understand the model's limits before relying on it for decisions.

## Further reading

See `03-ai-literacy-and-ethics.md` and `resources/free-learning-resources.md`.
