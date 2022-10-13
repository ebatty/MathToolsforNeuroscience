# Key Concepts

## Basic Probability

Given two events A and B:

- **Joint probability**= p(A and B) = p(A ∩ B) = probability that both A and B occur
- **Marginal probability** = p(A) = probability that A occurs
- **Conditional probability** = p(A|B) = probability of A occuring given that event B occured

- They are connected with this formula:

$$P(A | B) = \frac{P(A \text{ and } B)}{P(B)} $$

- If two events are **independent** (probability of one event is not affected by the other occuring), the joint can be written as the product of the marginals and the conditional probability of A given B just equals the marginal probability of A:

$$P(A \text{ and } B) = P(A) * P(B) $$

$$P(A | B) = P(A) $$

- If two events are **mutually exclusive** (A cannot occur if B occurs and vice versa), then their joint probability is 0 and the probability of one or the other occuring can be written as the sum of the marginals:

$$P(A \text{ and } B) = 0 $$

$$P(A \text{ or } B) = P(A) + P(B)$$

- We can derive **Bayes' Rule** from the above facts:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)} $$

We call P(A|B) the **posterior**, P(B|A) the **likelihood**, p(A) the **prior** probability, and p(B) the **marginal** probability. So the Bayes' Rule states that the posterior equals the likelihood times the prior divided by the marginal

- These terms make a bit more sense if we use Bayes' rule in the context it often is used, where A is the hypothesis (H) and B is the evidence (e) :

$$P(H|e) = \frac{P(e|H)P(H)}{P(e)} $$

We can see that the posterior probability that a hypothesis is true given the evidence (P(H|e)) is equal to the prior probability that the hypothesis is true before evidence is collected, p(H), times the likelihood of seeing the evidence given the hypothesis is true (P(e|H)), divided by the marginal probability of seeing the evidence (P(e)).

