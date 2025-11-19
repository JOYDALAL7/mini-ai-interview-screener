from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

# load env vars
load_dotenv()

app = FastAPI()

# initialize openai client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


# request models
class EvaluateRequest(BaseModel):
    answer: str


class RankRequest(BaseModel):
    answers: List[str]


# --- evaluate a single answer ---
@app.post("/evaluate-answer")
async def evaluate_answer(req: EvaluateRequest):
    try:
        prompt = f"""
        You are evaluating a candidate's interview answer.

        Candidate's response: "{req.answer}"

        Return ONLY a valid JSON object in this format:
        {{
          "score": 1-5,
          "summary": "short one-line summary",
          "improvement": "one improvement suggestion"
        }}
        Make sure the output is ONLY JSON. No extra text.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )

        raw = response.choices[0].message.content.strip()

        # sometimes the model may return extra characters, so extract JSON safely
        try:
            data = json.loads(raw)
        except:
            # try to extract JSON substring manually
            start = raw.find("{")
            end = raw.rfind("}") + 1
            json_str = raw[start:end]
            data = json.loads(json_str)

        return data

    except Exception as e:
        print("ERROR inside /evaluate-answer:", e)
        return {"error": str(e)}


# --- rank multiple candidates ---
@app.post("/rank-candidates")
async def rank_candidates(req: RankRequest):

    results = []

    for ans in req.answers:
        evaluated = await evaluate_answer(EvaluateRequest(answer=ans))

        # skip failed evaluations
        if "error" in evaluated:
            continue

        results.append({
            "answer": ans,
            "score": evaluated.get("score", 0),
            "summary": evaluated.get("summary", "")
        })

    results.sort(key=lambda x: x["score"], reverse=True)

    return {"ranked_candidates": results}
