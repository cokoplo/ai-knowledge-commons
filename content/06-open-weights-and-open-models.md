---
last_reviewed: 2026-07-13
---
# 6. Open Weights and Open Models

*Educational explainer · CC BY 4.0 · AI Knowledge Commons*

A recurring theme in this project is *open* technology. This article explains what
"open weights" means and why it matters for public AI literacy.

## What are model "weights"?

A large language model is defined by its **weights** — the numerical parameters
learned during training. Weights are the part you download and run. The *code* that
trains a model and the *data* it was trained on are separate questions.

## Closed vs. open

| Aspect | Closed model | Open-weights model |
| --- | --- | --- |
| Weights published | No | Yes |
| Run on your own hardware | No | Yes |
| Inspect / modify | No | Yes |
| Typical examples | Proprietary APIs | Community-released models |

"Open" is a spectrum: a model may publish weights but not training data or code.
Be precise about which kind of openness you mean.

## Why open weights help the public

- **Transparency**: researchers can study behavior directly instead of guessing.
- **Access**: anyone can run the model without paying a gatekeeper per request.
- **Resilience**: no single company can silently change or withdraw the model.
- **Local privacy**: sensitive tasks can run on your own machine.

## Honest caveats

- Open weights are not automatically safe; they still need evaluation and guardrails.
- Training data openness matters for reproducibility and for copyright questions.
- "Open" models may still carry licenses with usage restrictions.

## How this fits our mission

As an open educational initiative, we favor openly licensed and openly runnable
tooling so that AI literacy is something the public can *do*, not just *subscribe to*.

## Further reading

- `02-how-large-language-models-work.md` — background on how models are built.
- `05-responsible-use-of-ai-tools.md` — running models responsibly, including locally.
