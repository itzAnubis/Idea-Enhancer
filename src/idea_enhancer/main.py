#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from idea_enhancer.crew import IdeaEnhancer

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")
# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew with a starting idea.
    """
    # Change this to whatever idea you want to discuss
    print("## Enter the idea you want the board to enhance:")
    user_idea_input = input(">> ")

    inputs = {
        'user_idea': user_idea_input,
        'current_year': str(datetime.now().year)
    }

    try:
        IdeaEnhancer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    print("## Enter the idea you want to train the crew on:")
    user_idea = input(">> ")
    inputs = {
        "user_idea": user_idea,
        'current_year': str(datetime.now().year)
    }
    try:
        IdeaEnhancer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        IdeaEnhancer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    print("## Enter the idea you want to test the crew on:")
    user_idea = input(">> ")
    inputs = {
        "user_idea": user_idea,
        'current_year': str(datetime.now().year)
    }

    try:
        IdeaEnhancer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = IdeaEnhancer().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
