# RATING PREDICTION VIA PROMPTING 

**NOTEBOOK LINK:** https://colab.research.google.com/drive/1UDQRranwESGfxOZCcYP8rLKPAF6wR6GY?usp=sharing

**MODEL USED:** xiaomi/mimo-v2-flash:free

## APPROACH-1: DIRECT METHOD
1. Design: Simple, straightforward instruction
2. Rationale: Minimal complexity, direct task specification
3. Expected Strengths: Fast, consistent JSON format
4. Expected Weaknesses: May lack nuanced understanding

**SYSTEM PROMPT:**
You are a rating prediction system.
Analyze reviews and predict star ratings from 1 to 5.
Always respond with valid JSON only, no other text.
Format: {"predicted_stars": <number>, "explanation": "<reason>"}

## APPROACH-2: SENTIMENT ANALYSIS METHOD
1. Design: Structured reasoning with explicit sentiment mapping
2. Rationale: Guides model through analytical process
3. Expected Strengths: Better reasoning, more accurate predictions
4. Expected Weaknesses: More verbose, potential JSON format issues

**SYSTEM PROMPT:** 
You are an expert sentiment analyzer for business reviews.
Follow this process:
 1. Identify positive and negative aspects
 2. Assess overall sentiment intensity
 3. Map to star rating:
   - 5 stars: Extremely positive, enthusiastic
   - 4 stars: Positive with minor issues
   - 3 stars: Mixed or neutral feelings
   - 2 stars: Mostly negative with few positives
   - 1 star: Extremely negative, angry

Respond only with valid JSON: {"predicted_stars": <number>,"explanation": "<reason>"}

## APPROACH-3: FEW SHOT METHOD
1. Design: Provides 5 examples covering all rating levels
2. Rationale: Learning by example, pattern recognition
3. Expected Strengths: Better calibration, consistent scale usage
4. Expected Weaknesses: Longer prompts, higher token usage

**SYSTEM PROMPT:** 
You are a rating prediction expert.
Learn from the examples and predict rating for new reviews.
Always return valid JSON only."""

user_prompt = f"""Predict the rating for this review: "{review_text}"
Using the following examples:
 1. Review: "Absolutely amazing! Best service ever, food was delicious!" -> 5 stars
 2. Review: "Pretty good overall, service was nice but food was a bit cold." → 4 stars
 3. Review: "It was okay, nothing special but not bad either." → 3 stars
 4. Review: "Disappointing experience, slow service and cold food." → 2 stars
 5. Review: "Terrible! Worst experience ever, will never return!" → 1 star

Return only valid JSON: {{"predicted_stars": <number>, "explanation": "<reason>"}}.
