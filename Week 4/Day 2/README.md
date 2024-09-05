# Week 4: Day 2 Session

In today's assignment, we'll be verifying OpenAI's claims about their Embedding models using Ragas and LCEL RAG chains!

- 🤝 Breakout Room #1
  1. Task 1: Installing Required Libraries
  2. Task 2: Set Environment Variables
  3. Task 3: Creating a Simple RAG Pipeline with LangChain v.0.2.0
  4. Task 4: Synthetic Dataset Generation for Evaluation using Ragas (Optional)

- 🤝 Breakout Room #2
  1. Task 5: Evaluating our Pipeline with Ragas
  2. Task 6: Testing OpenAI's Claim
  3. Task 7: Selecting an Advanced Retriever and Evaluating
    
The notebook Colab link is located [here](https://colab.research.google.com/drive/13VsLN6BpARlAreNDBR2klZK9BiOeZV5S?usp=sharing)

## Ship 🚢

The completed notebook!

<details>
<summary>🚧 BONUS CHALLENGE 🚧</summary>

> NOTE: Completing this challenge will provide full marks on the assignment, regardless of the complete of the notebook. You do not need to complete this in the notebook for full marks.

##### **MINIMUM REQUIREMENTS**:

1. Baseline `LCEL RAG` Application using `NAIVE RETRIEVAL`
2. Baseline Evaluation using `RAGAS METRICS`
  - [Faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/faithfulness.html)
  - [Answer Relevancy](https://docs.ragas.io/en/stable/concepts/metrics/answer_relevance.html)
  - [Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/context_precision.html)
  - [Context Recall](https://docs.ragas.io/en/stable/concepts/metrics/context_recall.html)
  - [Answer Correctness](https://docs.ragas.io/en/stable/concepts/metrics/answer_correctness.html)
3. Implement a `SEMANTIC CHUNKING STRATEGY`.
4. Create an `LCEL RAG` Application using `SEMANTIC CHUNKING` with `NAIVE RETRIEVAL`.
5. Compare and contrast results.

##### **SEMANTIC CHUNKING REQUIREMENTS**:

Chunk semantically similar (based on designed threshold) sentences, and then paragraphs, greedily, up to a maximum chunk size. Minimum chunk size is a single sentence.

Have fun!
</details>

### Deliverables

- A short Loom of the notebook (or bonus challenge), and a 1min. walkthrough of the application in full

## Share 🚀

Make a social media post about your final application!

### Deliverables

- Make a post on any social media platform about what you built!

Here's a template to get you started:

```
🚀 Exciting News! 🚀

I am thrilled to announce that I have just built and shipped Synthetic Data Generation, benchmarking, and iteration with RAGAS & LangChain! 🎉🤖

🔍 Three Key Takeaways:
1️⃣ 
2️⃣ 
3️⃣ 

Let's continue pushing the boundaries of what's possible in the world of AI and question-answering. Here's to many more innovations! 🚀
Shout out to @AIMakerspace !

#LangChain #QuestionAnswering #RetrievalAugmented #Innovation #AI #TechMilestone

Feel free to reach out if you're curious or would like to collaborate on similar projects! 🤝🔥
```