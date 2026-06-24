import os
import sys

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


# ==============================
# Load Environment Variables
# ==============================

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")


if not OPENROUTER_API_KEY:
    raise ValueError("OPENROUTER_API_KEY is missing in .env")

if not MODEL_NAME:
    raise ValueError("MODEL_NAME is missing in .env")


# ==============================
# Initialize LLM
# ==============================

llm = ChatOpenAI(
    model=MODEL_NAME,
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3
)


# ==============================
# Helper Function
# Load Prompt Files
# ==============================

def load_prompt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()



# ==============================
# Load Five Prompts
# ==============================

prompt1 = PromptTemplate(
    input_variables=["project_description"],
    template=load_prompt(
        "prompts/prompt1_interpret_request.txt"
    )
)


prompt2 = PromptTemplate(
    input_variables=["stage1_output"],
    template=load_prompt(
        "prompts/prompt2_identify_categories.txt"
    )
)


prompt3 = PromptTemplate(
    input_variables=[
        "stage1_output",
        "stage2_output"
    ],
    template=load_prompt(
        "prompts/prompt3_select_category.txt"
    )
)


prompt4 = PromptTemplate(
    input_variables=[
        "project_description",
        "stage3_output"
    ],
    template=load_prompt(
        "prompts/prompt4_extract_missing_requirements.txt"
    )
)


prompt5 = PromptTemplate(
    input_variables=[
        "project_description",
        "stage3_output",
        "stage4_output"
    ],
    template=load_prompt(
        "prompts/prompt5_generate_assessment.txt"
    )
)



# ==============================
# Create LCEL Chains
# ==============================


chain1 = prompt1 | llm | StrOutputParser()

chain2 = prompt2 | llm | StrOutputParser()

chain3 = prompt3 | llm | StrOutputParser()

chain4 = prompt4 | llm | StrOutputParser()

chain5 = prompt5 | llm | StrOutputParser()



# ==============================
# Main Execution
# ==============================


if len(sys.argv) < 2:
    print(
        "Usage: python main.py \"your project description\""
    )
    sys.exit(1)



project_description = sys.argv[1]


# -------- Stage 1 --------

stage1_output = chain1.invoke(
    {
        "project_description": project_description
    }
)

print("\n========== STAGE 1 ==========")
print(stage1_output)



# -------- Stage 2 --------

stage2_output = chain2.invoke(
    {
        "stage1_output": stage1_output
    }
)

print("\n========== STAGE 2 ==========")
print(stage2_output)



# -------- Stage 3 --------

stage3_output = chain3.invoke(
    {
        "stage1_output": stage1_output,
        "stage2_output": stage2_output
    }
)

print("\n========== STAGE 3 ==========")
print(stage3_output)



# -------- Stage 4 --------

stage4_output = chain4.invoke(
    {
        "project_description": project_description,
        "stage3_output": stage3_output
    }
)

print("\n========== STAGE 4 ==========")
print(stage4_output)



# -------- Stage 5 --------

final_assessment = chain5.invoke(
    {
        "project_description": project_description,
        "stage3_output": stage3_output,
        "stage4_output": stage4_output
    }
)


print("\n========== FINAL PROJECT ASSESSMENT ==========")
print(final_assessment)