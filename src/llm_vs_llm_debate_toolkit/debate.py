import colorama
from colorama import Fore
import llm
from pydantic import BaseModel

colorama.init(autoreset=True)


class Question(BaseModel):
    text: str
    answer_a: str
    answer_b: str


class Agent(BaseModel):
    name: str
    model: str = "claude-3-sonnet-20240229"

    def generate_response(self, prompt: str) -> str:
        model = llm.get_model(self.model)
        response = model.prompt(prompt)
        return response.text()


class Debater(Agent):
    name: str
    position: str

    def generate_debater_prompt(
        self, position: str, question: Question, previous_statements: str
    ) -> str:
        prompt = f"""You are Debater {position}, arguing for the following answer:

        Answer {position}: {getattr(question, f'answer_{position.lower()}')}
        Previous statements are below:

        {previous_statements}

        Please provide your argument supporting Answer {position} in a clear and persuasive manner.

        """
        return prompt.strip()

    def generate_response(self, question: Question, previous_statements: str) -> str:
        prompt = self.generate_debater_prompt(self.position, question, previous_statements)
        return super().generate_response(prompt)


class Judge(Agent):

    def generate_judge_prompt(self, transcript: str) -> str:
        prompt = f"""
    You are a neutral judge evaluating a debate between Debater A and Debater B on the
    following question:

    {transcript}

    Based on the arguments presented, please decide which answer is more convincing, A or B,
    and briefly explain your reasoning.
    """
        return prompt.strip()

    def make_decision(self, transcript: list[str]) -> str:
        prompt = self.generate_judge_prompt(transcript)
        decision = super().generate_response(prompt)
        return "A" if "A" in decision.upper() else "B"


class DebateResult(BaseModel):
    transcript: str
    decision: str


def run_debate(
    question: Question, debater_a: Debater, debater_b: Debater, judge: Judge, rounds: int = 3
) -> DebateResult:
    transcript = f"Question: {question.text}\n"
    transcript += f"Answer A: {question.answer_a}\n"
    transcript += f"Answer B: {question.answer_b}\n"

    previous_statements = ""

    for round_num in range(1, rounds + 1):
        transcript += f"\nRound {round_num}:\n"
        print(f"\nRound {round_num}:\n")

        response_a = debater_a.generate_response(question, previous_statements)
        print(Fore.BLUE + f"Debater A: {response_a}")
        transcript += f"Debater A: {response_a}\n"
        previous_statements += f"Debater A: {response_a}\n"

        response_b = debater_b.generate_response(question, previous_statements)
        print(Fore.RED + f"Debater B: {response_b}")
        transcript += f"Debater B: {response_b}\n"
        previous_statements += f"Debater B: {response_b}\n"

    decision = judge.make_decision(transcript)
    transcript += f"\nJudge's Decision: {decision}\n"

    return DebateResult(transcript=transcript, decision=decision)


def main():
    question = Question(text="What is the capital of France?", answer_a="Paris", answer_b="London")

    debater_a = Debater(name="Debater A", position="A")
    debater_b = Debater(name="Debater B", position="B")
    judge = Judge(name="Judge")

    result = run_debate(question, debater_a, debater_b, judge)

    print(result.transcript)
    print(f"\nFinal decision: {result.decision}")


if __name__ == "__main__":
    main()
